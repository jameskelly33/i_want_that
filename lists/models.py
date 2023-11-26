from django.db import models

# Create your models here.

class WishListItem(models.Model):
    class Meta:
        verbose_name_plural='Wish List Items'
        ordering=('pk',)
    james = "james"  
    orla='orla'
    jack='jack'
    flat='flat'
    person= [
        (james,'James'),
        (orla,'Orflaith'),
        (jack,'Jack'),
        (flat, "Flat")]
    
    guitar = 'guitar'
    music = 'music'
    food = 'hamburger'
    drink = 'wine-bottle'
    watches = 'clock'
    clothes = 'shirt'
    kitchen = 'kitchen-set'
    crafting = 'paintbursh'
    gardening = 'leaf'
    electronics = 'computer'
    toys = 'gamepad'
    books = 'book'
    health = 'heart-pulse'
    other = 'heart'

    categories = [
        (guitar, 'Guitar'),
        (music, 'Music'),
        (food, 'Food'),
        (drink, 'Drink'),
        (watches, 'Watches'),
        (clothes, 'Clothes'),
        (kitchen, 'Kitchen'),
        (crafting, 'Crafting'),
        (gardening, 'Gardening'),
        (electronics, 'Electronics'),
        (toys, 'Toys'),
        (books, 'Books'),
        (health, 'Health'),
        (other, 'Other'),
    ]

        
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    price = models.DecimalField(max_digits=10,decimal_places=2, default=None)
    person = models.CharField(max_length=50, choices=person)
    categories = models.CharField(max_length=50, choices=categories, default='Other')
    