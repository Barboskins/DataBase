from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    sort_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    sort = request.GET.get('sort')

    if sort:
        phones = phones.order_by(sort_dict.get(sort))
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

# phones = Phone.objects.all()
# for phone in phones:
#     print(phone.name)
