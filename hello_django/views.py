from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from hello_django.calc import views


def empty_path(self):
    return HttpResponseRedirect(reverse('calc', kwargs={'a': 40, 'b': 2}))

class IndexView(TemplateView):

    #template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'wevwev'
        return context
