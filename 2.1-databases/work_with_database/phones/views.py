from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    """Перенаправляет пользователя на страницу каталога"""
    return redirect('catalog')


def show_catalog(request):
    """Отображает каталог страницы"""
    print('Отображает каталог страницы')
    sort = request.GET.get('sort', 'name')  # Сортировка по умолчанию по имени
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, 'catalog.html', context)


def show_product(request, slug):
    """Отображает страницу продукта"""
    print('Отображает страницу продукта')
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)

