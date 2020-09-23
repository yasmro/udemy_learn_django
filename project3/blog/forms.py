from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # formの各フィールドに対してform-control class属性を与える
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('name', 'text')
        # どの記事に移動するかは既に決めているのでいらない（隠し項目）