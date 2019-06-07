from django import forms

class InsertingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Poduct Id'
            }
        )
    )
    product_name = forms.CharField(
        label= 'Product Name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Porduct Name'
            }
        )
    )
    product_cost = forms.CharField(
        label= 'Product Cost',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Porduct Cost'
            }
        )
    )
    product_color = forms.CharField(
        label= 'Product Color',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_class = forms.CharField(
        label= 'Product Class',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    customer_name = forms.CharField(
        label= 'Customer Name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )

    customer_mobile = forms.IntegerField(
        label= 'Customer Mobile',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile'
            }
        )
    )
    customer_email = forms.EmailField(
        label= 'Customer Email',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email'
            }
        )
    )

class UpdateDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Product ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Poduct Id'
            }
        )
    )
    product_cost = forms.CharField(
        label='Product Cost',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Porduct Cost'
            }
        )
    )

class DeleteDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Product ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Poduct Id'
            }
        )
    )
