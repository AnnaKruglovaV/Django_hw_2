from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/', CategoryListView.as_view(), name='category_list'),
]
