from django.shortcuts import render
from .models import Room
#from django.http import HttpResponse
# Create your views here.
#rooms = [
#    {'id':1, 'name':'Lets learn Python'},
#    {'id':2, 'name':'Lets learn SQL'},
#    {'id':3, 'name':'Lets learn R'},
#]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,"base/home.html", context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    #for i in rooms:
    #    if i['id'] == int(pk) :
    #        room = i
    context = {'room':room}

    return render(request, "base/room.html",context)

      