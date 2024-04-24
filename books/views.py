from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer, Userserializer
from rest_framework import generics
from rest_framework.filters import SearchFilter

from django.contrib.auth.models import User


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    filterset_fields = ['genre', 'historical_period', 'author', 'location']
    search_fields = ['title', 'author', 'genre', 'historical_period', 'location']
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    
#usser creation view 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
