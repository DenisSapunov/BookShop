from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views import View
from .forms import NewUserForm
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import account_activation_token
from django.urls import reverse


@unauthenticated_user
def register_page(request):
    form = NewUserForm
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        form = NewUserForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'пользователь с таким email уже зарегестрирован')
        elif form.is_valid():
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }

            link = reverse('accounts:activate', kwargs={
                'uidb64': email_body['uid'], 'token': email_body['token']})

            email_subject = 'Activate your account'

            activate_url = 'http://' + current_site.domain + link

            email = EmailMessage(
                email_subject,
                'Привет, ' + user.username + ', Пройди по ссылке ниже, чтобы активировать аккаунт \n' + activate_url,
                'bookshop@gmail.com',
                [email],
            )
            email.send(fail_silently=False)
            messages.success(request,
                             'Аккаунт создан успешно, пройдите по ссылке отправденной на ваш email для активации')
            return redirect("accounts:login")
        messages.error(request, 'неправильно заполнена форма')
    return render(request, 'accounts/register.html', {'register_form': form})


class VerificationView(View):

    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('accounts:login' + '?message=' + 'User already activated')

            if user.is_active:
                return redirect('accounts:login')
            user.is_active = True
            user.save()

            messages.success(request, 'Аккаунт создан успешно')
            return redirect('accounts:login')

        except Exception as ex:
            pass

        return redirect('accounts:login')


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Вы вошли как {username}')
                return redirect("/")
            else:
                messages.error(request, 'неверное имя или пароль')
        else:
            messages.error(request, 'неверное имя или пароль')
    form = AuthenticationForm()

    return render(request, "accounts/login.html", {"login_form": form, })


def logout_request(request):
    logout(request)
    messages.info(request, 'вы успешно вышли из аккаунта')
    return redirect('/')


@login_required(login_url='login')
def user_page(request):
    user = request.user
    return render(request, 'accounts/user.html', {'user': user})
