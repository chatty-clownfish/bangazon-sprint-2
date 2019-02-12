from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from website.models import ProductOrder, Order
import datetime
from django.db import connection

def list_cart(request):
    user_id = request.user.id
    orders = Order.objects.raw(''' SELECT website_order.id FROM website_order
                                Where website_order.customer_id = %s
                                ''', [user_id])
    cart_items = ProductOrder.objects.raw('''Select * FROM website_productorder
                                            Where order_id =%s''', (user_id, ))
    context = {'orders' : orders , 'cart_items' : cart_items }

    return render(request, "product/cart.html" ,context)


def delete_cart(request, order_id, product_id):
    date = datetime.date.today()
    print("date",date)

    with connection.cursor() as cursor:
        deletedOn = date
        order_id = order_id
        product_id = product_id
        cursor.execute("Update website_productorder SET deletedOn=%s WHERE order_id= %s AND product_id= %s ",[deletedOn, order_id, product_id])

    return HttpResponseRedirect(reverse('website:index'))