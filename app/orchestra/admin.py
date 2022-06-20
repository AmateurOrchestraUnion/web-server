from django.contrib import admin
from django import forms

from orchestra.models import Concert, Instrument, User, Applicant, ApplicationForm

# TODO [ ] refactor duplication form class


class InstrumentAdminForm(forms.ModelForm):
    class Meta:
        model = Concert
        exclude = ('is_use', 'is_del')


class ConcertAdminForm(forms.ModelForm):
    class Meta:
        model = Concert
        exclude = ('is_use', 'is_del')


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = Concert
        exclude = ('is_use', 'is_del')


class ApplicantAdminForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ('is_use', 'is_del')


class ApplicationFormAdminForm(forms.ModelForm):
    class Meta:
        model = Concert
        exclude = ('is_use', 'is_del')


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    form = ConcertAdminForm


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    form = InstrumentAdminForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    form = ApplicantAdminForm


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    form = ApplicationFormAdminForm
