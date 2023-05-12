from django.urls import path
from .views import OrderListView, OrderCreateView, OrderDetailView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path("order/new/", OrderCreateView.as_view(), name="order_new"),
    path("order/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("order/<int:pk>/edit/", OrderUpdateView.as_view(), name="order_edit"),
    path("order/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
    path("", OrderListView.as_view(), name="home"),
]