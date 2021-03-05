from django.db import models


class AgroUser(models.Model):
    user_type = models.CharField(max_length=50,null=True)
    full_name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)
    number = models.IntegerField(null=False)

    def __str__(self):
        return self.user_type
