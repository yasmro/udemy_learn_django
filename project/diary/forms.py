from django import forms
from .models import Day
#modelからDayをインポート

class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__' 
        #('title', 'text', 'date')