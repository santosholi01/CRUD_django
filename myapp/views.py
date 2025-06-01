from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from .models import student
from .form import addmodel
# Create your views here.
class home(View):
    def get(self, request):
        stu=student.objects.all()
        return render(request, "home.html",{'model':stu})

class add(View):
    def get(self, request):
       fm=addmodel()
       return render(request, "add.html",{'form':fm})
    
    def post(self, request):
        fm=addmodel(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
          return render(request, "add.html",{'form':fm})

class delete(View):
    def post(self, request):
        data=request.POST.get('id')
        dat=student.objects.get(id=data)
        dat.delete()
        return redirect('/')
    
class edit(View):
    def get(self, request, id):
        dat=student.objects.get(id=id)
        fm=addmodel(instance=dat)
        return render(request, "edit.html",{'add':fm})
    
    def post(self, request, id):
        dat=student.objects.get(id=id)
        fm=addmodel(request.POST, instance=dat)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return HttpResponse("bad")

        
