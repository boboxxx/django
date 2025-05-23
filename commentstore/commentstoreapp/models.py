from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=100)
    visit_date = models.DateField()
    comment_str = models.CharField(max_length=500)

    def __str__(self):
        details = ''
        details += f'Name        : {self.name}\n'
        details += f'VisitDate   : {self.visit_date}\n'
        details += f'Comment     : {self.comment_str}\n'
        return details
