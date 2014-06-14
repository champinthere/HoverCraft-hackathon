import views
from django import template

register = template.Library()

def verify(anemail):
    try:
        user = views.getUser(anemail)
        return (user != None)
    except Exception:
        return False

register.filter('verify', verify)
