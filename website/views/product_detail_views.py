
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Product



# When user performs a gesture on the product hyperlink
# Then user will be shows the product detail page containing
# title, description, quantity available, price/unit, and a button labeled Add to Order

def product_details(request,id ):
  product_details = get_object_or_404(Product, pk=id)
  context = {'product_details' : product_details}
  return render(request, 'product/productDetails.html', context)
