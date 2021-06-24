from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact


def home_page(request):
    return render(request, 'contacts/index.html')


def all_contacts(request):
    contacts = Contact.objects.all()

    context = {
        "contacts": contacts
    }

    return render(request, 'contacts/all_contacts.html', context)


def save_contact(request):
    print(request.POST)
    # Create a new contact
    contact = Contact()
    # Rename request.POST to form
    form = request.POST

    # Assign contact attributes from form data
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


def search_contact(request):
    name = request.POST['first_name']
    if name:  # "Hector"
        contacts = Contact.objects.filter(first_name=name)
    else:
        contacts = ""

    context = {
        'contacts': contacts
    }

    return render(request, 'contacts/search_results.html', context)


def contact_details(request, contact_id):

    contact = Contact.objects.get(id=contact_id)

    context = {
        'contact': contact
    }

    return render(request, 'contacts/details.html', context)
