from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

from website.forms import UserForm, ProductForm, AddPaymentForm
from website.models import Product, PaymentType
from django.contrib.auth.models import User
from django.db import connection

@login_required
def profileList(request):

    with connection.cursor() as cursor:
        
        try:
            cursor.execute('''
                            SELECT * FROM auth_user AS a 
                            JOIN website_customer AS c ON a.id  = c.user_id
                            WHERE a.id = %s
                            ''', [request.user.id])

            columns= [col[0] for col in cursor.description]
            # print(columns)  

            profile = dict()

            for row in cursor.fetchall():
                print("THIS IS THE ROW:", row)
                to_add = dict(zip(columns, row))
                profile.update(to_add)

            try:
                customerId = request.user.customer.id
                print("CUSTOMER ID****", customerId)
                sql = PaymentType.objects.raw('''SELECT * FROM website_paymenttype as p
                                                WHERE p.customer_id == %s
                                                ''', [customerId])
                sql_list = list(sql)
                print("SQLLLLLL", sql_list.accountNumber)
                print(sql_list.accountNumber)
            except:
                sql = ""                                         
        except connection.OperationalError as err:
            print("Error...", err)
    
    print("CHECK THIS:", profile)
    
    context = {"profile": profile, "sql":sql_list}
    
    return render(request, 'profile/list.html', context)

@login_required
def addPayment(request):
    
    if request.method == 'GET':
        payment_form = AddPaymentForm()
        template_name = 'profile/add_payment.html'
        return render(request, template_name, {'payment_form': payment_form})

    
    if request.method == "POST":
        customer = request.user.id
        name = request.POST["name"]
        accountNumber = request.POST["accountNumber"]

    with connection.cursor() as cursor:
        cursor.execute("INSERT into website_paymenttype VALUES(%s, %s, %s, %s, %s)", [None, name, accountNumber, None, customer])
        return HttpResponseRedirect(reverse('website:profile'))