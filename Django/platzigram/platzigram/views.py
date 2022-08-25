from django.http import HttpResponse
from datetime import datetime
import json

def saludo(request):
    now = datetime.now().strftime(f'%b %dth, %Y -%H:%M Hrs')
    return HttpResponse(f'la fecha es {now}')

def nums(request):
   numbers = [int(i) for i in request.GET['nums'].split(',')]
   orden = sorted(numbers)
   data= {
       'status': 'ok',
       'numbers': orden,
       'message': "integer sorted :)" 
   }
   return HttpResponse(json.dumps(data), content_type='application/json')

def saludar(request,name,age):
    if age < 18:
        message = f"{name}, eres Menor de edad"
    else:
        message = f"{name}, eres Mayor de edad"
    return HttpResponse(message)


