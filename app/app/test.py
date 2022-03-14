from django.test import TestCase

from app.cal import add,subtract

class CalTests(TestCase): #inherit from testCase

    def test_add_numbers(self):
        """Test that two numbers are add together"""
        self.assertEqual(add(3,8),11)

    def test_subtract_numbers(self):  #test function should start with test
        self.assertEqual(subtract(5,11),6)