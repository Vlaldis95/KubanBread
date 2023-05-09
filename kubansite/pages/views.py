from django.shortcuts import redirect, render
from pages.forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Сообщение с контактной формы сайта'
            body = {'first_name': form.cleaned_data['first_name'],
                    'legal_entity': form.cleaned_data['legal_entity'],
                    'inn': form.cleaned_data['inn'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'e_mail': form.cleaned_data['e_mail'],
                    'region': form.cleaned_data['region'],
                    'sales_channel': form.cleaned_data['sales_channel'],
                    'nalog': form.cleaned_data['nalog'],
                    'theme': form.cleaned_data['theme'],
                    'text': form.cleaned_data['text'],
                    'rules': form.cleaned_data['rules']}
            message = '\n'.join(body.values())
            try:
                send_mail(subject,
                          message,
                          f"{body['first_name']} {body['email']}",
                          ['vlaldis@yandex.ru'])
                return redirect('success')
            except BadHeaderError:
                return HttpResponse('Найден некорретный заголовок')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'pages/index.html', {'form': form})
