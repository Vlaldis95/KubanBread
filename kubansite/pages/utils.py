from django.core.paginator import Paginator


def paginate_products(request,products):
    paginator = Paginator(products, 12) 
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)