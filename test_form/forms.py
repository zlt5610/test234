#coding=utf-8
from django import forms

from test_form.models import Clazz, Student
import re


class LoginForm(forms.Form):
    username=forms.CharField(label=u'姓名',max_length=8)
    password=forms.CharField(label=u'密码',max_length=8,widget=forms.PasswordInput)

class ClazzForm(forms.ModelForm):
    class Meta:
        model=Clazz
        fields=['cname']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['sname']

    def clean_sname(self):
        sname=self.cleaned_data.get('sname','')
        p=re.compile('^1[34589]\d{9}$]')
        if p.match(sname):
            return sname
        else:
            raise forms.ValidationError(u'格式不正确',code='sname_invalid')



