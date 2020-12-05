from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from userprofile import models


class LoginUser(View):
    """
    Url: login
    Logins the user using entered credentials.
    GET: Provides form for credentials input.
    POST: Authenticates the user, logins and redirects to dashboard if successful.
    """

    def get(self, request):
        return render(request, 'userprofile/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        ifregister = request.POST.get('register')
        if ifregister:
            return redirect(register)
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login')
        else:
            return HttpResponse("Not Authorized")


class RegisterUser(View):
    """
    Url: login
    Logins the user using entered credentials.
    GET: Provides form for credentials input.
    POST: Authenticates the user, logins and redirects to dashboard if successful.
    """

    def get(self, request):
        return render(request, 'userprofile/register.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        img = request.POST.get('img')
        if password == confirmpassword:
            profile = models.User(email=email, password=password, name=name,
                                  age=age, gender=gender, phone=phone, address=address, img=img)
            profile.save()
            return redirect('Profile')
        else:
            return HttpResponse("Password and Confirm password are not equal")

class Profile(View):
    
    def get(self, request):
        data=models.User.objects.all()
        userdata={
            "userdata":data
        }
        return render(request, 'userprofile/profile.html',userdata)