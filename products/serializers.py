from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from products.models import Products


class ProductListSerializer(ModelSerializer):
    variances = PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Products
        fields = '__all__'
        # exclude = ('created_by', 'updated_by')
