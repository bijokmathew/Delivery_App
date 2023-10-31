from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'name' : 'Product Name',
            'description':"Product description",
            'price':'Product Price'
        }
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                if self.fields[field].required:
                    placeholder= f'{placeholders[field]}*'
                else:
                    placeholder={placeholders[field]}
                
                self.fields[field].widget.attrs['placeholder']= placeholder
            
            self.fields[field].widget.attrs['class']='form-control border-black rounded-0'

       