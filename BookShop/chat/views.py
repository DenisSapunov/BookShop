
from django.shortcuts import render, redirect
from chat.models import Room, Message, NotAuthUsersMessage
from django.http import HttpResponse, JsonResponse


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def create_not_auth_user_message(request):
    NotAuthUsersMessage.objects.create(value=request.POST['value'], email=request.POST['email'])
    return redirect('chat:')


def just_message(request):
    return render(request, 'chat/just_message.html')

def home(request):
    return render(request, 'chat/home.html')

def checkview(request):
    if request.user.is_authenticated:
        room = request.user.username
        username = request.user.username
        if Room.objects.filter(name=room).exists():
            return redirect(room + '/?username=' + username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect(room + '/?username=' + username)
    else:
        return home(request)

def send(request):
    message = request.POST['message']
    if message:
        username = request.user.username
        room_id = request.POST['room_id']

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse('Message sent successfully')
    else:
        return HttpResponse('')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
