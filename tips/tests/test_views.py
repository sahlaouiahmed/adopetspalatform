from django.test import TestCase, Client
from django.urls import reverse
from tips.models import Article
from django.contrib.auth.models import User
from tips.forms import ArticleForm

################ PASS ###################
class ArticleListViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        for i in range(5):
            Article.objects.create(
                title=f'Article {i}', content='Content', category='Tech', author=self.user
            )
        self.url = reverse('article_list')

    def test_article_list_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/article_list.html')

    def test_article_list_view_filters(self):
        response = self.client.get(self.url, {'category': 'Tech'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Article 0')
        self.assertContains(response, 'Article 4')

        response = self.client.get(self.url, {'category': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Article 0')

    def test_article_list_view_all(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        for i in range(5):
            self.assertContains(response, f'Article {i}')

    def test_article_list_view_login_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


############## PASS ###############

class ArticleDetailViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(
            title='Sample Article', content='Content', category='Tech', author=self.user
        )
        self.url = reverse('article_detail', args=[self.article.id])

    def test_article_detail_view_status_code(self):
        # Ensure the article detail view returns a status code of 200 and uses the correct template
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/article_detail.html')

    def test_article_detail_view_content(self):
        # Ensure the article detail view contains the correct article information
        response = self.client.get(self.url)
        self.assertContains(response, 'Sample Article')
        self.assertContains(response, 'Content')
        self.assertContains(response, 'Tech')


############### PASS ######################

class AddArticleViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('add_article')

    def test_add_article_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/add_article.html')
        self.assertIsInstance(response.context['form'], ArticleForm)

    def test_add_article_view_post_valid(self):
        data = {
            'title': 'New Article',
            'content': 'Content of the new article',
            'category': 'Tech',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('article_list'))
        self.assertTrue(Article.objects.filter(title='New Article').exists())

    def test_add_article_view_post_invalid(self):
        data = {'title': ''}  # Invalid data: missing required fields
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/add_article.html')
        self.assertFalse(Article.objects.filter(title='').exists())


############## PASS ################

class MyArticlesViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        for i in range(5):
            Article.objects.create(
                title=f'Article {i}', content='Content', category='Tech', author=self.user
            )
        self.url = reverse('my_articles')

    def test_my_articles_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/my_articles.html')

    def test_my_articles_view_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Article 0')
        self.assertContains(response, 'Article 4')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')


################ PASS ##################

class EditArticleViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.another_user = User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.article = Article.objects.create(
            title='Original Title', content='Original Content', category='Tech', author=self.user
        )
        self.url = reverse('edit_article', args=[self.article.id])

    def test_edit_article_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/edit_article.html')
        self.assertIsInstance(response.context['form'], ArticleForm)

    def test_edit_article_view_post_valid(self):
        data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'category': 'Tech',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_articles'))
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Title')
        self.assertEqual(self.article.content, 'Updated Content')

    def test_edit_article_view_post_invalid(self):
        data = {'title': ''}  # Invalid data: missing required fields
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/edit_article.html')
        self.article.refresh_from_db()
        self.assertNotEqual(self.article.title, '')

    def test_edit_article_view_permission_denied(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_articles'))


################ PASS #####################

class DeleteArticleViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.article = Article.objects.create(
            title='Sample Article', content='Content', category='Tech', author=self.user
        )
        self.url = reverse('delete_article', args=[self.article.id])

    def test_delete_article_view_status_code(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_articles'))
        self.assertFalse(Article.objects.filter(id=self.article.id).exists())

    def test_delete_article_view_message(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('my_articles'))
        self.assertContains(response, 'Article deleted successfully.')

    def test_delete_article_view_login_required(self):
        self.client.logout()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')
