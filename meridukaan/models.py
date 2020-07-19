from django.db import models

# Create your models here.
class product(models.Model):
    # product_id = models.IntegerField(unique=True)
    product_category = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_image = models.ImageField(default='no-image.jpeg', upload_to='images/')
    product_description = models.CharField(max_length=300)

    def __str__(self):
        return self.product_name