from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

from .form import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from talko.models import Message


def index(request):
    return render(request,'talko/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'talko/registration.html',
                          {'user_form': user_form,
                           'registered': registered})


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/chat_view/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'talko/login.html', {})


@login_required
def chat_view(request):
    user = User.objects.all()
    logusr = request.user
    return render(request, 'talko/chat.html', {"users": user, 'loginuser': logusr})


@login_required
@csrf_exempt
def create_msg(request):
    if request.method == "POST":
        recver= User.objects.get(username='mhassan')
        msg = request.POST.get('msgtxt')
        c = Message(sender=request.user, reciever=recver, text=msg)
        if msg != '':
            c.save()
        return serialize({'msg': msg, 'sender': c.sender, 'reciever':recver})
    else:
        return HttpResponse('Request must be POST.')
