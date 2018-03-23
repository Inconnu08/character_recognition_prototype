from django.conf.urls import url

from products.views import ProductList, SearchProductView

app_name = 'Products'

urlpatterns = [
    url(r'^$', ProductList.as_view()),
    url(r'^search/', SearchProductView.as_view(), name='query'),
    # url(r'^(?P<product_id>[0-9]+)/', include(product_urlpatterns)),
]