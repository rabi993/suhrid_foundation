# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer