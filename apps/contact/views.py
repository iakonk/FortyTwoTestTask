from django.shortcuts import render_to_response
from django.http import Http404
from apps.contact.models import Contact


def contact(request):
    """
    :param request:
    :return: name, surname, date of birth, bio, contacts
    """
    try:
        contacts = Contact.objects.all()
    except ValueError:
        raise Http404()
    return render_to_response("contact.html", locals())
