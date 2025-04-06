from django import forms
from .models import Department, Employee

class EmployeeFilterForm(forms.Form):
    name = forms.CharField(
        label='氏名',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    department = forms.ModelChoiceField(
        label='部署',
        queryset=Department.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.ChoiceField(
        label='在籍状況',
        choices=[('', '選択してください')] + list(Employee.STATUS_CHOICES),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    hire_date_from = forms.DateField(
        label='入社日（開始）',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    hire_date_to = forms.DateField(
        label='入社日（終了）',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    min_salary = forms.IntegerField(
        label='最低給与',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    max_salary = forms.IntegerField(
        label='最高給与',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )