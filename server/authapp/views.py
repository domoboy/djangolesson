from django.shortcuts import render

from .forms import LoginForm

def login_view(request):
    form = LoginForm
    
    return render(
        request,
        'authapp/login.html',
        {
            'form': form
        }
    )
