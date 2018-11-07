from django.db import models

class List(models.Model):
    # Create a database
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    # to reprent data on admin page
    def __str__(self):
        # stringify the Boolean 'completed'
        return self.item + ' ' + '|' + ' ' + str(self.completed)
