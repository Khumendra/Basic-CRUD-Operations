from django.http import HttpResponse
from django.shortcuts import render
from .models import ProductData
from .forms import InsertingDataForm, UpdateDataForm, DeleteDataForm


def homeView(request):
    return render(request,'home.html')


def createView(request):
    if request.method == 'POST':
        iform = InsertingDataForm(request.POST)
        try:
            if iform.is_valid():
                product_id = request.POST.get('product_id')
                product_name = request.POST.get('product_name')
                product_cost = request.POST.get('product_cost')
                product_color = request.POST.get('product_color')
                product_class = request.POST.get('product_class')
                customer_name = request.POST.get('customer_name')
                customer_mobile = request.POST.get('customer_mobile')
                customer_email = request.POST.get('customer_email')
                data = ProductData(
                    product_id=product_id,
                    product_name=product_name,
                    product_cost=product_cost,
                    product_color=product_color,
                    product_class=product_class,
                    customer_name=customer_name,
                    customer_mobile=customer_mobile,
                    customer_email=customer_email
                )
                data.save()

                iform = InsertingDataForm()
                return render(request, 'create.html', {'iform': iform})
        except:
            return HttpResponse("IntegrityError!!! Data is Already Available🛑🤚🛑")

        else:
            return HttpResponse('Invalid Data')

    else:
        iform = InsertingDataForm()
        return render(request,'create.html',{'iform':iform})


def retrieveView(request):
    pdata = ProductData.objects.all()
    return render(request,'retrieve.html',{'pdata':pdata})


def updateView(request):
    if request.method == 'POST':
        uform = UpdateDataForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id')
            product_cost = request.POST.get('product_cost')
            product_id = ProductData.objects.filter(product_id=product_id)
            if not product_id:
                return HttpResponse('Invalid Product Id')
            else:
                product_id.update(product_cost= product_cost)
                uform = UpdateDataForm()
                return render(request,'update.html',{'uform':uform})
        else:
            msg = "🤚🚫 Please Fill The Form  "
            uform = UpdateDataForm()
            return render(request,'update.html',{'uform':uform,'msg':msg})
    else:
        uform = UpdateDataForm()
        return render(request,'update.html',{'uform':uform})


def deleteView(request):
    if request.method == 'POST':
        dform = DeleteDataForm(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id')
            product_id = ProductData.objects.filter(product_id=product_id)
            if not product_id:
                return HttpResponse('Invalid Product Id')
            else:
                product_id.delete()
                dform = DeleteDataForm
                return render(request,'delete.html',{'dform':dform})
        else:
            dform = DeleteDataForm()
            msg = "🤚🚫 Please Fill The Form  "
            return render(request,'delete.html',{'msg':msg,'dform':dform})

    else:
        dform = DeleteDataForm()
        return render(request,'delete.html',{'dform':dform})