from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from shop.models import product

from cart.models import cart

from cart.models import account

from cart.models import order


# Create your views here.
@login_required
def cartview(request):
    total = 0
    u = request.user
    c = cart.objects.filter(user=u)
    for i in c:
        total += i.quantity * i.product.price
    return render(request, 'cart.html', {'cart': c, 'total': total})

@login_required
def addtocart(request, n):
    p = product.objects.get(name=n)
    u = request.user
    try:
        c = cart.objects.get(user=u, product=p)
        if (p.stock>0):
            c.quantity -= 1
            c.save()
            p.stock += 1
            p.save()

    except:
        if (p.stock > 0):
            c = cart.objects.create(product=p, user=u, quantity=1)
            c.save()
            p.stock += 1
            p.save()
    return redirect('cartview')

@login_required
def removecart(request, n):
    p = product.objects.get(name=n)
    u = request.user
    c = cart.objects.get(user=u, product=p)
    if (c.quantity > 1):
        c.quantity -= 1
        c.save()
    else:
        c.delete()
    return redirect('cartview')

@login_required
def deletecart(request, n):
    p = product.objects.get(name=n)
    u = request.user
    try:
        c = cart.objects.get(user=u, product=p)


        c.delete()
        p.stock += c.quantity
        p.save()
    except:
        pass
    return redirect('cartview')

@login_required
def orderform(request):
    if (request.method == 'POST'):
        a = request.POST['u']
        p = request.POST['p']
        n = request.POST['a']
        u = request.user

        c = cart.objects.filter(user=u)
        total = 0
        for i in c:
            total += i.quantity * i.product.price
        try:
            ac = account.objects.get(accountnum=n)
            if (ac.amount >= total):
                ac.amount = ac.amount - total
                ac.save()
                for i in c:
                    o = order.objects.create(user=u, product=i.product, address=a, phone=p, no_of_items=i.quantity,
                                             order_status="paid")
                    o.save()
                c.delete()
                msg = "Your order Placed Successfully"
                return render(request, 'orderdetail.html', {'msg': msg})
            else:
                msg = "Insufficient Amount.You can't Place Order"
                return render(request, 'orderdetail.html', {'msg': msg})


        except:
            pass
    return render(request, 'order.html')

@login_required
def orderview(request):
    u = request.user
    o = order.objects.filter(user=u)
    return render(request, 'orderview.html', {'o': o})
