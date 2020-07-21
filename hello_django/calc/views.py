from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View

def calc_view(self, a, b):
    return HttpResponse('{} + {} = {}'.format(str(a), str(b), str(a + b)))

class CalcView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')
