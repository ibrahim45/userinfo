from rest_framework import serializers

from details.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('name', 'age', 'email')
