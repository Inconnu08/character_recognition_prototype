from rest_framework import generics
from rest_framework.permissions import AllowAny

from products.models import Products
from products.serializers import ProductListSerializer


class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ProductListSerializer
    search_fields = ('title', )

class SearchProductView(generics.ListAPIView):
    # template_name = "search/view.html"
    serializer_class = ProductListSerializer

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Products.objects.search(query)
        return None