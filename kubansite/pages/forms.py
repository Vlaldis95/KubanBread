from django import forms


class ContactForm(forms.Form):
    category = forms.ChoiceField(
        label='Категория покупателя',
        choices=(('1', 'Физ.лицо'), ('2', 'Юр.лицо'), ('3', 'ИП')))
    first_name = forms.CharField(label='Имя', max_length=50)
    legal_entity = forms.CharField(label='Юридическое лицо', max_length=50)
    inn = forms.IntegerField(label='ИНН', min_value=12, max_value=12)
    phone_number = forms.CharField(label='Номер телефона')
    e_mail = forms.EmailField(label='Электронная почта', max_length=50)
    region = forms.CharField(label='Регион', max_length=100)
    sales_channel = forms.ChoiceField(
        label='Канал продаж',
        choices=(('1', 'Retail'), ('2', 'Дистрибуция'), ('3', 'Физ.лицо')))
    nalog = forms.ChoiceField(
        label='Вид налога', choices=(('1', 'НДС'), ('2', 'Без НДС')))
    theme = forms.ChoiceField(
        label='Тема обращения',
        choices=(('1', 'Запрос на сотрудничество'),
                 ('2', 'Вопрос по качеству'), ('3', 'Другое')))
    text = forms.CharField(label='Сообщение', max_length=100)
