from django.shortcuts import render

def sign_up(request):
    return render(request, 'sign_up/sign_up.html')

def sign_in(request):
    return render(request, 'sign_in/sign_in.html')
