from django.http import Http404
from django.shortcuts import render
from ..models import Product, ProductType

def productHomeView(request):
    try:
        product_type = ProductType.objects.raw('SELECT * FROM website_producttype')
        all_products = Product.objects.raw('SELECT * FROM website_product')
        selected_products = '''
                            SELECT * 
                            FROM website_product 
                            WHERE website_product.productType_id = %s
                            and website_product.deletedOn is NULL
                            LIMIT 3
                            '''

        list_of_products = list()

        for taco in product_type:
            limited_taco = Product.objects.raw(selected_products, [taco.id,])
            list_of_products.append(limited_taco)


    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    context = {'allProducts': all_products, 'product_type': product_type, 'list_of_products':list_of_products}
    return render(request, 'product/product_home.html', context)
