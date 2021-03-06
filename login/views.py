from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
# from django.core.context_processors import csrf
from django.template import RequestContext
import models
# Create your views here.

from Crypto.Hash import SHA256
from django.db import IntegrityError
from Crypto.Random.random import getrandbits

SECURITY = 9876

def permute(seed, salt):
    x = SHA256.new()
    for i in range(SECURITY):
        x.update(seed)
        seed = x.digest() + salt
    return x.hexdigest()

def create(request):
    v = request.POST
    if not v["password"] or not v["password_confirmation"] or not v["password"] == v["password_confirmation"]:
        return render(request, 'login/new.html', {'error_message': 'Passwords do not match'})
    if not len(v["password"]) > 5:
        return render(request, 'login/new.html', {'error_message': 'Password too short'})
    salty = hex(getrandbits(64))[2:-1]
    user = models.AppUser(email=v["email"],
        password=permute(v["password"].encode('utf-8'), salty), plan=0, salt=salty, name=v["name"])
    try:
        user.save()
    except IntegrityError:
        return render(request, 'login/new.html', {'error_message': 'Email and Username must be unique'})
    request.session["user"] = user.email
    request.session["isnew"] = user.name + ", you have successfully created your account"
    return redirect(reverse("login:view"))

def view(request):
    try:
        if not request.session["user"]:
            return redirect(reverse("login:new"))
        user = getUser(request.session["user"])
        if not user:
            return redirect(reverse("login:new"))
        if "isnew" in request.session:
            x = request.session.pop("isnew", None)
            return render_to_response('login/view.html',
                                          {'user': user, 'success_message': x},
                                          context_instance=RequestContext(request))
        return render_to_response('login/view.html',
                                      {'user': user},
                                      context_instance=RequestContext(request))
    except KeyError:
        return redirect(reverse("login:logout"))

def new(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login/new.html', c, RequestContext(request))

def signin(request):
    request.session.flush()
    c = {}
    c.update(csrf(request))
    return render_to_response('login/signin.html', c, RequestContext(request))

def validateSignIn(request):
    try:
        v = request.POST
        if not v["email"] or not v["password"]:
            return redirect(reverse("login:signin"))
        user = getUser(v["email"])
        if not getUser(v["email"]):
            return redirect(reverse("login:signin"))
        if not (user.password == permute(v["password"].encode('utf-8'), user.salt.encode('ascii'))):
            return redirect(reverse("login:signin"))
        request.session["user"] = user.email;
        return redirect(reverse("login:view"))
    except KeyError:
        return redirect(reverse("login:logout"))


def getUser(anemail):
    return models.AppUser.objects.get(email=anemail)

def logout(request):
    x = ''
    if 'logout_error' in request.session:
        x = request.session['logout_error']
    elif not 'user' in request.session:
        x = 'Please sign in'
    else:
        x = 'Please sign in'
    request.session.flush()
    return render(request, "login/signin.html", {'error_message': x})


