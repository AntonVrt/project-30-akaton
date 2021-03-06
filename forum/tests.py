from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category, Author, Post, Comment


User = get_user_model()

class main_Test_Cases(TestCase):

   def test_Author(self):
      """tests for authors"""
      test_user = User.objects.create_user(username="user", email="email@mail.com", password="123456") #create a user
      self.assertEqual(Author.objects.all().count(), 0) #count authors in the db should be 0
      author1 = Author.objects.create(user=test_user, fullname="test1",slug="user1", bio="just for test") #create an author
      self.assertEqual(Author.objects.all().count(), 1) #count authors in the db should be 1
      author2 = Author.objects.create(user=test_user, fullname="test2",slug="user2", bio="just for test") #create an author
      self.assertEqual(Author.objects.all().count(), 2) #count authors in the db should be 2
      self.assertEqual(Author.objects.filter(fullname="test1").count(), 1) #count authors with the name test1 should be 1
      author1.delete() #delete the author
      self.assertEqual(Author.objects.filter(fullname="test1").count(), 0) #count authors with the name test1 should be 0
      self.assertEqual(Author.objects.all().count(), 1) #count authors in the db should be 0


   def test_Category(self):
      """ tests for categories"""
      self.assertEqual(Category.objects.all().count(), 0) #count categories in the db should be 0
      category1 = Category.objects.create(title="testcategory", slug="testcategory", description="just a test") #create a category
      self.assertEqual(Category.objects.all().count(), 1)#count categories in the db should be 1
      self.assertEqual(Category.objects.filter(title="testcategory").count(), 1)#count categories with the title testcatgory should be 1
      category2 = Category.objects.create(title="testcategory2", slug="testcategory2", description="just a test2") #create a category
      self.assertEqual(Category.objects.all().count(), 2) #count authors in the db should be 2
      category2.delete() #delete the category
      self.assertEqual(Category.objects.filter(title="testcategory2").count(), 0)#count categories with the title testcatgory2 should be 0
      self.assertEqual(Category.objects.all().count(), 1) #count authors in the db should be 0



   def test_Comment(self):
      """tests for comments"""
      test_user = User.objects.create_user(username="user", email="email@mail.com", password="123456") #create a user
      author1 = Author.objects.create(user=test_user, fullname="test1",slug="user1", bio="just for test") #create an author
      self.assertEqual(Comment.objects.all().count(), 0)#count comments in the db should be 0
      comment1 = Comment.objects.create(user=author1, content = "just a test") #create a comment
      self.assertEqual(Comment.objects.all().count(), 1)#count comments in the db should be 1
      self.assertEqual(Comment.objects.filter(content="just a test").count(), 1)#count comments with the content "just a test" should be 1
      comment2 = Comment.objects.create(user=author1, content = "just a test2") #create a comment
      self.assertEqual(Comment.objects.all().count(), 2)#count replies in the db should be 2
      comment1.delete() #delete the reply
      self.assertEqual(Comment.objects.all().count(), 1)  # count comments in the db should be 1
      self.assertEqual(Comment.objects.filter(content="just a test").count(),0)  # count comments with the content "just a test" should be 0

   def test_Post(self):
      """tests for posts"""
      test_user = User.objects.create_user(username="user", email="email@mail.com", password="123456")#create a user
      author1 = Author.objects.create(user=test_user, fullname="test1",slug="user1", bio="just for test") #create an author
      category1 = Category.objects.create(title="testcategory", slug="testcategory", description="just a test") #create an category
      self.assertEqual(Post.objects.all().count(), 0)#count posts in the db should be 0
      post1 = Post.objects.create(title="test post", slug="testpost", user=author1,
      content= "just post for a test", categories=category1, tags="test") #create a post
      self.assertEqual(Post.objects.all().count(), 1)#count posts in the db should be 1
      self.assertEqual(Post.objects.filter(title="test post").count(), 1)#count posts with the title "test post" should be 1
      post2 = Post.objects.create(title="test post2", slug="testpost2", user=author1,
      content="just post for a test2", categories=category1, tags="test")  # create a post
      self.assertEqual(Post.objects.all().count(), 2)#count posts in the db should be 2
      post2.delete() #delete the post
      self.assertEqual(Post.objects.all().count(), 1)#count posts in the db should be 1
      self.assertEqual(Post.objects.filter(title="test post2").count(), 0)#count posts with the title "test post" should be 0


