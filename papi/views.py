from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
from .mixins import CSRFExempt,render_to_response,is_json
from .models import StuData
from .forms import StuForm
import json

# Create your views here.
def sample(request):
    data={"Hello There":"Wassup "}
    return JsonResponse(data)

class StuDataDetail(View):
    def get(self,request,id,*args,**kwargs):
        obj=StuData.objects.get(id=id)
        json_data=obj.serialize()
        #data=serialize("json",[obj,])
        #return HttpResponse(json_data,content_type="application/json",status=200)
        return render_to_response(data=json_data,status=200)


class StuDataList(View):
    def get(self,request,*args,**kwargs):
        #obj=StuData.objects.all()
        obj=StuData.objects.order_by('-id')#descending id's
        json_data=obj.serialize()
        #data=serialize("json",[obj,])
        #return HttpResponse(json_data,content_type="application/json",status=200)
        return render_to_response(data=json_data,status=200)


class StuDataPost(CSRFExempt,View):
    def post(self,request,*args,**kwargs):
        form=StuForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=True)
            #obj_data=obj.serialize()
            #print(obj_data)
            data={"message":"Succesfull"}
            #return HttpResponse(json.dumps(data),content_type="application/json",status=200)
            return render_to_response(data=json.dumps(data),status=200)

        if form.errors:
            data={"message":"did not work properly!"}
            #return HttpResponse(json.dumps(data),content_type="application/json",status=402)
            return render_to_response(data=json.dumps(data),status=200)


class StuDataDelete(CSRFExempt,View):
    def get_object(self,id):
        qs=StuData.objects.filter(id=id)
        if qs.count()>0:
            return qs.first()
        return None

    def delete(self,request,id,*args,**kwargs):
        obj=self.get_object(id)
        if obj is None:
            err_data=json.dumps({"message":"No Such ID"})
            return render_to_response(err_data,status=404)

        obj.delete()
        return render_to_response(json.dumps({"message":f"{id} deleted successfully"}),status=200)

class StuDataUpdate(CSRFExempt,View):
    def get_object(self,id):
        qs=StuData.objects.filter(id=id)
        if qs.count()>0:
            return qs.first()
        return None

    def put(self,request,id,*args,**kwargs):
        obj=self.get_object(id)
        if obj is None:
            err_data=json.dumps({"message":"No Such ID"})
            return render_to_response(err_data,status=404)
        data=json.loads(obj.serialize())
        passed_data=json.loads(request.body)
        print(passed_data)
        for key,value in passed_data.items():
            data[key]=value
        form=StuForm(data,instance=obj)
        if form.is_valid():
            obj=form.save(commit=True)
            obj_data=obj.serialize()
            return render_to_response(obj_data,status=200)
        if form.errors:
            data=json.dumps(form.errors)
            return render_to_response(data,status=404)
