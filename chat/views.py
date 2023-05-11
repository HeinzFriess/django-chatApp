from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login/')

def index(request):
    if request.method == 'POST':
        print("Received data" + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages' : chatMessages})

def loginView(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'login.html', {'wrongPassword': True})

    return render(request, 'login.html', {'messages' : 'Hallo'})

def registerView(request):
    if request.method == 'POST':
        _password = request.POST.get('password')
        _passwordrepeat = request.POST.get('passwordrepeat')
        print(_password)
        print(_passwordrepeat)
        if _password == _passwordrepeat:
            user = User.objects.create_user(username = request.POST.get('username'), email = None, password = _password)
            login(request, user)
            return HttpResponseRedirect('/chat/')
       
        else:
            return render(request, 'register.html', {'wrongPassword': True})
        
    return render(request, 'register.html', {'messages' : 'Hallo'})



