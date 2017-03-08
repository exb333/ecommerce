from django.conf.urls import url

from .views import ProductListView, ProductDetailView, product_detail_view_func

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name = 'products'),
    url(r'(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    # url(r'pro/(?P<pk>\d+)', product_detail_view_func, name='product_detail_function'),
]


