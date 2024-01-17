from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(requests):
    context = {
        'page_heading':'Hello'

    }
    return render(requests, 'webutil/sample2.html', context)
