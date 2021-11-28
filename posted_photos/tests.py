from django.test import TestCase
from .models import Category, Location, Image

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='Food')
        self.category.save_category()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(location_name = 'Rongai')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)
    
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(location_name = 'Rongai')
        self.location.save_location()

        self.category = Category(category_name = 'Food')
        self.category.save_category()

        self.image_test = Image(id=1, name='Burger', description='Grab the tastiest of burgers', 
                               location=self.location, category = self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))
 
    def test_save_image(self):
        self.image_test.save_image()
        follow = Image.objects.all()
        self.assertTrue(len(follow) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'images/image1.jpg')
        changed_image = Image.objects.filter(image='images/image1.jpg')
        self.assertTrue(len(changed_image) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()