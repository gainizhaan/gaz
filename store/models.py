from django.db import models

from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  # onetoone to user model
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name



class Product(models.Model):   # each prodect individually
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)  # if the product is digital or physical
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

@property
def imageURL(self):
	try:
		url = self.image.url
	except:
		url = ''
	return url

# summary of items

class Order(models.Model): # our complete order
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) #order is connnected to the customer
	date_ordered = models.DateTimeField(auto_now_add=True) #when order was placed
	complete = models.BooleanField(default=False)  #complete orr incolmplete
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) #conncet to the product
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) #connect to the order
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)


	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True) #we connect to the customer so they can cancel or change the address
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) #connect to the order bc if it is physical only then we ship
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
