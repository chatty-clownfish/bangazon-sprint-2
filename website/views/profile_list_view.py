from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product
from django.db import connection

@login_required
def profileList(request):


    with connection.cursor() as cursor:
        try:
            cursor.execute('''
                            SELECT * FROM auth_user AS a 
                            JOIN website_customer AS c ON a.id  = c.user_id
                            JOIN website_paymenttype as p ON a.id = p.customer_id
                            WHERE a.id = %s
                            ''', [request.user.id])

            columns= [col[0] for col in cursor.description]
            print(columns)  

            profile = dict()

            for row in cursor.fetchall():
                print(row)
                to_add = dict(zip(columns, row))
                profile.update(to_add)

        except connection.OperationalError as err:
            print("Error...", err)
    
    print(profile)
    context = {"profile": profile}

    return render(request, 'profile/list.html', context)