from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, PasswordResetForm
from .models import Student,SlotsAvailable, Specialization, TechCompany
from django.http import HttpResponse

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']
            student = Student.objects.filter(email_address=email_address).first()
            if student and student.check_password(password):
                # Authentication successful
                request.session['email_address'] = student.email_address
                return redirect('dashboard')
            else:
                # Authentication failed
                return render(request, self.template_name, {'form': form, 'error': 'Invalid email or password'})
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Invalid email or password'})

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        # Fetch all available slots
        slots_available = SlotsAvailable.objects.select_related(
            'specialization_id', 'tech_company_id').all()

        # Group slots by specialization
        specialization_slots = {}
        total_slots = 0  # Initialize total slots count
        for slot in slots_available:
            specialization_name = slot.specialization_id.specialization_name
            if specialization_name not in specialization_slots:
                specialization_slots[specialization_name] = []
            specialization_slots[specialization_name].append(slot)
            total_slots += slot.slot_count  # Increment total slots count

        # Fetch all tech companies
        tech_companies = TechCompany.objects.all()

        # Perform some basic data analysis
        total_companies = tech_companies.count()

        context = {
            'specialization_slots': specialization_slots,
            'tech_companies': tech_companies,
            'total_slots': total_slots,  # Add total slots count to context
            'total_companies': total_companies,  # Add total companies count to context
        }
        return render(request, self.template_name, context)


class RegisterView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            specialization_id=form.cleaned_data['specialization_id']
            email_address = form.cleaned_data['email_address']
            password_hash = form.cleaned_data['password_hash']

            # REQ-1: Check if account already exists
            if Student.objects.filter(email_address=email_address).exists():
                form.add_error(None, "This email address has already been used!")
                return render(request, self.template_name, {'form': form})
            else:
                # Create the account
                # Save the application
                new_account = form.save(commit=False)
                new_account.set_password(form.cleaned_data['password_hash'])
                new_account.save()
                return redirect('login')
        else:
            # If the form is not valid, render the template with the form and errors
            return render(request, self.template_name, {'form': form})

class PasswordResetView(View):
    template_name = 'forgot_password.html'

    def get(self, request):
        form = PasswordResetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            email_address = form.cleaned_data['email_address']

            # REQ-1: Check if the email address exists
            if not Student.objects.filter(email_address=email_address).exists():
                form.add_error(None, "Invalid email address!")
            else:
                # Redirect to dashboard
                return redirect('dashboard', email_address=email_address)
            # If there are errors, render the template with the form and errors
            return render(request, self.template_name, {'form': form})
        else:
            # If the form is not valid, render the template with the form and errors
            return render(request, self.template_name, {'form': form})
