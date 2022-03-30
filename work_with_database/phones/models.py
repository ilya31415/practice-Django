from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

