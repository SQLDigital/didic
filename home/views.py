from django.shortcuts import render
from django.http import HttpResponse
import random


from home.models import Register

# Create your views here.

def index(request):
    return render(request,'home.html')


def reg(request):
    return render(request,'reg.html')


def register(request):
    acct = random.randint(100000000000,999999999999)

    first_name  = request.POST['fname']
    last_name =  request.POST['lname']
    email = request.POST['email']
    phone =  request.POST['phone']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    zip = request.POST['zip']
    userId = request.POST['userid']
    password = request.POST['pswd']

    Save = Register()
    Save.first_name = first_name
    Save.last_name = last_name
    Save.email = email
    Save.phone = phone
    Save.street = address
    Save.city = city
    Save.state = state
    Save.country = country
    Save.zip = zip
    Save.account_No = acct
    Save.userid = userId
    Save.password = password
    Save.balance = "0.00"
    Save.routine = "BDOFOMRU"

    Save.save()

    return render(request, 'signin.html')
    