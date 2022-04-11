from django import forms


class AddToCartForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=[1,2,3,4,5],coerce=int)

