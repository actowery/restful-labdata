from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import modelformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from .forms import CommentForm, OrderForm, OrderAssayForm, OrderAssayFormSet
from .models import Order, OrderAssay


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
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()

        order_assays_formset = OrderForm.OrderAssayFormSet(self.request.POST, instance=order)
        if order_assays_formset.is_valid():
            order_assays_formset.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['order_assay_formset'] = OrderAssayFormSet(self.request.POST)
        else:
            data['order_assay_formset'] = OrderAssayFormSet()
        return data

    def form_invalid(self, form):
        # This method is called when the form validation fails.
        # You can add your debugging statements here to print the form errors.
        print(form.errors)
        print(form.cleaned_data)
        return super().form_invalid(form)

class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    template_name = "order_edit.html"
    fields = (
        "company", 
        "assays"
    )

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
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
