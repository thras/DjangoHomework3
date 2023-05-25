from rest_framework import generics, mixins, permissions
from quotes.models import quote
from quotes.api.serializers import QuoteSerializer
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.pagination import SmallSetPagination

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = quote.objects.all().order_by("id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination
   

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]