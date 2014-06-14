from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import serial
from django.core.context_processors import csrf
from login.models import AppUser

# Arduino Library api
class HoverCraftDelegate(object):
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600)

    def receiveData(self):
        return self.ser.readline()

    def moveLeft(self):
        self.ser.write(b'2')

    def moveRight(self):
        self.ser.write(b'0')

    def moveForward(self):
        self.ser.write(b'1')

    def moveBackward(self):
        self.ser.write(b'3')

    def moveUp(self):
        self.ser.write(b'4')

delegate = None
try:
     delegate = HoverCraftDelegate('uuid')
except Exception:
    pass

def control(request):
    if not "user" in request.session or not AppUser.validate(request.session["user"]):
        return redirect(reverse("login:logout"))
    if (delegate == None):
        redirect(reverse("login:view"))
    try:
        return render(request, 'arduino/control.html',
                dict().update(csrf(request)))
    except OSError:
        redirect(reverse("login:view"))



# Create your views here.
def manage(request):
    try:
        if not AppUser.validate(request.session["user"]):
            return redirect(reverse("login:logout"))
        elif "left" in request.POST:
            delegate.moveLeft();
        elif "right" in request.POST:
            delegate.moveRight();
        elif "forward" in request.POST:
            delegate.moveForward();
        elif "backward" in request.POST:
            delegate.moveBackward();
        elif "up" in request.POST:
            delegate.moveUp();
        return redirect("robot:control")

    except Exception:
        return redirect(reverse("login:logout"))