from rest_framework import serializers
from quotes.models import quote

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = quote
        fields = "__all__"