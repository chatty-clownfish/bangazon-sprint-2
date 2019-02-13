from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.db import connection
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

from ..models import Product, ProductType

@login_required

def deleteProduct(request, product_id):
    date = datetime.date.today()
    try:
        with connection.cursor() as cursor:
            cursor.execute('''UPDATE website_product
                                SET deletedOn = %s
                                where website_product.id = %s''', [date, product_id])
            return HttpResponseRedirect(reverse('website:list_products'))



    except Product.DoesNotExist:
        raise Http404("Product does not exist")




# with connection.cursor() as cursor:
#         cursor.execute("INSERT into website_product VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", [None, title, description, price, quantity, None, seller, productType])
#         return HttpResponseRedirect(reverse('website:index'))