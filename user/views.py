from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render , redirect 
from django.contrib.auth import login , authenticate
from product.models import Favorite
from .forms import SignUpForm , LoginForm , Resetpassform
from product.models import Favorite

def signup_view(request):
    if request.method == 'POST':
        print("ssss")
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # login(request, user)
            return redirect('user:login')  
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def login_view(request):
    request.session.set_expiry(3600)
    print(request.method)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(f'user: {user}, email: {email} password: {password}')
            if user is not None:
                print("salam")
                login(request, user)
                return redirect('home:home')  
    else:
        form = LoginForm()
    return render(request, 'user/signin.html', {'form': form})


# def password_reset_request(request):
#     if request.method == "POST":
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             user = form.save(request=request)
#             subject = "تنظیم مجدد رمز عبور"
#             email_template_name = "registration/password_reset_email.html"
#             context = {
#                 "email": user.email,
#                 "domain": request.get_host(),
#                 "site_name": "onlineshop",
#                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                 "token": default_token_generator.make_token(user),
#                 "protocol": 'http',
#             }
#             email = render_to_string(email_template_name, context)
#             send_mail(subject, email, 'admin@yourdomain.com', [user.email])
#             return redirect("password_reset_done")
#     else:
#         form = PasswordResetForm()
#     return render(request, "registration/password_reset_form.html", {"form": form})

# def password_reset_done(request):
#     return render(request, "registration/password_reset_done.html")

# def password_reset_confirm(request, uidb64, token):
#     # اینجا باید کد تایید رمز عبور را اضافه کنید
#     return PasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)

# def password_reset_complete(request):
#     return render(request, "registration/password_reset_complete.html")


def dashboard(request):
    # favorite = Favorite.objects.order_by()
    # comment = 
    # address = 
    # order = 
    print(request.user)

  

    return render(request, 'user/account-infoprofile.html', )

