from django.contrib.auth.models import User
from django import forms
from website.models import Product, PaymentType, Customer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('address', 'phoneNumber',)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title','productType', 'description', 'price', 'quantity', )

class AddPaymentForm(forms.ModelForm):

    class Meta:
        model = PaymentType
        fields = ('name', 'accountNumber', )