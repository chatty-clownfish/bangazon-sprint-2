from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from website.models import ProductOrder, Order, PaymentType
import datetime
from django.db import connection
from django.contrib.auth.decorators import login_required

@login_required
def list_cart(request):
    user_id = request.user.id
    orders = Order.objects.raw(''' SELECT website_order.id FROM website_order
                                Where website_order.customer_id = %s
                                ''', [user_id])[0]
    cart_items = ProductOrder.objects.raw('''Select * FROM website_productorder
                                            Where order_id =%s''', [orders.id])
    print("ORDERRSSS", orders)
    print("CART ITEMSSS", cart_items)
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

    return HttpResponseRedirect(reverse('website:cart'))

def completeOrder(request):
    customerId = request.user.customer.id
    
    sql = PaymentType.objects.raw('''SELECT * FROM website_paymenttype as p
                                    WHERE p.customer_id == %s''', [customerId])
                
    sql_list = list(sql)

    context = {"sql":sql_list}
    return render(request, "product/complete_order.html", context)

def selectPayment(request):
    return render(request, "product/thankyou.html")