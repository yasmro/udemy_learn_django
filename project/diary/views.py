from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day

class IndexView(generic.ListView):
    model = Day
    # template_name = 'diary/my_list.html'
    paginate_by = 3

class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class DeleteView(generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    model = Day

def index(request):
    context = {
        'day_list': Day.objects.all(),
    }
    #Day.objects.all(): 保存されているdaysを全部取ってくる
    return render(request, 'diary/day_list.html', context)

def add(request):
    # 送信内容を元にフォームを作る．POSTじゃなければ空Noneのフォーム
    form = DayCreateForm(request.POST or None)

    # method=POST，つまり送信ボタン押下時に入力内容に問題がないときsave (Validation)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常時のページアクセスや，入力内容に誤りがあればページを再表示
    context = {
        'form': DayCreateForm()
    }
    return render(request, 'diary/day_form.html', context)

def update(request, pk):
    # urlのpkをもとにDayを取得
    day = get_object_or_404(Day, pk=pk)

    # フォームに取得したDayを取得する
    form = DayCreateForm(request.POST or None, instance=day)

    # method=POST，つまり送信ボタン押下時に入力内容に問題がないときsave (Validation)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常時のページアクセスや，入力内容に誤りがあればページを再表示(変更点2)
    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)

def delete(request, pk):
    # urlのpkをもとにDayを取得
    day = get_object_or_404(Day, pk=pk)

    # method=POSTのときデリート
    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    # 通常時のページアクセスや，入力内容に誤りがあればページを再表示(変更点2)
    context = {
        'day': day
    }
    return render(request, 'diary/day_confirm_delete.html', context)

def detail(request, pk):
    # urlのpkをもとにDayを取得
    day = get_object_or_404(Day, pk=pk)

    # 通常時のページアクセスや，入力内容に誤りがあればページを再表示(変更点2)
    context = {
        'day': day
    }
    return render(request, 'diary/day_detail.html', context)