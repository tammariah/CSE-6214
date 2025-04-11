from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer, Seller, CustomUser


def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            group = Group.objects.get(name = 'admin')
            instance.groups.add(group)
            print(' Created Admin')
        elif instance.role == 'seller':
            group = Group.objects.get(name = 'seller')
            instance.groups.add(group)
            Seller.objects.create(user = instance,)  
            print('Created Seller')
            
        else :
            group = Group.objects.get(name = 'customer')
            instance.groups.add(group)
            Customer.objects.create(user = instance,)    
            print('Created Customer')      
post_save.connect(create_profile, sender=CustomUser)    

    



''''    
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name = 'customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name = instance.username,
        )
    print('Profile Created')
post_save.connect(customer_profile, sender=User)    
'''