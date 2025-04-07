from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase


class BlogPostBoundaryTest(APITestCase):

    def test_boundary_cache_expiration(self):
        """Test if the cache expires after the defined time."""
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestCacheExpiration", True, "boundary")
        print("TestCacheExpiration = Passed")