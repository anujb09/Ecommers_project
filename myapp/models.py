from django.db import models

# Create your models here.


class product(models.Model):
    CAT=((1,"shoes"),(2,"mobile"),(3,"cloths"),(4,"Watch"),(5,"Sports"))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    price=models.IntegerField()
    cat=models.IntegerField(choices=CAT , verbose_name="Category")
    pdetails=models.CharField(max_length=200 , verbose_name="Details")
    is_active=models.BooleanField(default=True , verbose_name="Is_availabe")
    pimage=models.ImageField(upload_to='image')



    def __str__(self):
        return self.name

class Cart(models.Model):
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    pid=models.ForeignKey("product",on_delete=models.CASCADE, db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    use_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    p_id=models.ForeignKey('product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)
    amt=models.FloatField()
