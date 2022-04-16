from os import stat
from pydoc import resolve
from re import L
from urllib import request
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse 

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='saugat', password='saugat')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name='netflix', about='#platform', website='https//:www.netflix.com')

    def test_streamplatform_create(self):
        data =  {
            'name': 'netflix',
            'about': '#1 stream platform',
            'website': 'https://netflix.com'
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatfrom_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))


class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='saugat', password='saugat')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name='netflix', about='#platform', website='https//:www.netflix.com')
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title='example movie', storyline='example storyline', active=True)

    def test_watchlist_create(self):
        data = {
            'platform': self.stream,
            'title': 'example movie',
            'storyline': 'example story',
            'active': True
        }  
        response = self.client.post(reverse('movie_list'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie_detail', args=[self.watchlist.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

