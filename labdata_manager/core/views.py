from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Order

class OrderListView(ListView):
    model = Order
    template_name = "home.html"

class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"

class OrderCreateView(CreateView):
    model = Order
    template_name = "order_new.html"
    fields = ["company", "assays"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "order_edit.html"
    fields = ["company", "assays"]

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "order_delete.html"
    success_url = reverse_lazy("home")