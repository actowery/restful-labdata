from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from .forms import CommentForm, OrderForm


from .models.models import Order

class HomeView(ListView):
    model = Order
    template_name = "home.html"

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order_list.html"

class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = "order_new.html"

    form_class = OrderForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "order_edit.html"
    fields = (
        "company", 
        "assays"
    )

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "order_delete.html"
    success_url = reverse_lazy("order_list")
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentGet(DetailView):
    model = Order
    template_name = "order_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Order
    form_class = CommentForm
    template_name = "order_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.order = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        order = self.get_object()
        return reverse("order_detail", kwargs={"pk": order.pk})
