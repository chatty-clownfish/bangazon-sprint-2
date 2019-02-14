
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Product
from website.models import Order
from django.db import connection




# When user performs a gesture on the product hyperlink
# Then user will be shows the product detail page containing
# title, description, quantity available, price/unit, and a button labeled Add to Order

def product_details(request,id ):
    user_id = request.user.id
    product_details = get_object_or_404(Product, pk=id)
    product_details_quantity = '''
                                SELECT p.id, p.title, (p.quantity - COUNT(po.product_id)) as pCount
                                FROM website_product p
                                JOIN website_productorder po on po.product_id = p.id
                                JOIN website_order o on o.id = po.order_id
                                WHERE p.id = %s
                               '''
    product_details_quantity_id = Product.objects.raw(product_details_quantity, [id,])[0]
    context = {'product_details' : product_details , 'user_id' : user_id, 'product_details_quantity_id': product_details_quantity_id}
    return render(request, 'product/productDetails.html', context)


def add_product_to_cart(request, product_details):
    user_id = request.user.id
    website_order_id = Order.objects.raw('''select * from website_order
                                            Where deletedOn is null and customer_id = %s''', [user_id])[0]
    print('website_order_id', website_order_id.id)
    print('user_id', user_id)
    with connection.cursor() as cursor:
        try:
            cursor.execute('''Insert into website_productorder (deletedOn, order_id, product_id)
                            Values(NULL, %s, %s)''', [website_order_id.id, product_details])
        except IndexError:
            raise Http404("This product type does not exist")
    return HttpResponseRedirect(reverse('website:cart'))

