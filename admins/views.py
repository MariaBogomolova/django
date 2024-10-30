from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryEditForm, ProductEditForm
from geekshop.mixin import CustomDispatchMixin
from mainapp.models import ProductCategory, Product
from users.models import User


# Create your views here.


def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'

        return context


class UserCreateView(CreateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Регистрация'
        return context


class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование пользователя'
        return context


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admins_user')

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return super().form_valid(form)
    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.is_active = False
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории'
        return context


class CategoryCreateView(CreateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создание категории'
        return context


class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование категории'
        return context


class CategoryDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:admins_category')


class ProductCategoryListView(ListView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-category-read.html'
    context_object_name = 'products_category'

    def get_queryset(self):
         return Product.objects.filter(category=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Товары категории'
        return context




class ProductUpdateView(UpdateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('admins:admins_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование товара категории'
        return context

