from django.db import models

class CongressMan(models.Model):
    def __init__(self, name, party, local):
        self.name = name
        self.party = party
        self.local = local

    name = models.CharField(max_length = 50)
    party = models.CharField(max_length = 50)
    local = models.CharField(max_length = 100)

class Restaurant(models.Model):
    def __init__(self, name, latitude, longitude, address):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.address = address

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def update(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    name = models.CharField(max_length = 50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length = 250)
    kind = models.CharField(max_length=20)

class CongressRestaurantMap(models.Model):
    congress = models.ForeignKey(CongressMan)
    restaurant = models.ForeignKey(Restaurant)
    price = models.IntegerField()
