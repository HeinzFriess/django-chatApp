from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers

@login_required(login_url='/login/')

def index(request):
    """
    This view renders the chat HTML.
    """
    data = {'null':'null'}
    if request.method == 'POST':
        print("Received data" + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_Message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [new_Message, ])  
        #data = {'textmassage':request.POST['Textmassage'],'created_at':request.POST['created_at'],'author':request.POST['author']}
        return JsonResponse(serialized_obj[1:-1], safe=False) #[1.-1] erzeugt einen substring vom 2 zeichen (index1) bis zum vorletzten
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages' : chatMessages})
   

def loginView(request):
    """
    This view renders the logIn HTML.
    """
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'login.html', {'wrongPassword': True})

    return render(request, 'login.html', {'messages' : 'Hallo'})

def registerView(request):
    """
    This view renders the register HTML.
    """
    if request.method == 'POST':
        _password = request.POST.get('password')
        _passwordrepeat = request.POST.get('passwordrepeat')
        _firstname = request.POST.get('firstname_lastname').split()[0]
        _lastname = request.POST.get('firstname_lastname').split()[-1]
        if _password == _passwordrepeat:
            user = User.objects.create_user(username = request.POST.get('username'),
            email = None, password = _password, first_name = _firstname, last_name = _lastname)
            login(request, user)
            return HttpResponseRedirect('/chat/')
       
        else:
            return render(request, 'register.html', {'wrongPassword': True})
        
    return render(request, 'register.html')



