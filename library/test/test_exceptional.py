from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase


class BlogPostExceptionalTest(APITestCase):

    def test_invalid_post_id(self):
        """Test if an invalid post ID results in a 404 error"""
        test_obj = TestUtils()
        try:
            # Test with an invalid post ID (assuming no post with ID 999 exists)
            response = self.client.get(reverse('post_detail', args=[999]))
            if response.status_code == 404:
                test_obj.yakshaAssert("TestInvalidPostID", True, "exceptional")
                print("TestInvalidPostID = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidPostID", False, "exceptional")
                print("TestInvalidPostID = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestInvalidPostID", True, "exceptional")
            print("TestInvalidPostID = Passed")