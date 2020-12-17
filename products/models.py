from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey("Category", null=True, blank=True,
     on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    book_format = models.CharField(max_length=554)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
