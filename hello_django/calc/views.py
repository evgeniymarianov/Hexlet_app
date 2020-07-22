from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View
from hello_django.calc.models import History


def index(request):
    return HttpResponse('calc')

def history(request):
    last_values = History.objects.all().order_by('timestamp')[:10]
    return render(request, 'calc/history.html', {'last_values': last_values})

def calc_view(request, a, b):
    #return HttpResponse('{} + {} = {}'.format(str(a), str(b), str(sum)))
    print(request)
    if request.method == 'GET':
        sum = a + b
        History(value=sum).save()
        context = {'a': a, 'b': b, 'sum': sum}
        return render(request, 'calc/calc.html', context = context)

class CalcView(View):

    def get(self, request, *args, **kwargs):
        print(request)
        return HttpResponse('calc')
