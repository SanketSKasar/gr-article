from django.db import models
import qrcode

from .constants import *

class Article(models.Model):
    name = models.CharField(max_length = 50)
    unit = models.CharField(max_length = 2, choices=units_of_measurement, null=True, blank=True)

    def __str__(self):
        return self.name

class Goods(models.Model):
    sr_no = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    color = models.CharField(max_length = 20, choices = article_colors)
    other = models.TextField()

    def __str__(self):
        return f"{self.sr_no}-{self.article.name}"

    def get_qr(self):
        return qrcode.make(f"{self.article.name}-{self.article.unit}-{self.color}-{self.quantity}")

class Supplier(models.Model):
    name =  models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    gst_no = models.CharField(max_length = 15)
    other = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.gst_no}"

class GR(models.Model):
    date = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}-{self.supplier.name}"

