from django.test import TestCase, Client
from chat.models import Message, Room


class TestChatModels(TestCase):

    def setUp(self):
        self.room = Room.objects.create(name='test_room')
        self.client = Client()
        self.message = Message.objects.create(value='test_message', room='test_room', user='test_user')

    def test_message_value(self):
        message = Message.objects.first()
        self.assertEqual(message.value, 'test_message')

    def test_room_name(self):
        room = Room.objects.first()
        self.assertEqual(room.name, 'test_room')

    def test_message_room(self):
        message = Message.objects.first()
        self.assertEqual(message.room, 'test_room')
        self.assertEqual(message.user, 'test_user')

