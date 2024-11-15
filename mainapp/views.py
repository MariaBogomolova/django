from django.http import JsonResponse
from django.shortcuts import render
import os, json

from django.template.loader import render_to_string

from .models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


# def products(request):
#     context = {
#         'title': 'geekshop',
#         'products': [{'name': 'Худи черного цвета с монограммами adidas Originals',
#                       'price': '6 090,00', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
#                       'link': 'vendor/img/products/Adidas-hoodie.png'},
#                      {'name': 'Синяя куртка The North Face',
#                       'price': '23 725,00',
#                       'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
#                       'link': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
#                      {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
#                       'price': '3 390,00',
#                       'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
#                       'link': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
#                      {'name': 'Черный рюкзак Nike Heritage',
#                       'price': '2 340,00',
#                       'description': 'Плотная ткань. Легкий материал.',
#                       'link': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
#                      {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
#                       'price': '3 590,00',
#                       'description': 'Гладкий кожаный верх. Натуральный материал.',
#                       'link': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
#                      {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
#                       'price': '2 890,00',
#                       'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
#                       'link': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
#         ]
#     }
#     return render(request, 'mainapp/products.html', context)


# extra task context from JSON file
# def products(request):
#     file_path = os.path.join(MODULE_DIR, 'fixtures/db.json')
#     with open(file_path, encoding='utf-8') as f:
#         context = json.load(f)
#     return render(request, 'mainapp/products.html', context)


#extra task info from models


def products(request, category_id=None, page_id=1):
    products = Product.objects.filter(category_id=category_id) if category_id is not None else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)


    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        context = {
            'products': products}
        result = render_to_string('mainapp/filtered_products.html', context)

        return JsonResponse({'result': result})
    else:
        context = {
            'title': 'Каталог',
            'categories': ProductCategory.objects.all(),
            'products': products_paginator}
    return render(request, 'mainapp/products.html', context)


