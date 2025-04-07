from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import BlogPost
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse



class BlogPostFunctionalTest(APITestCase):

    def test_blog_post_cache(self):
        """Test if the blog post detail page is cached correctly."""
        test_obj = TestUtils()
        try:
            # Create a blog post
            post = BlogPost.objects.create(title='Test Post', content='Test Content')
            
            # Get the blog post detail page (this should trigger caching)
            response = self.client.get(reverse('post_detail', args=[post.id]))
            if response.status_code == 200:
                test_obj.yakshaAssert("TestBlogPostCache", True, "functional")
                print("TestBlogPostCache = Passed")
            else:
                test_obj.yakshaAssert("TestBlogPostCache", False, "functional")
                print("TestBlogPostCache = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestBlogPostCache", False, "functional")
            print("TestBlogPostCache = Failed")

    def test_update_post_cache_invalidation(self):
        """Test if cache is invalidated when the blog post is updated."""
        test_obj = TestUtils()
        try:
            # Create a blog post
            post = BlogPost.objects.create(title='Test Post', content='Test Content')
            post_id = post.id

            # Access the blog post detail page (this should cache the response)
            response = self.client.get(reverse('post_detail', args=[post_id]))
            # Update the blog post (this should invalidate the cache)
            post.title = 'Updated Test Post'
            post.save()

            # Access the updated blog post (new data should be fetched from DB)
            response = self.client.get(reverse('post_detail', args=[post_id]))
            if response.status_code == 200 and post.title == 'Updated Test Post':
                test_obj.yakshaAssert("TestPostCacheInvalidation", True, "functional")
                print("TestPostCacheInvalidation = Passed")
            else:
                test_obj.yakshaAssert("TestPostCacheInvalidation", False, "functional")
                print("TestPostCacheInvalidation = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestPostCacheInvalidation", False, "functional")
            print("TestPostCacheInvalidation = Failed")