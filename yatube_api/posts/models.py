from django.contrib.auth import get_user_model
from django.db import models

MAX_LENGTH = 200

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=MAX_LENGTH, verbose_name='Название',
    )
    slug = models.SlugField(
        unique=True, verbose_name='Слаг',
    )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True,
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор',
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        verbose_name='Изображение',
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        verbose_name='Группа',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Автор',
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Публикация',
    )
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True,
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий №{self.id} к посту "{self.post}"'


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower', verbose_name='Пользователь',
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following', verbose_name='Подписки',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'following')

    def __str__(self):
        return f'Подписка {self.user.username} на {self.following.username}'
