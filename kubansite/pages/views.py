from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from kubansite.settings import RECIPIENTS_EMAIL
from pages.forms import ContactForm, WeightForm

from .models import Category, Product, Catalog
from .utils import paginate_products


def index(request):
    """Главная страница"""
    catalog = Catalog.objects.all()
    return render(request, 'pages/index.html', {'catalog': catalog})


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
    category_id=category.id
    products = category.products.all()
    form = WeightForm(request.POST)
    if form.is_valid():
        weight_category = form.cleaned_data.get('title')
        products = weight_category.products.filter(category_id=category_id)
        page_obj = paginate_products(request, products)
        return render(request, 'pages/category.html', {'category': category, 'page_obj': page_obj, 'form': form})
    page_obj = paginate_products(request, products)
    return render(request, 'pages/category.html', {'category': category, 'page_obj': page_obj, 'form': form})


def katalog(request):
    """Страница категорий в каталоге."""
    category = Category.objects.all()
    page_obj = paginate_products(request, category)
    context = {'page_obj': page_obj, }
    return render(request, 'pages/katalog.html', context)


def product(request, product_id):
    """Страница определенного продукта в каталоге."""
    product = get_object_or_404(Product, id=product_id)
    images = product.images.all()
    exists = images.exists()
    context = {'product': product, 'images': images, 'exists': exists}
    return render(request, 'pages/product.html', context)


def page_not_found(request, exception):
    return render(request,
                  'pages/404.html', {'path': request.path}, status=404)


def e_handler500(request):
    return render(request, 'pages/500.html', status=500)

def privacy(request):
    return render(request,'pages/privacy.html')

def agreement(request):
    return render(request,'pages/agreement.html')




