import os
from django.db import models
import qrcode
import datetime

from .constants import *

class Article(models.Model):
    name = models.CharField(max_length = 50)
    unit = models.CharField(max_length = 2, choices=units_of_measurement, null=True, blank=True)

    def __str__(self):
        return self.name

class Goods(models.Model):
    sr_no = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="goods_article")
    quantity = models.IntegerField()
    color = models.CharField(max_length = 20, choices = article_colors)
    other = models.TextField()

    def __str__(self):
        return f"{self.sr_no}-{self.article.name}"

    def get_qr(self):
        qr_image = qrcode.make(f"{self.article.name}-{self.article.unit}-{self.color}-{self.quantity}")
        qr_image.save(f'{self}.png')
        return "file://" + os.path.abspath(f'{self}.png')

class Supplier(models.Model):
    name =  models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    gst_no = models.CharField(max_length = 15)
    other = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.gst_no}"

class GR(models.Model):
    gr_id = models.CharField(max_length = 10, unique=True)
    date = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="gr_supplier")
    goods = models.ManyToManyField(Goods, related_name="gr_goods")

    def __str__(self):
        return f"{self.date}-{self.supplier.name}"

    def save(self, *args, **kwargs):
        if not self.id:
            today = datetime.datetime.today()
            year = today.year
            if datetime.datetime.now().month <= 3:
                year -= 1
            current_year_start_date = datetime.date(year, 4, 1)
            running_serial = GR.objects.filter(date__gte = current_year_start_date).count() + 1
            self.gr_id = f"{year%100}{(year+1)%100}/{running_serial}"
        super(GR, self).save(*args, **kwargs)

