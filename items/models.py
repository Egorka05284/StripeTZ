from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'item'
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return f'{self.name}'