from django import forms
from .models import Club, Department

class SearchForm(forms.Form):
    # forms.ModelChoiceFieldで検索
    # queryset:対象のモデル
    # label:ラベル 
    # required: 必須か？

    club = forms.ModelChoiceField(
        queryset=Club.objects,
        label='サークル',
        required=False
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects,
        label='部署',
        required=False
    )