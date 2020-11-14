from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("group", "text")
        labels = {"text": "Текст поста", "group": "Группа поста"}

    def check_filled_text(self):
        data = self.cleaned_data["text"]
        if len(data.replace(' ', '')) == 0:
            raise forms.ValidationError("Данное поле должно быть заполнено")
        return data

