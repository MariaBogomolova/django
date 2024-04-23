from django.shortcuts import render
import os, json


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
def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/db.json')
    with open(file_path, encoding='utf-8') as f:
        context = json.load(f)
    return render(request, 'mainapp/products.html', context)
