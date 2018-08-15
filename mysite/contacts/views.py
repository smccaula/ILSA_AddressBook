# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

from contacts.models import Contact

class ListContactView(ListView):

    model = Contact
    template_name = 'list_contact.html'

class CreateContactView(CreateView):

    model = Contact
    fields = ['first_name','last_name','phone','email','street_address']
    template_name = 'add_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')

        return context

class UpdateContactView(UpdateView):

    model = Contact
    fields = ['first_name','last_name','phone','email','street_address']
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):

    model = Contact
    template_name = 'contact.html'


