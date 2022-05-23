from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


#Form creado para extraer la imagen y que sirva el Upload_to
#Sin el form no se guardaba en la carpeta media por lo que al querer mostrar no habia imagen
class ImageUploadForm(forms.Form):
    
    image = forms.ImageField()