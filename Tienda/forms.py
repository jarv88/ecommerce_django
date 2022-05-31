from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Form creado para extraer la imagen y que sirva el Upload_to
#Sin el form no se guardaba en la carpeta media por lo que al querer mostrar no habia imagen
class ImageUploadForm(forms.Form):
    
    image = forms.ImageField()




class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='User', widget=forms.TextInput(attrs={'class': 'user'}), max_length=150, required=True, help_text='Required. Max. 150 characters. Letters, numbers and @ /. / + / - / _ ')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Required. At least 8 characters and can´t be only numbers')
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Required. Repeat password')
    first_name = forms.CharField(
        label='Name', widget=forms.TextInput(attrs={'class': 'first_name'}), max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        label='Last Name', widget=forms.TextInput(attrs={'class': 'last_name'}), max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email'}), max_length=254, required=True, help_text='Valid email required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )