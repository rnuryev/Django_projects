from django.shortcuts import render, redirect
from .models import NewsUser
import random

# Create your views here.

def newsletter_subscribe(request):

    if request.method == 'POST':
        user_email = request.POST.get('email')

        if NewsUser.objects.filter(email=user_email).exists():
            user = NewsUser.objects.get(email=user_email)
            if not user.is_active:
                user.is_active = True
                user.save()

        else:
            new_user = NewsUser()
            new_user.email = user_email
            new_user.user_hash = ''.join([random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(25)])
            new_user.save()

    return redirect(request.META['HTTP_REFERER'] + '#subcribe-form')

def newsletter_unsubscribe(request, user_hash):
    user = NewsUser.objects.get(user_hash=user_hash)
    user.is_active = False
    user.save()

    return render(request, 'newsletter/unsubscribe.html')