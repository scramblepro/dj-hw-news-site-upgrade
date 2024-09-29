from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название разд.')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', upload_to='articles/')

    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles')

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_ordered_scopes(self):
        return sorted(self.scopes.all(), key=lambda x: (not x.is_main, x.tag.name))


class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Название')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной', default=False)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
