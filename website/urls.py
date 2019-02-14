from django.conf.urls import url
from django.urls import path
from . import views
from .views.product_detail_views import product_details
from .views.cart_views import delete_cart
from .views.deleteProduct import deleteProduct
from .views.product_detail_views import add_product_to_cart

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    path('profile/', views.profileList, name='profile'),
    path('profile/addpayment/', views.addPayment, name='add_payment'),
    path('home/', views.productHomeView, name='product_home'),
    path('producttype/<int:pk>/', views.products_by_type, name='products_by_type'),
    path('products/<int:id>/', product_details, name='product_detail'),
    path('cart/', views.list_cart, name='cart'),
    path('cart_views/<int:order_id>/<int:product_id>', views.delete_cart, name='cart_views'),
    path('deleteProduct/<int:product_id>', views.deleteProduct, name='deleteProduct'),
    path('addProduct/<int:product_details>', views.add_product_to_cart, name='addProduct'),
    path('cart/completeorder/', views.completeOrder, name='completeOrder'),
    path('cart/selectpayment/', views.selectPayment, name='selectPayment')
    ]