from django.shortcuts import render
from rest_framework import generics
from .models import Product, Customer, Sale
from .serializers import ProductSerializer, CustomerSerializer, SaleSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <div style="min-height:100vh; background: linear-gradient(135deg, #e0e7ff 0%, #f0f7fa 100%); padding-bottom: 80px;">
            <div class="container-fluid" style="display: flex; gap: 20px; background: #007bff; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                <a href="/admin/" style="text-decoration:none; color:#fff; font-weight:bold;">Admin Panel</a>
                <a href="/api/products/" style="text-decoration:none; color:#fff; font-weight:bold;">Products API</a>
                <a href="/api/customers/" style="text-decoration:none; color:#fff; font-weight:bold;">Customers API</a>
                <a href="/api/sales/" style="text-decoration:none; color:#fff; font-weight:bold;">Sales API</a>
            </div>
            <h3 style="color: red; text-align: center;">Welcome to the Point of Sale System</h3>
        </div>
        <footer style="
            background: #007bff; 
            color: #fff; 
            text-align: center; 
            padding: 20px; 
            border-radius: 8px; 
            font-weight: bold;
            font-size: 16px;
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            margin: 0;
            z-index: 1000;
        ">
            &copy; 2025 <span style="color:#fff;">Point of Sale</span> &mdash; Powered by Django<br>
            <span style="font-size: 14px; font-weight: normal;">
                <a href="#" style="color: #fff; text-decoration: underline;">Terms and Conditions</a> |
                <a href="#" style="color: #fff; text-decoration: underline;">Privacy Policy</a> |
                Software Developer: Whinya Brighton <span style="color: #ffd700;">Zomac Digital</span>
            </span>
        </footer>
    """)

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SaleListView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
