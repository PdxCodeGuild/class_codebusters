from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact


def home_page(request):
    return render(request, 'contacts/index.html')


def all_contacts(request):
    cool_contacts = Contact.objects.filter(is_cool=True).order_by('first_name')

    not_cool_contacts = Contact.objects.filter(
        is_cool=False).order_by('first_name')

    context = {
        'cool_contacts': cool_contacts,
        'not_cool_contacts': not_cool_contacts
    }
    return render(request, 'contacts/all_contacts.html', context)


def save_contact(request):
    # create a new contact
    contact = Contact()
    # rename request.POST to form
    form = request.POST

    # assign contact attributes from form data
    contact.first_name = form['first_name'].title()
    contact.last_name = form['last_name'].title()
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
    if name:
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
