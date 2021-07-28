from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact

def home_page(request):
    return render(request,'contacts/index.html')

def all_contacts(request):
    cool_contacts = Contact.objects.filter(is_cool=True).order_by('first_name')
    not_cool_contacts = Contact.objects.filter(is_cool=False).order_by('first_name')
    


    context = {
        'cool_contacts': cool_contacts,
        'not_cool_contacts': not_cool_contacts
    }
    return render(request,'contacts/all_contacts.html', context)

def save_contact(request):
    contact = Contact()
    form = request.POST
    contact.first_name = form['first_name'].title()
    contact.last_name = form['last_name'].title()
    contact.email = form['email']
    if form.get('is_cool') == 'on':
        contact.is_cool = True
    else:
        contact.is_cool = False
    
    contact.save()
    return redirect('../all/')

def search_contact(request):
    name = request.POST['first_name'].title()
    contacts = Contact.objects.filter(first_name=name)
    context = {
        'contacts' : contacts
    }
    return render(request,'contacts/search_results.html', context)

def contact_detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {
        'contact': contact
    }
    return render(request,'contacts/details.html', context)