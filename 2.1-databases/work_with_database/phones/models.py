from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=255)  # название телефона.
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цена телефона.
    image = models.ImageField(upload_to='phones/')  # изображения телефона.
    release_date = models.DateField()  # дата выпуска телефона.
    lte_exists = models.BooleanField(default=False)  # булево поле, указывающее на наличие LTE.
    slug = models.SlugField(unique=True, max_length=255, blank=True)  # Слагификация названия телефона.
    print('Модель создана.')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)   # Слагификация названия телефона.
        super(Phone, self).save(*args, **kwargs)


