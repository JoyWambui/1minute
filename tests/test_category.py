import unittest
from app.models import Category

class CategoryModelTest(unittest.TestCase):
    """Class that tests the Category Model."""
    
    def setUp(self):
        """Set Up Test that creates a new category instance"""
        self.new_category = Category(name="interview pitch")
        
    def test_category_variables(self):
        """Checks if the category variables are correctly placed."""
        self.assertEquals(self.new_category.name,"interview pitch")
       
       
    