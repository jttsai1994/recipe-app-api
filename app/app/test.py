from django.test import TestCase

from app.cal import add

class CalTests(TestCase): #inherit from testCase

    def test_add_numbers(self):
        """Test that two numbers are add together"""
        self.assertEqual(add(3,8),11)