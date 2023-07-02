from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import os

from .models import User, abt_description, abt_carousel, writings, paints
# Create your views here.

def index(request):

    #Variables that will be necesary for the webpage
    all_writings = writings.objects.all()
    carousel_items = abt_carousel.objects.all()
    about_me = abt_description.objects.get(name = "description")
    drawings = paints.objects.all()

    return render(request, "index.html", {
        'writings': all_writings,
        'carousel_items': carousel_items,
        'about_me': about_me,
        'paints': drawings
    })

@login_required(login_url='login')
def dashboard(request):
    all_writings = writings.objects.all().order_by("-id")
    carousel_items = abt_carousel.objects.all().order_by("-id")
    about_me = abt_description.objects.get(name = "description")
    drawings = paints.objects.all().order_by("-id")

    return render(request, "dashboard.html", {
        'writings': all_writings,
        'carousel_items': carousel_items,
        'about_me': about_me,
        'paints': drawings
    })

def add_carousel(request):
    if request.method == 'POST':
        owner = request.POST['owner']
        quote = request.POST['text']
        num = len(abt_carousel.objects.all()) + 1

        newQuote = abt_carousel(
            owner =owner,
            text=quote,
            num=num
        )
        newQuote.save()

        return HttpResponseRedirect(reverse("Dashboard"))
    else: 
        return HttpResponseRedirect(reverse("Dashboard"))
    
def add_description(request): 
    if request.method == "POST":
        #Delete the existent description
        existing_description = abt_description.objects.get(name="description")
        existing_description.delete()
        #Create a new description
        text = request.POST['text']
        new_description = abt_description(
            text=text
        )
        new_description.save()
        return HttpResponseRedirect(reverse('Dashboard'))
    else: 
        return HttpResponseRedirect(reverse('Dashboard'))
    
def add_paint(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES['paint_img_new']

        new_paint = paints(
            name=name,
            paint_img=img
        )
        new_paint.save()
        return HttpResponseRedirect(reverse('Dashboard'))
    else: 
        return HttpResponseRedirect(reverse('Dashboard'))

def add_writing(request):
    if request.method == 'POST':
        text = request.POST['text']
        name = request.POST['name']

        new_writing = writings(
            name=name,
            text=text
        )
        new_writing.save()
        return HttpResponseRedirect(reverse('Dashboard'))
    else: 
        return HttpResponseRedirect(reverse('Dashboard'))
    
def delete_button(request, identifier, id):
    match identifier:
        case "quotes":
            quote_to_delete = abt_carousel.objects.get(pk=id)
            quote_to_delete.delete()
            return HttpResponseRedirect(reverse('Dashboard'))
        case "paint":
            paint_to_delete = paints.objects.get(pk=id)
            paint_to_delete.delete()
            os.remove(paint_to_delete.paint_img.path)
            return HttpResponseRedirect(reverse('Dashboard'))
        case "writing":
            writing_to_delete = writings.objects.get(pk=id)
            writing_to_delete.delete()
            return HttpResponseRedirect(reverse('Dashboard'))
        
def edit_button(request, identifier, id):
    if request.method == 'POST':
        match identifier:
            case "carousel":
                carousel = abt_carousel.objects.get(pk=id)
                new_owner = request.POST['new_carousel_owner']
                new_text = request.POST['new_carousel_text']

                carousel.owner = new_owner
                carousel.text = new_text
                carousel.save()
                return HttpResponseRedirect(reverse('Dashboard'))
            
            case "description":
                description = abt_description.objects.get(pk=id)
                new_description = request.POST['new_description']
                description.text = new_description
                description.save()
                return HttpResponseRedirect(reverse('Dashboard'))
            
            case "writing":
                writing = writings.objects.get(pk=id)
                new_writing = request.POST['new_writing'] 
                writing.text = new_writing
                writing.save()
                return HttpResponseRedirect(reverse('Dashboard'))

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("Dashboard"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "login.html")