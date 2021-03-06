from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from website.forms import UserForm, ProductForm
from website.models import Product, ProductType

from django.db import connection

@login_required
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
            product_details = cursor.lastrowid

    return HttpResponseRedirect(reverse("website:product_detail", args=(product_details,)))
        

    

