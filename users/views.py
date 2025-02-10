from django.conf import settings
from django.core.mail import send_mail

from .models import User

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import auth
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, UpdateView, CreateView

from geekshop.mixin import BaseClassContextMixin
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from baskets.models import Basket
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.


class LoginLoginView(LoginView, BaseClassContextMixin):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Geekshop - Авторизация'

# def login(request):
#
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'title': 'Geekshop - Авторизация',
#         'form': form
#     }
#     return render(request, 'users/login.html', context)

class RegisterView(CreateView, BaseClassContextMixin):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    title = 'Geekshop - Регистрация'


    # def form_valid(self, form):
    #     user = form.save()
    #
    #     if user:
    #         auth.login(self.request, user)
    #
    #     return super().form_valid(form)


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_link(user):
                messages.success(request, 'Вы успешно зарегистрирвоались')
            return redirect(self.success_url)
        return redirect(self.success_url)


def send_verify_link(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    subject = f'Для активации учетной записи {user.username} пройдите по ссылке'
    message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user and user.activation_key == activation_key and not user.is_activation_key_expired():
            user.activation_key = ''
            #user.activation_key_created = None
            #user.activation_key_expires = None
            user.is_active = True
            user.save()
            auth.login(request, user)
        return render(request, 'users/verification.html')
    except Exception as e:
        return HttpResponseRedirect(reverse('index'))

# def register(request):
#
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Вы успешно зарегистрировались")
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm()
#
#     context = {
#         'title': 'Geekshop - Регистрация',
#         'form': form
#     }
#     return render(request, 'users/register.html', context)

class ProfileFormView(UpdateView, BaseClassContextMixin):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Geekshop - Профайл'

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileFormView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return redirect(self.success_url)

# @login_required
# def profile(request):
#
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Данные успешно сохранены")
#
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             messages.error(request, 'Что-то пошло не так')
#
#
#     context = {
#         'title': 'Geekshop - Личный кабинет',
#         'form': UserProfileForm(instance=request.user),
#         'baskets': Basket.objects.filter(user=request.user)
#
#     }
#     return render(request, 'users/profile.html', context)

class Logout(LogoutView):
    template_name = 'mainapp/index.html'

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))



