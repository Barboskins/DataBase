from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=40,allow_unicode=True)

    def slug_url(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().slug_url(*args, **kwargs)

    def __str__(self):
        return f'{self.id}:{self.name}'


    # # TODO: Добавьте требуемые поля
    # pass
