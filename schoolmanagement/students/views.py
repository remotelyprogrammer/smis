from django.shortcuts import render


def blank(requests):
    return render(requests, 'students/blank.html')