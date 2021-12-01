from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create(username='tester', password='test123')
        test_post = Post.objects.create(category_id=1, title='Test Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'tester')
        self.assertEqual(title, 'Test Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(cat.name, 'django')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(str(post), 'Test Post Title')
        self.assertEqual(str(cat), 'django')
