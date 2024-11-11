# home/urls.py
from django.urls import path
from .views import ProductDetailView, CommentCreateView

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
]