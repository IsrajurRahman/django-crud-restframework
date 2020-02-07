from rest_framework import serializers
from .models import BookList

class booklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookList
        #fields = ('name','price') For individula column value
        fields='__all__'