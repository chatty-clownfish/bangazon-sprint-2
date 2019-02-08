from django.conf.urls import url
from django.urls import path

from . import views
from .views.product_detail_views import product_details

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    path('products/<int:id>/', product_details, name='product_detail'),
    # url(r'^profile$', views.list_profile, name='profile'),
    # url(r'^cart$', views.list_cart, name='cart'),
]