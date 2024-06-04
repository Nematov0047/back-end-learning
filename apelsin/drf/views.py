from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerilarizer, ContactSerializer
from .models import Contact

# Create your views here.
@api_view()
def index(request):
    return Response({'status':'active'})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerilarizer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerilarizer

@api_view(['GET','POST'])
def ser(request): # a function for learning serializers
    if request.method == 'GET':
        queryset = Contact.objects.all()
        # beginning of filter code
        name = request.query_params.get('name')
        print('incoming name is', name)
        contact = request.query_params.get('contact')

        if name:
            queryset = queryset.filter(name__contains=name)
            print('name has been filtered')
        
        if contact:
            queryset = queryset.filter(contact__contains=contact)
         # beginning of ordering code
        ordering = request.query_params.get('ordering')
        if ordering:
            ordering_fields = ordering.split(',')
            queryset = queryset.order_by(*ordering_fields)

        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        serializer = ContactSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Contact.objects.create(name=serializer.data['name'], contact=serializer.data['contact'])
        return Response(serializer.data)