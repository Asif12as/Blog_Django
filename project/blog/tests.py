from django.test import TestCase
from .models import Post, Comment
from django.contrib.auth import get_user_model


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        testuser = User.objects.create_user(username="testuser",password="12345")
        Post.objects.create(author = testuser,  title ="Test Post", content="This is test post content.")

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post.author), "testuser")
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "this is a test post content.")

    def test_comment_content(self):
        post = Post.objects.get(id=1)
        Comment.onjects.create(post =post, author=post.author, content= "test comment content.")
        comment= Comment.objects.get(id=1)
        self.assertEquall(str(comment,author), "testuser")
        self.assertEqual(comment.content,"test comment content")
        

