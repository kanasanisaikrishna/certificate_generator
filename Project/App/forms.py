# forms.py
from django import forms
from .models import *

class CertificateForm(forms.Form):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), label='Select Teacher')
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label='Select Student')

class TeacherForm(forms.Form):
    class Meta:
        model = Teacher
        fields = ['tname', 'subject']

    tname=forms.CharField(max_length=100)
    subject=forms.CharField(max_length=100)

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = ['sname', 'group','teachers']

    sname=forms.CharField(max_length=100)
    group=forms.CharField(max_length=100)
    teachers=forms.ModelMultipleChoiceField(queryset=Teacher.objects.all(),widget=forms.CheckboxSelectMultiple)

