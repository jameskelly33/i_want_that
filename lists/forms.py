from django import forms
from .models import WishListItem

   
class WishListItemForm(forms.ModelForm):

    class Meta:
        model = WishListItem
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control-lg",'placeholder':'What is it?'})
        self.fields["description"].widget.attrs.update({"class": "form-control-lg","rows":3,'cols':20,'placeholder':'Enter a short description'})
        self.fields["url"].widget.attrs.update({"class": "form-control-lg",'placeholder':'Paste link'})
        self.fields["price"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["person"].widget.attrs.update({"class": "form-control-lg"})
    