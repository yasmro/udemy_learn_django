from django.views import generic
from django.shortcuts import render
from .models import Employee
from .forms import SearchForm

# Create your views here.
class IndexView(generic.ListView):
    model = Employee
    paginate_by = 1
    # template_name = 'employee/employee_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        # もとの辞書にformを追加
        context['form'] = SearchForm(self.request.GET)
        return context
    
    def get_queryset(self):
        # テンプレートへ渡すemployee_listを作成
        form = SearchForm(self.request.GET)
        # これをしないとcleaned_dataができない
        form.is_valid()

        # まず，全社員を取得
        queryset = super().get_queryset()

        # 部署の選択があれば，部署で絞り込み(filter)
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)
        
        # サークルの選択があれば，サークルで絞り込み
        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club = club)
        return queryset
