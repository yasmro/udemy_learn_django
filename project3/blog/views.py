from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect
from django.views import generic
from .forms import CommentCreateForm
from .models import Post, Category, Comment


class IndexView(generic.ListView):
    # template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 10

    def get_queryset(self):
        # return Post.objects.order_by('-created_at')
        # 先頭に-をつけると降順になる！

        queryset = Post.objects.order_by('-created_at')

        # 検索フォーム(nameがkeyword)の値を受け取る
        keyword = self.request.GET.get("keyword")

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
            # 〜が含むかどうか fieldName__icontains(大文字小文字無視), __contains

        return queryset
         
class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        # category = get_object_or_404(Category, pk=self.kwargs['pk'])
        # queryset = Post.objects.order_by('-created_at').filter(category=category)
        category_pk = self.kwargs['pk']
        queryset = Post.objects.order_by('-created_at').filter(category__pk = category_pk)
        return queryset


class DetailView(generic.DetailView):
    model = Post
    template_name='blog/post_detail.html'

class CommentView(generic.CreateView):
    model = Comment
    # fields = ('name', 'text')
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('blog:detail', pk=post_pk)
