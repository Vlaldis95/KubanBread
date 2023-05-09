from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class': 'form__input'}))  # Имя
    legal_entity = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Юридическое лицо',
                   'class': 'form__input'}))  # Юридическое лицо
    inn = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'ИНН',
                   'class': 'form__input'}), max_length=12)  # ИНН
    phone_number = forms.RegexField(
        regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
        widget=forms.TextInput(attrs={'placeholder': '+7-999-999-99-99',
                                      'class': 'form__input',
                                      'type': 'tel'}))  # Номер телефона
    e_mail = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'E-mail',
               'class': 'form__input'}),
                max_length=50)  # Электронная почта
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваш регион',
                   'class': 'form__input'}), max_length=100)  # Регион
    sales_channel = forms.ChoiceField(
        choices=(('Retail', 'Retail'),
                 ('Дистрибуция', 'Дистрибуция'), 
                 ('Физ.лицо', 'Физ.лицо')),
        widget=forms.Select(attrs={'class': 'form__select'}))
    nalog = forms.ChoiceField(
        choices=(('НДС', 'НДС'), ('Без НДС', 'Без НДС')),
        widget=forms.Select(attrs={'class': 'form__select'}))   # Вид налога
    theme = forms.ChoiceField(
        choices=(('Запрос на сотрудничество', 'Запрос на сотрудничество'),
                 ('Вопрос по качеству', 'Вопрос по качеству'),
                 ('Другое', 'Другое')),
        widget=forms.Select(attrs={'class': 'form__select'}))
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение',
                   'class': 'form__input'}), max_length=100)
    rules = forms.BooleanField(
        label='Я принимаю условия пользовательского соглашения',
        widget=forms.CheckboxInput(
            attrs={'class': 'form__input contact__checkbox'}))
