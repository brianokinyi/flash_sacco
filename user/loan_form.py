from django import forms

#

#copy of Applicant’s ID
#copy of the referee’s ID
#copy of Applicant’s PIN certificate
#all guarantors’ ID copies
#3 months’ certified pay slips
#3 months’ bank statements
#utility bill (not more than 3 months old)
#


from django.forms.widgets import CheckboxSelectMultiple
from django.forms import ModelMultipleChoiceField,ModelForm

from .models import User, Group
from savings.models import Savings, Deposits


class LoanForm (forms.Form ):

    applicantId = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Account Holders ID number'} ), label=' National ID' )

    refereeID = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Referees ID number'} ), label=' National ID' )

    guarantor=forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Guarantors Name'} ),
                                    label='Guarantors Name' )

    amount = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Loan Amount'} ),
                                    label='Amount' )

    file_field = forms.FileField( widget=forms.ClearableFileInput( attrs=
                                                                   {'multiple': True, 'webkitdirectory': True,
                                                                    'directory': True} ) )


class ProfileUpdateForm(forms.ModelForm):

        firstName = forms.CharField( widget=forms.TextInput(
            attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off'} ),
            label='First Name' )
        lastName = forms.CharField( widget=forms.TextInput(
            attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off'} ),
            label='Last Name' )
        email = forms.CharField( widget=forms.TextInput(
            attrs={'class': 'form-control ', 'required': True, 'autocomplete': 'off'} ),
            label='Email Address' )

        contact = forms.IntegerField( widget=forms.TextInput(
            attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off'} ),
            label='Phone Number' )


        class Meta:
            model = User
            fields = ['firstName', 'lastName', 'email', 'contact']

class PinUpdateForm(forms.Form):
    contact=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off','placeholder':'Account Pin'}),label='Current Account Pin')
    contact_cp1=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off','placeholder':'Account Pin'}),label='Enter Account Pin')
    contact_cp2=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off','placeholder':'Account Pin'}),label='New Pin Again')


class RegisterForm(forms.ModelForm):
    firstName = forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder':'Your First Name'} ),
        label='First Name' )
    lastName = forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder':'Your Last Name'} ),
        label='Last Name' )
    IDnumber = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Your Identification Number'} ),
        label='ID Number' )
    DateOfBirth = forms.DateField( widget=forms.TextInput(
        attrs={'class': 'date-pick form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Date of Birth','data-date-format':'DD d MM yyyy'} ),
        label='Date of Birth' )

    register_date = forms.DateField( widget=forms.TextInput(
        attrs={'class': 'date-pick form-control', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Date of Birth', 'data-date-format': 'DD d MM yyyy'} ),
        label='Date of register' )

    contact = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Phone Number'} ),
        label='Phone Number' )
    email = forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder':'Email Address'} ),
        label='Email' )
    address = forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder':'Postal Address'} ),
        label='Address' )
    code = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder':'Postal Code'} ),
        label='Postal Code' )
    town = forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder':'Town'} ),
        label='Town' )
    # marital=forms.ChoiceField(widget=forms.)
    married_choices = (
        ('single', 'single'),
        ('married', 'married'),
    )
    marital = forms.CharField(
        max_length=30,
        widget=forms.Select( choices=married_choices ),
    )
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'IDnumber', 'DateOfBirth', 'contact', 'email', 'address', 'code', 'town',
                  'image','register_date']


class RegisterGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


