from django.test import TestCase
from tips.forms import ArticleForm

class ArticleFormTest(TestCase):
    def test_form_valid_data(self):
        """
        Test that the form is valid with valid data.
        """
        form_data = {
            'title': 'Sample Article',
            'content': 'This is the content of the sample article.',
            'category': 'Technology',
        }
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_title(self):
        """
        Test that the form is invalid when the title is missing.
        """
        form_data = {
            'content': 'This is the content of the sample article.',
            'category': 'Technology',
        }
        form = ArticleForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_missing_content(self):
        """
        Test that the form is invalid when the content is missing.
        """
        form_data = {
            'title': 'Sample Article',
            'category': 'Technology',
        }
        form = ArticleForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_form_missing_category(self):
        """
        Test that the form is invalid when the category is missing.
        """
        form_data = {
            'title': 'Sample Article',
            'content': 'This is the content of the sample article.',
        }
        form = ArticleForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)
