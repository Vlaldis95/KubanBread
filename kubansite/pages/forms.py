from django import forms


class ContactForm(forms.Form):
    category = forms.ChoiceField(
        choices=(('1', 'Физ.лицо'),
                 ('2', 'Юр.лицо'),
                 ('3', 'ИП')))  # Выбор категории клиента
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form__input'}))  # Имя
    legal_entity = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Юридическое лицо', 'class': 'form__input'}))  # Юридическое лицо
    inn = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'ИНН', 'class': 'form__input'}), max_length=12)  # ИНН
    phone_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': '+7-999-999-99-99', 'class': 'form__input', 'type': 'tel', 'pattern': '\+?[0-9\s\-\(\)]+'}))  # Номер телефона
    e_mail = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'E-mail', 'class': 'form__input'}), max_length=50)  # Электронная почта
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваш регион', 'class': 'form__input'}), max_length=100)  # Регион
    sales_channel = forms.ChoiceField(
        choices=(('1', 'Retail'), ('2', 'Дистрибуция'), ('3', 'Физ.лицо')),
        widget=forms.Select(attrs={'class':'form__select'}))
    nalog = forms.ChoiceField(
        choices=(('1', 'НДС'), ('2', 'Без НДС')),
        widget=forms.Select(attrs={'class':'form__select'}))   # Вид налога
    theme = forms.ChoiceField(
        choices=(('1', 'Запрос на сотрудничество'),
                 ('2', 'Вопрос по качеству'), ('3', 'Другое')),
                 widget=forms.Select(attrs={'class':'form__select'}))
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение', 'class': 'form__input'}), max_length=100)
    rules = forms.BooleanField(label ='Я принимаю условия пользовательского солгашения',
        widget=forms.CheckboxInput(
            attrs={'class': 'form__input contact__checkbox'}))
