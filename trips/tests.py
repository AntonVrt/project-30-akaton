from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Trip, Review, Tag
from users.models import Profile

User = get_user_model()

class main_Test_Cases(TestCase):

   def test_Trip(self):
      """tests for trips"""
      test_user = User.objects.create_user(username="user", email="email@mail.com", password="123456") #create a user
      self.assertEqual(Trip.objects.all().count(), 0) #count Trips in the db should be 0
      profile1 = Profile.objects.create(user=test_user, name="test1", email="email@mail.com", username="test_user", location="here", short_intro="hi", bio="test profile") #create a Profile
      tag1= Tag.objects.create(name="tag1")
      trip1 = Trip.objects.create(owner=profile1, title="test1", description="test1", vote_total=1, vote_ration=100)#create a trip
      trip1.tags.add(tag1)#add a tag to the trip
      trip1.save() #save the trip with the new tag
      self.assertEqual(Trip.objects.all().count(), 1) #count trips in the db should be 1
      trip2 = Trip.objects.create(owner=profile1, title="test2", description="test2", vote_total=1, vote_ration=100)#create a trip
      trip2.tags.add(tag1)#add a tag to the trip
      trip2.save() #save the trip with the new tag
      self.assertEqual(Trip.objects.all().count(), 2) #count trips in the db should be 2
      self.assertEqual(Trip.objects.filter(title="test1").count(), 1) #count trips with the name test1 should be 1
      trip1.delete() #delete the profiles
      self.assertEqual(Trip.objects.filter(title="test1").count(), 0) #count trips with the name test1 should be 0
      self.assertEqual(Trip.objects.all().count(), 1) #count trips in the db should be 0



   def test_Review(self):
      """tests for Reviews"""
      test_user = User.objects.create_user(username="user", email="email@mail.com", password="123456") #create a user
      test_user2 = User.objects.create_user(username="user2", email="email@mail.com", password="123456") #create a user
      self.assertEqual(Review.objects.all().count(), 0) #count Reviews in the db should be 0
      profile1 = Profile.objects.create(user=test_user, name="test1", email="email@mail.com", username="test_user", location="here", short_intro="hi", bio="test profile") #create a Profile
      profile2 = Profile.objects.create(user=test_user2, name="test2", email="email@mail.com", username="test_user2", location="here", short_intro="hi", bio="test profile2") #create a Profile
      tag1= Tag.objects.create(name="tag1")
      trip1 = Trip.objects.create(owner=profile1, title="test1", description="test1", vote_total=1, vote_ration=100)#create a trip
      trip1.tags.add(tag1)#add a tag to the trip
      trip1.save() #save the post with the new tag
      VOTE_TYPE = (
         ('up', 'Up Vote'),
         ('down', 'Down Vote'),
      )
      review1 = Review.objects.create(owner=profile1, trip=trip1, body="test1",value=VOTE_TYPE )
      self.assertEqual(Review.objects.all().count(), 1) #count Reviews in the db should be 1
      review2 = Review.objects.create(owner=profile2, trip=trip1, body="test2", value=VOTE_TYPE )
      self.assertEqual(Review.objects.all().count(), 2) #count Reviews in the db should be 2
      self.assertEqual(Review.objects.filter(body="test1").count(), 1) #count Reviews with the name test1 should be 1
      review1.delete() #delete the profiles
      self.assertEqual(Review.objects.filter(body="test1").count(), 0) #count Reviews with the name test1 should be 0
      self.assertEqual(Review.objects.all().count(), 1) #count Reviews in the db should be 0

   def test_Tags(self):
      self.assertEqual(Tag.objects.all().count(), 0) #count tags in the db should be 0
      tag1 = Tag.objects.create(name="tag1")
      self.assertEqual(Tag.objects.all().count(), 1) #count tags in the db should be 1
      tag2 = Tag.objects.create(name="tag2")
      self.assertEqual(Tag.objects.filter(name="tag1").count(), 1) #count tags with the name tag1 should be 1
      self.assertEqual(Tag.objects.all().count(), 2) #count tags in the db should be 2
      tag1.delete() #delete the profiles
      self.assertEqual(Tag.objects.filter(name="tag1").count(), 0) #count Reviews with the name test1 should be 0
      self.assertEqual(Tag.objects.all().count(), 1) #count Reviews in the db should be 0



