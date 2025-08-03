from django.test import TestCase
from .forms import AdoptionRequestFilterForm

# Create your tests here.
class AdoptionRequestFilterFormTest(TestCase):
    def test_form_renders_status_choice_field(self):
        """
        Test that the form renders the status choice field with the correct CSS class.
        """
        form = AdoptionRequestFilterForm()
        self.assertIn('status', form.fields)
        self.assertEqual(form.fields['status'].widget.attrs['class'], 'form-control')

    def test_form_valid_data(self):
        """
        Test that the form is valid with valid data.
        """
        form = AdoptionRequestFilterForm(data={'status': 'approved'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['status'], 'approved')

    def test_form_empty_data(self):
        """
        Test that the form is valid with empty data (since all fields are optional).
        """
        form = AdoptionRequestFilterForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['status'], '')

    def test_form_invalid_data(self):
        """
        Test that the form is invalid with incorrect data.
        """
        form = AdoptionRequestFilterForm(data={'status': 'invalid_status'})
        self.assertFalse(form.is_valid())

if __name__ == '__main__':
    TestCase.run()

#-----------------------------------------------------------#
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PetForm
from .models import Pet

class PetFormTest(TestCase):
    def test_form_renders_all_fields(self):
        """
        Test that the form renders all expected fields.
        """
        form = PetForm()
        self.assertIn('name', form.fields)
        self.assertIn('age', form.fields)
        self.assertIn('breed', form.fields)
        self.assertIn('species', form.fields)
        self.assertIn('gender', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('photo', form.fields)
        self.assertIn('city', form.fields)
        self.assertIn('country', form.fields)

    def test_form_valid_data(self):
        """
        Test that the form is valid with valid data, including a valid photo upload.
        """
        with open('path/to/your/test_image.jpg', 'rb') as img:
            form = PetForm(data={
                'name': 'Buddy',
                'age': 3,
                'breed': 'Golden Retriever',
                'species': 'Dog',
                'gender': 'Male',
                'description': 'Friendly and energetic',
                'city': 'Pet City',
                'country': 'Petland'
            }, files={'photo': SimpleUploadedFile(img.name, img.read(), content_type='image/jpeg')})
            if not form.is_valid():
                print(form.errors)
            self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        """
        Test that the form is invalid with no data (all fields are required).
        """
        form = PetForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 9)  # Adjust the number based on required fields

if __name__ == '__main__':
    TestCase.run()


#-------------------------------------#
from django import forms
from .forms import UserRegistrationForm

class UserRegistrationFormTest(TestCase):
    def test_form_valid_data(self):
        """
        Test that the form is valid with valid data.
        """
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """
        Test that the form is invalid with incorrect data.
        """
        form_data = {
            'username': '',
            'email': 'not-an-email',
            'password1': 'password1',
            'password2': 'password2different',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_form_missing_field(self):
        """
        Test that the form is invalid when a required field is missing.
        """
        form_data = {
            'username': 'testuser',
            'email': '',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_password_mismatch(self):
        """
        Test that the form is invalid when the passwords do not match.
        """
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'differentpassword123',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)



#------------------------------#
from .forms import PetSearchForm

class PetSearchFormTest(TestCase):
    def test_form_valid_data(self):
        """
        Test that the form is valid with valid data.
        """
        form_data = {
            'species': 'Dog',
            'breed': 'Labrador',
            'city': 'New York',
            'country': 'USA',
            'posted_by': 'John Doe',
        }
        form = PetSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_blank_data(self):
        """
        Test that the form is valid with no data (all fields are optional).
        """
        form_data = {}
        form = PetSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_partial_data(self):
        """
        Test that the form is valid with partial data.
        """
        form_data = {
            'species': 'Dog',
            'breed': '',
            'city': 'San Francisco',
            'country': '',
            'posted_by': 'Jane Smith',
        }
        form = PetSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


#------------------------------------#
from .forms import AdoptionRequestForm

class AdoptionRequestFormTest(TestCase):
    def test_form_initial_message(self):
        """
        Test that the form initializes the message field with the correct template.
        """
        form_data = {
            'message': """Dear John Smith,

I hope this message finds you well. My name is Jane Doe, and I recently came across your post about Buddy. I wanted to express my heartfelt interest in adopting Buddy and providing them with a loving home.

From the description and photos, I can tell that Buddy is a wonderful pet. I am particularly drawn to their [mention specific traits or behavior you admire]. I believe Buddy would make a perfect addition to my family. We have [mention any other pets or family members] who are equally excited about the possibility of welcoming Buddy into our home.

I have experience caring for [mention any relevant experience with pets], and I am fully prepared to meet Buddy's needs, ensuring they live a happy and healthy life. I would love the opportunity to learn more about Buddy and discuss the adoption process in more detail.

Please let me know if there are any additional steps I need to take or if you require any further information from my end. You can reach me at janedoe@example.com.

Thank you so much for considering my request. I look forward to hearing from you soon.

Best regards,
Jane Doe"""
        }
        form = AdoptionRequestForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['message'], form_data['message'])

    def test_form_custom_initial_message(self):
        """
        Test that the form is valid with a custom initial message.
        """
        form_data = {
            'message': "Custom initial message."
        }
        form = AdoptionRequestForm(data=form_data, requester_name='Jane Doe', owner_name='John Smith', pet_name='Buddy', initial={'email': 'janedoe@example.com'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['message'], "Custom initial message.")
