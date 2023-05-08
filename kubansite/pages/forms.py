from django import forms


class ContactForm(forms.Form):
    category = forms.ChoiceField(
        choices=(('1', 'Физ.лицо'),
                 ('2', 'Юр.лицо'),
                 ('3', 'ИП')))  # Выбор категории клиента
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))  # Имя
    legal_entity = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Юридическое лицо'}))  # Юридическое лицо
    inn = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'placeholder': 'ИНН'}), min_value=12, max_value=12)  # ИНН
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '+7-999-999-99-99'}))  # Номер телефона
    e_mail = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'E-mail'}), max_length=50)  # Электронная почта
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваш регион'}), max_length=100)  # Регион
    sales_channel = forms.ChoiceField(
        choices=(('1', 'Retail'), ('2', 'Дистрибуция'), ('3', 'Физ.лицо')))
    nalog = forms.ChoiceField(
        choices=(('1', 'НДС'), ('2', 'Без НДС')))   # Вид налога
    theme = forms.ChoiceField(
        choices=(('1', 'Запрос на сотрудничество'),
                 ('2', 'Вопрос по качеству'), ('3', 'Другое')))
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение'}), max_length=100)
    rules = forms.BooleanField(label ='Я принимаю условия пользовательского солгашения')
