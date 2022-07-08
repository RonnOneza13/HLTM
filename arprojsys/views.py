from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm, PayForm

installed_apps = ['arprojsys']

def Mainpage(request):
	return render(request, 'model_CustomerInfo.html')


def Payment(request):
	if request.method == "POST":
		lname = request.POST['lname']
		fname = request.POST['fname']
		address= request.POST['address']
		number = request.POST['number']
		food= request.POST['food']
		prqua = request.POST['prqua']
		data = HealthyContact.objects.create(LName = lname, Fname = fname, PAddress = address, Pnumber = number, Food = food, Order = prqua)
		data.save()
	return render(request, 'model_Payment.html')

def Summary(request):
	if request.method == "POST":
		datetoday = request.POST['datetoday']
		deliverydate = request.POST['deliverydate']
		pay = request.POST['pay']
		datas = ModPayDate.objects.create(DToday = datetoday,DelToday = deliverydate, Mop = pay)
		datas.save()
	aHealthyContact = HealthyContact.objects.all()
	aModPayDate = ModPayDate.objects.all()
	return render(request, 'SummaryTable.html', {'HealthyContact':aHealthyContact,'ModPayDate':aModPayDate})

def edit(request, id):
	cont = HealthyContact.objects.get(id=id)
	form = ContactForm(instance=cont)
	if request.method == 'POST':
		form = ContactForm(request.POST, instance = cont)
		if form.is_valid():
			form.save()
			return redirect('/Summary')

	return render(request, 'edit.html', {'form':form})
		
def delete(request, id):
    y = HealthyContact.objects.get(id=id)
    for x in HealthyContact.objects.only('id'):
        if y == x:
            x = HealthyContact.objects.get(id=id).delete()
            break
    return redirect('/Summary')

def pedit(request, id):
	pay = ModPayDate.objects.get(id=id)
	form = PayForm(instance=pay)
	if request.method == 'POST':
		form = PayForm(request.POST, instance = pay)
		if form.is_valid():
			form.save()
			return redirect('/Summary')

	return render(request, 'pedit.html', {'form':form})
		
def pdelete(request, id):
    z = ModPayDate.objects.get(id=id)
    for x in ModPayDate.objects.only('id'):
        if z == x:
            x = ModPayDate.objects.get(id=id).delete()
            break
    return redirect('/Summary')