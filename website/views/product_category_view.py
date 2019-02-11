from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

from website.forms import UserForm, ProductForm
from website.models import Product, ProductType

from django.db import connection


def sell_product(request):
    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    if request.method == "POST":
        seller = request.user.id
        title = request.POST["title"]
        productType = request.POST["productType"]
        description = request.POST["description"]
        price = request.POST["price"]
        quantity = request.POST["quantity"]

    with connection.cursor() as cursor:
        cursor.execute("INSERT into website_product VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", [None, title, description, price, quantity, None, seller, productType])
        return HttpResponseRedirect(reverse('website:index'))



