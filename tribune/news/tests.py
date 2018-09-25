from django.test import TestCase
from . models import Editor,Article,tags

# Create your tests here.

class EditorTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.gabriel = Editor(first_name = 'gabriel', last_name = 'nwachukwu', email = 'gabrielcoder247@gmail.com')

    # Test instance    
    def test_instance(self):
        self.assertTrue(isinstance(self.gabriel,Editor))

    def test_save_method(self):
        self.gabriel.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)



class ArticleTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.new_article = Article( 
        title = 'arm robber caught in abuja',
        editor_id = 4,
        post = 'five armed men were caught last night with sophisticated weapons',
        pub_date = 2018-10-25)

    # Test instance    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_save_method(self):
        self.new_article.save_article()
        articles = Article.objects.all()
        self.assertTrue(len(articles) > 0)        

