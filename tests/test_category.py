import unittest
from app.models import Category
from app import db

class CategoryModelTest(unittest.TestCase):
    """Class that tests the Category Model."""
    
    def setUp(self):
        """Set Up Test that creates a new category instance"""
        self.new_category = Category(name="interview pitch")
        
    def tearDown(self):
        """Deletes all user and pitch elements from the database after every test."""
        Category.query.delete()
        db.session.commit()
    
        
    def test_category_variables(self):
        """Checks if the category variables are correctly placed."""
        self.assertEquals(self.new_category.name,"interview pitch")
    
    def test_save_category(self):
        """Checks if a category is being saved."""
        self.new_category.save_category()
        self.assertTrue(len(Category.query.all())>0)
   
    
    def test_get_categories(self):
        """Checks if all categories are returned."""
        category_two=Category(name="product pitch")
        category_three=Category(name="story pitch")
        category_four=Category(name="Shoot your Shot")
        category_five=Category(name="app pitch")
        category_six=Category(name="election pitch")
        self.new_category.save_category()
        category_two.save_category()
        category_three.save_category()
        category_four.save_category()
        category_five.save_category()
        category_six.save_category()
        got_categories = Category.get_categories()
        self.assertTrue(len(got_categories) == 6)
   
    