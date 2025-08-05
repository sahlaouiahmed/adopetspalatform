from django.core.paginator import Paginator, Page
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Pet, AdoptionRequest
from django.contrib.auth.models import User
from .forms import PetSearchForm, AdoptionRequestForm, AdoptionRequestFilterForm, PetForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.paginator import Paginator


# Display the index page with search functionality
def index(request):
    form = PetSearchForm(request.GET)
    pets = Pet.objects.all()

    if form.is_valid():
        if form.cleaned_data['species']:
            pets = pets.filter(species__icontains=form.cleaned_data['species'])
        if form.cleaned_data['breed']:
            pets = pets.filter(breed__icontains=form.cleaned_data['breed'])
        if form.cleaned_data['city']:
            pets = pets.filter(city__icontains=form.cleaned_data['city'])
        if form.cleaned_data['country']:
            pets = pets.filter(country__icontains=form.cleaned_data['country'])
        if form.cleaned_data['posted_by']:
            pets = pets.filter(posted_by__username__icontains=form.cleaned_data['posted_by'])

    return render(request, 'adopets_platform/index.html', {'form': form, 'pets': pets})




# Display the details of a specific pet
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adopets_platform/pet_detail.html', {'pet': pet})

# Handle user registration
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Submit an adoption request for a pet
from django.core.mail import send_mail
from django.conf import settings

