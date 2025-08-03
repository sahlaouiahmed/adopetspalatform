############### PASS ######################
from django.test import TestCase, Client
from django.urls import reverse
from adopets_platform.models import Pet, User

class PetDetailViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.url = reverse('pet_detail', args=[self.pet.id])

    def test_pet_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/pet_detail.html')

    def test_pet_detail_view_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Buddy')
        self.assertContains(response, 'Golden Retriever')
        self.assertContains(response, 'Pet City')



############# PASS ##############
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import AdoptionRequest, Pet
from adopets_platform.forms import AdoptionRequestFilterForm

class MyAdoptionRequestsViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.adoption_request = AdoptionRequest.objects.create(
            pet=self.pet, requester=self.user, message='I want to adopt Buddy', status='pending'
        )
        self.url = reverse('my_adoption_requests')
        self.client.login(username='testuser', password='testpassword')

    def test_my_adoption_requests_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/adoptionrequests.html')
    
    def test_my_adoption_requests_view_with_requests(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'I want to adopt Buddy')
        self.assertContains(response, 'pending')

    def test_my_adoption_requests_view_with_filter(self):
        response = self.client.get(self.url, {'status': 'pending'})
        self.assertContains(response, 'I want to adopt Buddy')
        self.assertContains(response, 'pending')

        response = self.client.get(self.url, {'status': 'approved'})
        self.assertNotContains(response, 'I want to adopt Buddy')

    def test_my_adoption_requests_view_no_requests(self):
        self.adoption_request.delete()
        response = self.client.get(self.url)
        self.assertContains(response, 'You have not submitted any adoption requests yet. Start finding your perfect pet and submit your first request!')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')


############### PASS ##################
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import Pet, AdoptionRequest

class ReceivedAdoptionRequestsViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.adoption_request = AdoptionRequest.objects.create(
            pet=self.pet, requester=self.user, message='I want to adopt Buddy', status='pending'
        )
        self.url = reverse('received_adoption_requests')

    def test_received_adoption_requests_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/received_adoption_requests.html')

    def test_received_adoption_requests_view_with_requests(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'I want to adopt Buddy')
        self.assertContains(response, 'pending')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

############ PASS ##############
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import AdoptionRequest, Pet

class UpdateStatusViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.adoption_request = AdoptionRequest.objects.create(
            pet=self.pet, requester=self.user, message='I want to adopt Buddy', status='pending'
        )
        self.url = reverse('update_status', args=[self.adoption_request.id])

    def test_update_status_view_valid_status(self):
        data = {'status': 'approved'}
        response = self.client.post(self.url, data)
        self.adoption_request.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('received_adoption_requests'))
        self.assertEqual(self.adoption_request.status, 'approved')

    def test_update_status_view_invalid_status(self):
        data = {'status': 'invalid_status'}
        response = self.client.post(self.url, data)
        self.adoption_request.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('received_adoption_requests'))
        self.assertNotEqual(self.adoption_request.status, 'invalid_status')
        self.assertEqual(self.adoption_request.status, 'pending')  # status should remain unchanged

    def test_update_status_view_login_required(self):
        self.client.logout()
        data = {'status': 'approved'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))



############### PASS ##################
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import Pet

class MyPostedPetsViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.url = reverse('my_posted_pets')

    def test_my_posted_pets_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/my_posted_pets.html')

    def test_my_posted_pets_view_with_pets(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Buddy')

    def test_my_posted_pets_view_no_pets(self):
        Pet.objects.filter(id=self.pet.id).delete()
        response = self.client.get(self.url)
        self.assertNotContains(response, 'Buddy')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

############### PASSSSS ##################
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import AdoptionRequest, Pet

class DeleteAdoptionRequestViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.adoption_request = AdoptionRequest.objects.create(
            pet=self.pet, requester=self.user, message='I want to adopt Buddy', status='pending'
        )
        self.url = reverse('delete_adoption_request', args=[self.adoption_request.id])

    def test_delete_adoption_request_view_status_code(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_adoption_requests'))
        self.assertFalse(AdoptionRequest.objects.filter(id=self.adoption_request.id).exists())

    def test_delete_adoption_request_view_message(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('my_adoption_requests'))
        self.assertContains(response, 'Adoption request successfully deleted.')

    def test_delete_adoption_request_view_login_required(self):
        self.client.logout()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')



############### PASS ##################
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import Pet
from adopets_platform.forms import PetForm

class EditPetViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.another_user = User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.url = reverse('edit_pet', args=[self.pet.id])

    def test_edit_pet_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/edit_pet.html')
        self.assertIsInstance(response.context['form'], PetForm)

    def test_edit_pet_view_post_valid(self):
        data = {
            'name': 'Max',
            'species': 'Dog',
            'breed': 'Labrador',
            'age': 2,
            'gender': 'Male',
            'description': 'Friendly',
            'city': 'Pet City',
            'country': 'Petland'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_posted_pets'))
        self.pet.refresh_from_db()
        self.assertEqual(self.pet.name, 'Max')
        self.assertEqual(self.pet.breed, 'Labrador')

    def test_edit_pet_view_post_invalid(self):
        data = {'name': ''}  # Invalid data: missing required fields
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/edit_pet.html')
        self.pet.refresh_from_db()
        self.assertNotEqual(self.pet.name, '')

    def test_edit_pet_view_permission_denied(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_posted_pets'))


############### PASS ###############
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import Pet

class DeletePetViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.pet = Pet.objects.create(
            name='Buddy', species='Dog', breed='Golden Retriever', age=3,
            gender='Male', description='Friendly and energetic', photo='path/to/photo',
            city='Pet City', country='Petland', posted_by=self.user
        )
        self.url = reverse('delete_pet', args=[self.pet.id])

    def test_delete_pet_view_status_code(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_posted_pets'))
        self.assertFalse(Pet.objects.filter(id=self.pet.id).exists())

    def test_delete_pet_view_message(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('my_posted_pets'))
        self.assertContains(response, 'Pet deleted successfully.')

    def test_delete_pet_view_login_required(self):
        self.client.logout()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')



################# PASS #####################
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from adopets_platform.models import Pet

class IndexViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        for i in range(15):
            Pet.objects.create(
                name=f'Buddy{i}', species='Dog', breed='Golden Retriever', age=3,
                gender='Male', description='Friendly and energetic', photo='path/to/photo',
                city='Pet City', country='Petland', posted_by=self.user
            )
        self.url = reverse('index')

    def test_index_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/index.html')

    def test_index_view_filters(self):
        # Test filtering by species
        response = self.client.get(self.url, {'species': 'Dog'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buddy0')
        
        # Test filtering by breed
        response = self.client.get(self.url, {'breed': 'Golden Retriever'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buddy0')
        
        # Test filtering by city
        response = self.client.get(self.url, {'city': 'Pet City'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buddy0')
        
        # Test filtering by country
        response = self.client.get(self.url, {'country': 'Petland'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buddy0')
        
        # Test filtering by posted_by
        response = self.client.get(self.url, {'posted_by': 'testuser'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buddy0')

###########################################
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from adopets_platform.models import Pet
from adopets_platform.forms import PetForm
from PIL import Image
import tempfile

class AddPetViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('add_pet')

    def test_add_pet_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/add_pet.html')
        self.assertIsInstance(response.context['form'], PetForm)

    def test_add_pet_view_post_valid(self):
        # Create a temporary image file
        with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
            image = Image.new('RGB', (100, 100))
            image.save(tmp, format='JPEG')
            tmp.seek(0)
            photo = SimpleUploadedFile(tmp.name, tmp.read(), content_type='image/jpeg')
            data = {
                'name': 'Buddy',
                'species': 'Dog',
                'breed': 'Golden Retriever',
                'age': 3,
                'gender': 'Male',
                'description': 'Friendly and energetic',
                'city': 'Pet City',
                'country': 'Petland',
                'photo': photo
            }
            response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(Pet.objects.filter(name='Buddy').exists())

    def test_add_pet_view_post_invalid(self):
        data = {'name': ''}  # Invalid data: missing required fields
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopets_platform/add_pet.html')
        self.assertFalse(Pet.objects.filter(name='').exists())
