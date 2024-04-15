from django.contrib import admin

from . models import Specialization, Student, County,Constituency,Ward, TechCompany, SlotsAvailable

models_to_register = [Specialization, Student, County ,Constituency,Ward, TechCompany, SlotsAvailable]

for model in models_to_register:
    admin.site.register(model)
