from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':
                   '*Ваше имя',
                     'class': 'popup__input form__input'}))  # Имя
    phone_number = forms.RegexField(
        regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
        widget=forms.TextInput(attrs={'placeholder': '* +7-999-999-99-99',
                                      'class': 'popup__input form__input',
                                      'type': 'tel',
                                      'pattern': '^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'}))  # Номер телефона
    e_mail = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': '*Ваш e-mail',
               'class': 'popup__input form__input',
               'pattern': "[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+"}),
                max_length=50)  # Электронная почта
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваш регион (страна, город, район, населенный пункт)',
                   'class': 'popup__input form__input'}), max_length=100, required=False)  # Регион
    sales_channel = forms.ChoiceField(
        choices=(('Retail', 'Retail'),
                 ('Дистрибуция', 'Дистрибуция'),
                 ('Физ.лицо', 'Физ.лицо')),
        widget=forms.Select(attrs={'class': 'popup__select'}))
    nalog = forms.ChoiceField(
        choices=(('-', '-'), ('НДС', 'НДС'), ('Без НДС', 'Без НДС')),
        widget=forms.Select(attrs={'class': 'popup__select'}))   # Вид налога
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение',
                   'class': 'popup__input popup__input_type_text form__input'}), max_length=200, required=False)
    rules = forms.BooleanField(
        label='Я принимаю условия пользовательского соглашения',
        widget=forms.CheckboxInput(
            attrs={'class':
                   'popup__input form__input form__input_el_extra_options'}))
