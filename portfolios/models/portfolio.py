from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'name'], name='unique_portfolio_name_for_user')
        ]

    def __str__(self):
        return f"{self.owner} - {self.name}"
