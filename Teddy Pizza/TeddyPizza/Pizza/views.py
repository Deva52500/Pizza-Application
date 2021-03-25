from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Pizza, IngredientList
from django.db import connection

# Create your views here.


def loginPage(request):
    return render(request, 'pizza/login.html')


def verifyLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = authenticate(request, username=username, password=password)

        if admin is not None:
            login(request, admin)
            return redirect('/displayOrder')
        else:
            messages.info(request, 'Enter Valid Credentials.')
    context = {}
    return render(request, 'pizza/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/loginPage')

def home(request):
    orders = IngredientList.objects.values('ingredient_name')

    return render(request, 'pizza/home.html', {'orders': orders})

def placeOrder(request):
    if request.method == "POST":
        c_name = request.POST.get('customer_name')
        i_name = request.POST.get('ingredient_name')
        price = request.POST.get('price')

        order = Pizza(pizza_name=i_name, price=price, CustomerName=c_name)
        order.save()
        return render(request, 'pizza/home.html')

@login_required(login_url='/loginPage')
def displayOrder(request):

    orders = Pizza.objects.all()

    return render(request, 'pizza/baker.html', {'orders': orders})

@login_required(login_url='/loginPage')
def deleteOrder(request, cid):
    order = Pizza.objects.get(id=cid)
    order.delete()
    return render(request, 'pizza/baker.html')

@login_required(login_url='/loginPage')
def displayIngredient(request):
    ingredients = IngredientList.objects.all()

    return render(request, 'pizza/displayIngredient.html', {'ingredients': ingredients})

@login_required(login_url='/loginPage')
def adding_ingredient(request):
    return render(request, 'pizza/ingredient.html')

@login_required(login_url='/loginPage')
def addIngredient(request):
    if request.method == "POST":
        if request.POST.get('ingredient_name') and request.POST.get('supplier_name'):
            ingresave = IngredientList()
            ingresave.ingredient_name = request.POST.get('ingredient_name')
            ingresave.supplier_name = request.POST.get('supplier_name')
            cursor = connection.cursor()
            cursor.execute("call addIngredient('"+ingresave.ingredient_name+"', '"+ingresave.supplier_name+"')")
            return render(request, 'pizza/ingredient.html')

@login_required(login_url='/loginPage')
def updating_ingredient(request):
    orders = IngredientList.objects.values('ingredient_name')
    return render(request, 'pizza/updatingingredient.html', {'orders': orders})

@login_required(login_url='/loginPage')
def updateIngredient(request):
    if request.method == "POST":
        if request.POST.get('ingredient_name') and request.POST.get('supplier_name'):
            ingresave = IngredientList()
            ingresave.ingredient_name = request.POST.get('ingredient_name')
            ingresave.supplier_name = request.POST.get('supplier_name')
            cursor = connection.cursor()
            cursor.execute("call updateIngredient('"+ingresave.ingredient_name+"', '"+ingresave.supplier_name+"')")
            return render(request, 'pizza/ingredient.html')


@login_required(login_url='/loginPage')
def deletingIngredients(request):
    lists = IngredientList.objects.values('ingredient_name')
    return render(request, 'pizza/deleteIngredient.html', {'lists': lists})

@login_required(login_url='/loginPage')
def deleteIngredient(request):
    if request.method == "POST":
        if request.POST.get('ingredient_name'):
            deleteingre = IngredientList()
            deleteingre.ingredient_name = request.POST.get('ingredient_name')
            cursor = connection.cursor()
            cursor.execute("call deleteIngredient('"+deleteingre.ingredient_name+"')")
            return render(request, 'pizza/ingredient.html')