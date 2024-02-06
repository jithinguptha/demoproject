from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from shop.models import category

from shop.models import product


# Create your views here.
def allcategory(request):
    c = category.objects.all()
    return render(request, 'category.html', {'c': c})


def allproduct(request, m):
    c = category.objects.get(id=m)
    p = product.objects.filter(category=c)
    return render(request, 'product.html', {'c': c, 'p': p})


def details(request, p):
    t = product.objects.get(id=p)
    return render(request, 'details.html', {'t': t})


def user_login(request):
    if (request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            return redirect('category')
        else:
            return HttpResponse('invalid')

    return render(request, 'login.html')


def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if p == cp:
            user = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            user.save()
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
                return redirect('category')
            else:
                return HttpResponse('invalid')

        else:
            return HttpResponse('password are not same')

    return render(request, 'register.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('category')


