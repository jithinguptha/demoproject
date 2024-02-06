from django.db.models import Q
from django.shortcuts import render

from shop.models import product


# Create your views here.
def search(request):
    s = None
    c = ""
    if (request.method == "POST"):
        s = request.POST['s']
        if s!= " ":
            c = product.objects.filter(name__icontains=s)
    return render(request, 'search.html', {'s': s, 'c': c})
