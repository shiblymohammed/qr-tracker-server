from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    code = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Scan(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
