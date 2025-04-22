from rest_framework import serializers
from shelf.models import Shelves

class Shelf_Serializer(serializers.ModelSerializer):
    year = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Shelves
        fields = ('year', 'price', 'weight', 'pages',)

    def validate(self, value):
        if not value:
            return None
        try:
            return int(value)
        except ValueError:
            raise serializers.ValidationError('Valid year required')