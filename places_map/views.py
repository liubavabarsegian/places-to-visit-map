from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def map(request):
    return render(request, 'djeym/djeym.html', {'section': 'djeym'})
