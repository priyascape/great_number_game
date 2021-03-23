from django.shortcuts import render
import random

# Create your views here.
from django.shortcuts import render,redirect, HttpResponse
from .models import *

def index(request):
    if 'computer_guess' not in request.session:
        request.session['computer_guess'] = random.randint(1,10)
        request.session ['too_low'] = False
        request.session ['too_high'] = False
        request.session ['just_right'] = False
    
    context = {
        'too_low':request.session ['too_low'],
        'too_high':request.session ['too_high'],
        'just_right':request.session ['just_right']
    }
    return render(request, 'index.html', context)


def guess(request):
    # Grab the guess from form
    request.session ['too_low'] = False
    request.session ['too_high'] = False
    request.session ['just_right'] = False
    
    if (int(request.POST['guess']) < request.session['computer_guess']):
        request.session['too_low'] = True
        
    elif (int(request.POST['guess']) > request.session['computer_guess']):
        request.session['too_high'] = True
    else:
        request.session['just_right'] = True
    # compare against computer guess
    
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
    