@login_required
def adopt_request(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    owner_name = pet.posted_by.username
    owner_email = pet.posted_by.email  # 👈 Owner's email
    requester_name = request.user.username
    requester_email = request.user.email

    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST, initial={'email': requester_email})
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.email = requester_email 
            adoption_request.user = request.user  
            adoption_request.pet = pet
            adoption_request.requester = request.user  
            adoption_request.save()

            # ✉️ Notify Pet Owner
            send_mail(
                subject=f"New Adoption Request for {pet.name}",
                message=(
                    f"Hi {owner_name},\n\n"
                    f"You have received a new adoption request for your pet '{pet.name}' from {requester_name} "
                    f"({requester_email}). Please log in to review the request.\n\nThanks,\nAdopet Platform"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[owner_email],
                fail_silently=False,
            )

            # ✉️ Confirm to Requester
            send_mail(
                subject=f"Your Request for {pet.name} Has Been Sent",
                message=(
                    f"Hi {requester_name},\n\n"
                    f"Your request to adopt '{pet.name}' has been successfully sent to {owner_name}. "
                    f"You'll be contacted once it's reviewed.\n\nThanks,\nAdopet Platform"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[requester_email],
                fail_silently=False,
            )

            return redirect('success_page')
    else:
        form = AdoptionRequestForm(initial={'email': requester_email}, requester_name=requester_name, owner_name=owner_name, pet_name=pet.name)
    
    return render(request, 'adopets_platform/adopt_request.html', {'form': form})


def success_page(request):
    return render(request, 'adopets_platform/success_page.html')

# Display the adoption requests made by the user
@login_required
def my_adoption_requests(request):
    adoption_requests = AdoptionRequest.objects.filter(requester=request.user)
    if request.method == 'GET':
        form = AdoptionRequestFilterForm(request.GET)
        if form.is_valid():
            status = form.cleaned_data.get('status')
            if status:
                adoption_requests = adoption_requests.filter(status=status)
    else:
        form = AdoptionRequestFilterForm()
    return render(request, 'adopets_platform/adoptionrequests.html', {'adoption_requests': adoption_requests, 'form': form})

# Display the adoption requests received by the user
@login_required
def received_adoption_requests(request):
    pets = Pet.objects.filter(posted_by=request.user)
    adoption_requests = AdoptionRequest.objects.filter(pet__in=pets).order_by('-created_at')
    return render(request, 'adopets_platform/received_adoption_requests.html', {'adoption_requests': adoption_requests})

# Update the status of an adoption request

@require_POST
@login_required
def update_status(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id)
    new_status = request.POST.get('status')

    if new_status in ['pending', 'approved', 'rejected']:
        adoption_request.status = new_status
        adoption_request.save()

        # Prepare dynamic message based on status
        if new_status == 'approved':
            message_body = (
                f"Dear {adoption_request.requester.first_name},\n\n"
                f"Fantastic news! Your adoption request for {adoption_request.pet.name} has been **APPROVED** 🎉.\n\n"
                f"Here are the details:\n"
                f"- Pet Name: {adoption_request.pet.name}\n"
                f"- Breed: {adoption_request.pet.breed}\n"
                f"- Age: {adoption_request.pet.age} years\n"
                f"- Owner Name: {adoption_request.pet.posted_by.get_full_name()}\n"
                f"- Owner Contact: {adoption_request.pet.posted_by.email}\n\n"
                "Please reach out to the owner to arrange pickup or delivery. They will provide further guidance.\n\n"
                "We’re thrilled for you — congratulations on your new furry friend!\n\n"
                "Warm regards,\n"
                "Adopets Team 🐾"
            )
        elif new_status == 'rejected':
            message_body = (
                f"Dear {adoption_request.requester.first_name},\n\n"
                f"We're sorry to inform you that your request to adopt {adoption_request.pet.name} has been **REJECTED**.\n\n"
                "Don't worry — there are many pets still looking for loving homes on our platform. 💔🐶🐱\n"
                "Explore the listings and find your perfect companion!\n\n"
                "Thank you for being part of Adopets."
            )
        else:
            message_body = (
                f"Dear {adoption_request.requester.first_name},\n\n"
                f"Your request to adopt {adoption_request.pet.name} is currently **PENDING**.\n\n"
                "The pet’s owner is reviewing your application. We’ll notify you once there is an update.\n\n"
                "Thank you for your patience!"
            )

        # Send email to requester
        send_mail(
            subject=f'Adopets Update: {adoption_request.pet.name} adoption status',
            message=message_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[adoption_request.requester.email],
            fail_silently=False,
        )

        messages.success(request, f'Status updated to {new_status}.')
    else:
        messages.error(request, 'Invalid status update.')

    return redirect('received_adoption_requests')


# Display the pets posted by the user
@login_required
def my_posted_pets(request):
    if request.user.is_authenticated:
        posted_pets = Pet.objects.filter(posted_by=request.user)
        return render(request, 'adopets_platform/my_posted_pets.html', {'posted_pets': posted_pets})
    else:
        return redirect('account_login')

# Add a new pet to the platform
@login_required
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.posted_by = request.user
            pet.save()
            messages.success(request, 'Pet added successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error adding your pet. Please try again.')
    else:
        form = PetForm()
    return render(request, 'adopets_platform/add_pet.html', {'form': form})

# Delete an adoption request made by the user
@require_POST
@login_required
def delete_adoption_request(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id, requester=request.user)
    adoption_request.delete()
    messages.success(request, 'Adoption request successfully deleted.')
    return redirect('my_adoption_requests')


# Edit a pet
@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.user != pet.posted_by:
        return redirect('my_posted_pets')
    
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet updated successfully.')
            return redirect('my_posted_pets')
    else:
        form = PetForm(instance=pet)
    
    return render(request, 'adopets_platform/edit_pet.html', {'form': form, 'pet': pet})

# Delete a pet
@require_POST
@login_required
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, posted_by=request.user)
    pet.delete()
    messages.success(request, 'Pet deleted successfully.')
    return redirect('my_posted_pets')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pet, ContactMessage  # Pet and ContactMessage
from .forms import ContactOwnerForm

@login_required
def contact_owner(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == 'POST':
        form = ContactOwnerForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']

            # Save the message to DB
            ContactMessage.objects.create(
                pet=pet,
                sender_name=name,
                sender_email=email,
                message=message_content
            )
            # Send email to pet owner
            send_mail(
                subject=f"New message about your pet: {pet.name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[pet.posted_by.email],  # Assuming pet.owner.email exists
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent to the owner!')
            return redirect('pet_detail', pet_id=pet.id)
    else:
        form = ContactOwnerForm()

    return render(request, 'adopets_platform/contact_owner.html', {
        'pet': pet,
        'form': form
    })
