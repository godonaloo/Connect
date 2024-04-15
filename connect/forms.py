from django import forms
from .models import Student, Specialization

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
    )
    specialization_id = forms.ModelChoiceField(
        queryset=Specialization.objects.all(),
        required=True,
        label='Area of Specialization',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'specialization_id', 'email_address', 'password_hash']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'specialization_id': 'Area of Specialization',
            'email_address': 'Email Address',
            'password_hash': 'Password',
            'confirm_password': 'Confirm Password',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'password_hash': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password_hash")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and confirm password do not match")

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data["password_hash"])
        if commit:
            instance.save()
        return instance

class LoginForm(forms.Form):
    email_address = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email_address = cleaned_data.get("email_address")
        password = cleaned_data.get("password")
        return cleaned_data

class PasswordResetForm(forms.Form):
    email_address = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )

    def clean_email_address(self):
        email = self.cleaned_data.get('email_address')
        if not Student.objects.filter(email_address=email).exists():
            raise forms.ValidationError("This email address is not associated with any account.")
        return email

