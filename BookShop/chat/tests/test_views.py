from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from chat.models import Room, Message


class TestChatView(TestCase):

    def setUp(self):
        self.client = Client()
        self.room = Room.objects.create(name="test_room")
        self.client.force_login(user=User.objects.create(username='test_user_name', password='3333333'), backend=None)

    def test_checkview_GET(self):
        response = self.client.get(reverse('chat:checkview'))
        self.assertEqual(response.status_code, 302)

    def test_room_GET(self):
        response = self.client.get(reverse('chat:room', args=['test_room']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/room.html')

    def test_send_POST(self):
        message = Message.objects.create(value='test', room='test_room')
        response = self.client.post('/chat/send/', data={'message':message, 'room_id':1})
        self.assertEqual(response.status_code, 200)

    def test_getMessages_GET(self):
        response = self.client.get(reverse('chat:getMessages', args=['test_room']))
        self.assertEqual(response.status_code, 200)

