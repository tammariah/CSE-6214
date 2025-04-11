from django.db import models

from django.contrib.auth.models import User, Group, Permission

#User Models


class CustomUser(User):
    role = models.CharField(max_length=20, choices=[
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    ], default='customer')

    
    def __str__(self):
        return self.username
     
class Customer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length = 200, null = True)
    shipping_preference = models.CharField(max_length=255, blank=True)
    bank_account_number = models.CharField(max_length=50, null=True)
    # Add other customer-specific fields as needed

    def __str__(self):
        return self.user.username
    
class Seller(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255, null=True)
    store_description = models.TextField(blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, null=True)
    # Add other seller-specific fields as needed

    def __str__(self):
        return self.user.username 

#Product Models  
class Tag(models.Model):
    name = models.CharField(max_length=200, null = True)    

    def __str__(self):
        return self.name

    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length = 200, null = True)
    store = models.CharField(max_length=200,blank=True, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    category =models.CharField(max_length = 200, null = True, choices = CATEGORY)
    image = models.ImageField(upload_to='store/', blank = True, null=True)
    description = models.CharField(max_length = 200, null = True, blank = True)
    qty= models.IntegerField(null=True, blank =True)
    date_created =  models.DateTimeField(auto_now_add=True, null = True)  
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    STATUS = ( ('Pending', 'Pending'),
               ('Out for delivery', 'Out for delivery'),
               ('Delivered', 'Delivered'),
     )

    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null = True)  
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    note = models.CharField(max_length=1000, null=True)
   
    def __str__(self):
         return self.product.name


    




    

''''
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE) 
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default="no_profile.png",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        if self.name:
          return self.name
        else:
            return "Unnamed"
class Seller(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE) 
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default="no_profile.png",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
      
    def __str__(self):
        if self.name:
          return self.name
        else:
            return "Unnamed"        
class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE) 
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default="no_profile.png",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
      
    def __str__(self):
        if self.name:
          return self.name
        else:
            return "Unnamed"       

class Tag(models.Model):
    name = models.CharField(max_length=200, null = True)    

    def __str__(self):
        return self.name

    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null=True)
    category =models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created =  models.DateTimeField(auto_now_add=True, null = True)  
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    STATUS = ( ('Pending', 'Pending'),
               ('Out for delivery', 'Out for delivery'),
               ('Delivered', 'Delivered'),
     )

    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null = True)  
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    note = models.CharField(max_length=1000, null=True)
   
    def __str__(self):
         return self.product.name
    '''