from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=150
    )
    content = models.TextField(
        verbose_name='Content',
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Creation date',
        auto_now_add=True
    )
    is_published = models.BooleanField(
        verbose_name='Published',
        default=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Category'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['-created_at',]

class Category(models.Model):

    title = models.CharField(
        verbose_name="Title",
        max_length=80,
        db_index=True
    )

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})
