from django import forms
from .models import User, AdoptionRequest
from .models import Pet

# Form for registering new users
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


# Form for searching pets with optional criteria
class PetSearchForm(forms.Form):
    species = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    breed = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    posted_by = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

from django import forms
from django.contrib.auth.models import User
from .models import AdoptionRequest

# Form for sending adoption requests with a pre-filled message
class AdoptionRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        requester_name = kwargs.pop('requester_name', 'Your Name')
        owner_name = kwargs.pop('owner_name', 'Owner\'s Name')
        pet_name = kwargs.pop('pet_name', 'Pet\'s Name')
        super(AdoptionRequestForm, self).__init__(*args, **kwargs)
        self.fields['message'].initial = f"""
Dear {owner_name},

I hope this message finds you well. My name is {requester_name}, and I recently came across your post about {pet_name}. I wanted to express my heartfelt interest in adopting {pet_name} and providing them with a loving home.

From the description and photos, I can tell that {pet_name} is a wonderful pet. I am particularly drawn to their [mention specific traits or behavior you admire]. I believe {pet_name} would make a perfect addition to my family. We have [mention any other pets or family members] who are equally excited about the possibility of welcoming {pet_name} into our home.

I have experience caring for [mention any relevant experience with pets], and I am fully prepared to meet {pet_name}'s needs, ensuring they live a happy and healthy life. I would love the opportunity to learn more about {pet_name} and discuss the adoption process in more detail.

Please let me know if there are any additional steps I need to take or if you require any further information from my end. You can reach me at {kwargs['initial']['email']}.

Thank you so much for considering my request. I look forward to hearing from you soon.

Best regards,
{requester_name}
"""

    class Meta:
        model = AdoptionRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Form for filtering adoption requests by status
class AdoptionRequestFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

# Form for submitting pet details
from django import forms
from adopets_platform.models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'gender', 'description', 'photo', 'city', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'species': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        

class ContactOwnerForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
