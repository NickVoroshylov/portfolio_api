from django.db import models

from .portfolio import Portfolio


def portfolio_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/portfolio_owner - portfolio_name/<filename>
    return f"portfolios/{instance.portfolio.owner} - {instance.portfolio.name}/{filename}"


class Picture(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=portfolio_directory_path)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
