from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100, strip=True, widget=forms.TextInput(attrs={'placeholder': 'Например, Тимофей', 'autocomplete': 'given-name'}))

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError('Введите имя.')
        return name
