from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Product, ProductType

def products_by_type(request, pk):
    '''
    This method gets one individual producttype and lists it along with all associated products by name, quantity and price.

    Method uses a SELECT from the product table and JOIN with the producttype table.
    '''
    try:

        sql = '''
        SELECT p.title, p.quantity, p.price, pt.name, pt.id as "productTypeId", p.id
        FROM website_product p
        JOIN website_producttype pt on pt.id = p.productType_id
        WHERE pt.id=%s
        '''
        product_type = ProductType.objects.raw(sql, [pk,])[0]
        product = Product.objects.raw(sql, [pk,])

    except IndexError:
        raise Http404("This product type does not exist")

    context = {'type': product_type, 'prod':product}
    return render(request, 'product/products_by_type.html', context)