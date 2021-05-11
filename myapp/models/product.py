from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    categories=models.ForeignKey('Category',on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to="upload/product",default=0)

    @staticmethod
    
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)


##filter 
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(categories=category_id)
        else:
            return Product.get_all_products()