from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Guests
from django.template import loader
import traceback

# Create your views here.




def home(request):

    if request.user.is_authenticated:
        return redirect("invitado/")
    
    if request.method == "POST":
        codes = request.POST.get("code").lower()
        template = loader.get_template('index.html')
        try:
            guest = Guests.objects.filter(code=codes).values()
            if guest.exists():
                user = User.objects.get(username='guests')
                login(request, user)
                return redirect("invitado/?code=" + codes, {"data": guest})
            else:
                print("no existe")
                context = {
                    'error': 'Lo siento No estas invitado :(',
                }
                return HttpResponse(template.render(context, request))
        except Exception as e:
            return redirect("home")
    return render(request, 'index.html')


#@login_required(login_url='home')
def Guest(request):
    
    try:
        codes = request.GET.get("code").lower()
        guest = Guests.objects.filter(code=codes).values()
        if guest.exists():
            return render(request, 'invitation.html', {"data": guest})
        else:
            logout(request)
            return redirect("home")
    except:
        logout(request)
        return redirect("home")
    
