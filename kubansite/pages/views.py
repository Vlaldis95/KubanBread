from django.shortcuts import redirect, render
from pages.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
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
                    'text': form.cleaned_data['text']}
            message = '\n'.join(body.values())
            try:
                send_mail(subject,
                          message, body['e_mail'], 'vlaldis@yandex.ru')
            except BadHeaderError:
                return HttpResponse('Ошибка в письмe.')
            return redirect('success')
    form = ContactForm()
    return render(request, 'pages/index.html', {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
