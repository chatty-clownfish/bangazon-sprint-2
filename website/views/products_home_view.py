from django.http import Http404
from django.shortcuts import render
from ..models import Product, ProductType

def productHomeView(request):
    try:

        sql = '''
            SELECT pt.name as typeName, p.title as prodTitle, COUNT(p.id) as pCount, p.id, pt.id
            FROM website_producttype pt
            JOIN website_product p on p.productType_id = pt.id
            WHERE pt.id = %s
            and p.deletedOn is null
            '''

        product_type = ProductType.objects.raw('SELECT * FROM website_producttype')
        selected_products = '''
                            SELECT * 
                            FROM website_product 
                            WHERE website_product.productType_id = %s 
                            AND website_product.deletedOn is NULL
                            LIMIT 3
                            '''

        list_of_products = list()

        for category in product_type:
            limited_category = Product.objects.raw(selected_products, [category.id,])
            list_of_products.append(limited_category)


    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    context = {'product_type': product_type, 'list_of_products':list_of_products}
    return render(request, 'product/product_home.html', context)




# def productHomeView(request):
#     try:
#         product_type = ProductType.objects.raw('SELECT * FROM website_producttype')
#         all_products = Product.objects.raw('SELECT * FROM website_product')
#         selected_products = '''
#                             SELECT * 
#                             FROM website_product 
#                             WHERE website_product.productType_id = %s 
#                             LIMIT 3
#                             '''

#         list_of_products = list()

#         for taco in product_type:
#             limited_taco = Product.objects.raw(selected_products, [taco.id,])
#             list_of_products.append(limited_taco)


#     except Product.DoesNotExist:
#         raise Http404("Product does not exist")

#     context = {'allProducts': all_products, 'product_type': product_type, 'list_of_products':list_of_products}
#     return render(request, 'product/product_home.html', context)