from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html', {'section': 'dashboard'})
        # redirect('dashboard')
# Create your views here.

