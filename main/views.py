from django.shortcuts import render

from main.models import Product


# Create your views here.
# def home(request):
#     products = Product.objects.all()
#     data = {'products': products}
#     return render(request, 'main/test.html', data)
def home(request):
    type_filter = request.GET.get('type')
    if type_filter:
        products = Product.objects.filter(type=type_filter)
    else:
        products = Product.objects.all()
    types = Product.objects.values_list('type', flat=True).distinct()
    return render(request, 'main/test.html', {'products': products, 'types': types})
