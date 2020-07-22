from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View
from django.template import Context, Template

def index(request):
    return HttpResponse('calc')

def calc_view(request, a, b):
    #return HttpResponse('{} + {} = {}'.format(str(a), str(b), str(sum)))
    print(request)
    if request.method == 'GET':
        sum = a + b
        context = {'a': a, 'b': b, 'sum': sum}
        return render(request, 'calc/calc.html', context = context)

class CalcView(View):

    def get(self, request, *args, **kwargs):
        print(request)
        return HttpResponse('calc')
