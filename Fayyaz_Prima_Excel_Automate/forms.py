from django import forms


class UploadCSVForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(attrs={'accept': '.csv,.xls,.xlsx'})
    )