from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Contact

# Create your views here.
def home_page(request):
    return render(request, 'contacts/index.html')

def all_contacts(request):
    contacts = Contact.objects.all

    context = {
        "contacts": contacts
    }

    return render(request, 'contacts/all.html', context)

def save_contact(request):

    contact = Contact()

    form = request.POST

    contact.first_name = form['first_name']
    contact.last_name = form['last_name']
    contact.phone_number = form['phone_number']
    contact.email = form['email']
    contact.address = form['address']
    if form.get('is_cool') == 'on':
        contact.is_cool = True
    else:
        contact.is_cool = False

    contact.save()
    
    return HttpResponseRedirect(reverse('contacts:all_contacts'))