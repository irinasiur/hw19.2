from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'purchase_price', 'category', 'description', 'image',)
        # exclude = ('date_of_creation',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = ''

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                          'радар', ]
        if cleaned_data in forbidden_word:
            raise forms.ValidationError('Запрещенное слово')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        forbidden_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                          'радар', ]
        if cleaned_data in forbidden_word:
            raise forms.ValidationError('Запрещенное слово')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product',)
