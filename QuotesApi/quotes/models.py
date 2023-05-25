from django.db import models

class quote(models.Model):
    quote_author = models.CharField(max_length=25)
    quote_body = models.CharField(max_length=50)
    context = models.TextField(max_length=250)
    source = models.URLField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_body


