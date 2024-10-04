from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *
def stock(request):
    templates = loader.get_template('shop.html')
    return HttpResponse(templates.render())

def add(request):
    if request.method=='POST':
        CreatedAt=request.POST['CreatedAt']
        Name=request.POST['Name']
        Weight=request.POST['Weight']
        Price=request.POST['Price']
        sales(CreatedAt = CreatedAt, Name=Name,
            Weight=Weight,
            Price=Price).save()
        return redirect('add')

    data = sales.objects.all()
    return render(request, 'shop.html', {'data': data})

def update(request,id):
    dataget = sales.objects.get(id = id)
    data = sales.objects.all()
    if request.method == "POST":
        CreatedAt = request.POST['CreatedAt']
        Name = request.POST['Name']
        Weight = request.POST['Weight']
        Price = request.POST['Price']
        dataget.CreatedAt = CreatedAt
        dataget.Name = Name
        dataget.Weight = Weight
        dataget.Price = Price
        dataget.save()
        return redirect('add')
    return render(request,'shop.html',{'dataget':dataget,'data':data})

def delete(request,id):
    dataget = sales.objects.get(id=id)
    dataget.delete()
    return redirect('add')