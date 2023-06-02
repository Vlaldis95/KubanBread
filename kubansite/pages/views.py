from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from kubansite.settings import RECIPIENTS_EMAIL
from pages.forms import ContactForm

from .models import Category, Product
from .utils import paginate_products


def index(request):
    """Главная страница"""
    return render(request, 'pages/index.html')


def contacts(request):
    """Страница контакты и с формой обратной связи"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {'first_name': form.cleaned_data['first_name'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'e_mail': form.cleaned_data['e_mail'],
                    'region': form.cleaned_data['region'],
                    'sales_channel': form.cleaned_data['sales_channel'],
                    'nalog': form.cleaned_data['nalog'],
                    'text': form.cleaned_data['text']}
            ln = '\n'
            message = (f"Имя: {body['first_name']}{ln}"
                       f"Номер телефона: {body['phone_number']}{ln}"
                       f"e-mail: {body['e_mail']}{ln}"
                       f"Регион: {body['region']}{ln}"
                       f"Канал продаж: {body['sales_channel']}{ln}"
                       f"Вид налога: {body['nalog']}{ln}"
                       f"Текст сообщения: {body['text']}")
            try:
                send_mail("Сообщение с сайта",
                          message,
                          body['e_mail'],
                          RECIPIENTS_EMAIL)
                flag = True
                form = ContactForm()
                return render(
                    request, 'pages/contacts.html',
                    {'flag': flag, 'form': form})
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
    form = ContactForm()
    return render(request, 'pages/contacts.html', {'form': form})


def category(request, slug):
    """Страница категории в каталоге."""
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    page_obj = paginate_products(request, products)
    context = {'category': category, 'page_obj': page_obj}
    return render(request, 'pages/category.html', context)


def katalog(request):
    """Страница категорий в каталоге."""
    category = Category.objects.all()
    page_obj = paginate_products(request, category)
    context = {'page_obj': page_obj, }
    return render(request, 'pages/katalog.html', context)


def product(request, product_id):
    """Страница определенного продукта в каталоге."""
    product = get_object_or_404(Product, id=product_id)
    packaging = product.packages.all()
    context = {'product': product, 'packaging': packaging}
    return render(request, 'pages/product.html', context)


def page_not_found(request, exception):
    return render(request,
                  'pages/404.html', {'path': request.path}, status=404)


def e_handler500(request):
    return render(request, 'pages/500.html', status=500)


def packaging(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    packaging = product.packages.all()
    context = {'packaging': packaging, 'product': product}
    return render(request, 'pages/packaging.html', context)
