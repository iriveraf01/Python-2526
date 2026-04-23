from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    # Añadimos campos de contraseña con validación
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repite la contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def clean_password_confirm(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password_confirm')
        if p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return p2

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['direccion', 'solicita_vendedor']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'solicita_vendedor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'solicita_vendedor': 'Solicito ser vendedor'
        }

from .models import Product

class ProductForm(forms.ModelForm):
    # Campo extra: nueva categoría
    nueva_categoria = forms.CharField(
        required=False,
        label='O crea una nueva categoría',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Mindstorms, Architecture...'})
    )
    # Campo extra: URL de imagen (no es del modelo, lo procesamos en la vista)
    imagen_url = forms.URLField(
        required=False,
        label='O bien, pega un enlace de imagen',
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'})
    )

    class Meta:
        model = Product
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'cantidad', 'estado', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del set o pieza'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe el estado y contenido del producto'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'imagen': 'Subir imagen desde tu ordenador',
            'categoria': 'Selecciona una categoría existente'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer categoria opcional (se puede rellenar nueva_categoria en su lugar)
        self.fields['categoria'].required = False
        # Definir el orden: categoria y nueva_categoria juntas, imagen e imagen_url juntas al final
        self.order_fields(['nombre', 'descripcion', 'categoria', 'nueva_categoria', 'precio', 'cantidad', 'estado', 'imagen', 'imagen_url'])