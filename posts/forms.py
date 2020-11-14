from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("group", "text")
        labels = {"text": "Введите текст", "group": "Выберите группу поста"}