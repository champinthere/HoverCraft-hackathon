from django.shortcuts import render
import serial

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


# Create your views here.
