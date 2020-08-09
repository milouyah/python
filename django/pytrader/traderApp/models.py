from django.db import models

# Create your models here.
class StockPrice(models.Model):
    date = models.DateField(max_length=20, primary_key=True)
    open = models.DecimalField(max_digits=10,decimal_places=3)
    close = models.DecimalField(max_digits=10,decimal_places=3)
    high = models.DecimalField(max_digits=10,decimal_places=3)
    low = models.DecimalField(max_digits=10,decimal_places=3)

    # https://realpython.com/python-f-strings/
    def __str__(self):
        return f'{self.date},{self.open},{self.close},{self.high},{self.low},'