from django.db import models

class Wallet(models.Model):
    address = models.CharField(max_length=42, unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=8, default=0.0)

    def __str__(self):
        return self.address
