from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.http import HttpResponse

import json

class CSRFExempt(object):
    @method_decorator(csrf_exempt)
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)

def render_to_response(data,status):
    return HttpResponse(data,content_type="application/json",status=status)

def is_json(data):
    try:
        real_json=json.loads(data)
        is_valid =True
    except ValueError:
        is_valid=False
    return is_valid
