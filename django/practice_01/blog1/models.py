from django.db import models

class Post1(models.Model):
    title = models.CharField(max_length=30, default='')
    content = models.TextField(null=True, default='')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f'[{self.pk}] {self.title} {self.created_at} {self.updated_at}'
    
    def get_absolute_url(self):
        return f'/blog1/{self.pk}/'