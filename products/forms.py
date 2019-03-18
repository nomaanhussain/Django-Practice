from django import forms

from.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Title',
            'Description',
            'price'
        ]

    def clean_Title(self, *args, **kwargs):
        Title = self.cleaned_data.get('Title')
        if not 'cfe' in Title:
            raise forms.ValidationError("This is not a valid field")
        else:
            return Title

class RawProductForm(forms.Form):
    Title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    Description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)