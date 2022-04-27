from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Eat NO meat for the entire month!'
    elif month == 'february':
        challenge_text = 'Walk for at least 20 minutes per day.'
    elif month == 'march':
        challenge_text = 'Learn Django for at least 30 minutes per day.'
    else:
        return HttpResponseNotFound('This month is not supported!')
    return HttpResponse(challenge_text)
