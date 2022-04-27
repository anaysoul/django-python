from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

monthly_challenges = {
    'january': 'Eat NO meat for the entire month!',
    'february': 'Walk for at least 20 minutes per day.',
    'march': 'Learn Django for at least 30 minutes per day.',
    'april': 'Learn React for at least an hour each day.',
    'may': 'Eat NO meat for the entire month!',
    'june': 'Walk for at least 20 minutes per day.',
    'july': 'Learn Django for at least 30 minutes per day.',
    'august': 'Learn React for at least an hour each day.',
    'september': 'Eat NO meat for the entire month!',
    'october': 'Walk for at least 20 minutes per day.',
    'november': 'Learn Django for at least 30 minutes per day.',
    'december': 'Learn React for at least an hour each day.'
}


# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')
