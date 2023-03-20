from django.db import models
from django.contrib.auth.models import User

PROVINCE = [ 
    ('CF', 'CAPITAL FEDERAL'),
    ('BA', 'BUENOS AIRES'),
    ('CA', 'CATAMARCA'),
    ('CH', 'CHACO'),
    ('CU', 'CHUBUT'),
    ('CO', 'CÓRDOBA'),
    ('CR', 'CORRIENTES'),
    ('ER', 'ENTRE RÍOS'),
    ('FO', 'FORMOSA'),
    ('JU', 'JUJUY'),
    ('LP', 'LA PAMPA'),
    ('LR', 'LA RIOJA'),
    ('MZ', 'MENDOZA'),
    ('MI', 'MISIONES'),
    ('NQ', 'NEUQUÉN'),
    ('RN', 'RÍO NEGRO'),
    ('SA', 'SALTA'),
    ('SJ', 'SAN JUAN'),
    ('SL', 'SAN LUIS'),
    ('SC', 'SANTA CRUZ'),
    ('SF', 'SANTA FE'),
    ('SE', 'SANTIAGO DEL ESTERO'),
    ('TF', 'TIERRA DEL FUEGO'),
    ('TU', 'TUCUMÁN')
            ]

BILLING = [ 
        ('1' , 'PRO'),
        ('2', 'FC')
           ]

class Color(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_color')
    charge_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Carriage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_carriage')
    charge_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    web = models.CharField(max_length=200, blank=True)
    enlaced_number_system = models.IntegerField()
    enlaced_code_system = models.CharField(max_length=20, blank=True)
    observations = models.TextField(blank=True)

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_category')
    charge_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=200, blank=True)
    observations = models.TextField()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_product')
    charge_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    materials = models.CharField(max_length=200)
    weight = models.FloatField()
    size = models.CharField(max_length=100)
    catergory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    units_per_package = models.IntegerField()
    observations = models.TextField()

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_client')
    charge_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_price_list')
    charge_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100, blank=True)
    cuit = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200)
    province = models.CharField(max_length=2, choices=PROVINCE, default='BA')
    location = models.CharField(max_length=100)
    observations = models.TextField(blank=True)

class Price_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_price_list')
    charge_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    initial_date = models.DateField()
    finish_date = models.DateField()
    observations = models.TextField(blank=True)
    enlaced_number_system = models.IntegerField()
    enlaced_code_system = models.CharField(max_length=30, blank=True)

class Line_price_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_line_price')
    charge_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_line_price_list')
    price = models.FloatField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_order')
    charge_date = models.DateTimeField(auto_now_add=True)
    price_list = models.ForeignKey(Price_list, on_delete=models.CASCADE, related_name='price_list_order')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_order')
    carriage = models.ForeignKey(Carriage, on_delete=models.CASCADE, related_name='carriage_order')
    billing = models.CharField(max_length=1, choices=BILLING, default='2')

class Line_order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_line_order')
    charge_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_line_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_line_order')
    amount = models.IntegerField()
    price = models.FloatField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color_line_order')
    billing = models.CharField(max_length=1, choices=BILLING, default='2')
    discount = models.IntegerField()
