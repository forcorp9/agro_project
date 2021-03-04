from django.db import models


class Agro_User(models.Model):
    SPISKA = [
        (1,'Jismoniy_Shaxs'),
        (2,'Yuridik_Shaxs'),
    ]
    user_type = models.CharField(choices=SPISKA,max_length=50,null=True)
    full_name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)
    number = models.IntegerField(null=False)


# class Accommodation(models.Model):
#     choice_category = models.ForeignKey()
#     city_region = models.ForeignKey()
#     ad_type = models.ForeignKey()
#     heading_ad = models.ForeignKey()
#
#     condition = models.CharField(choices=)
#     business = models.CharField(choices=)
#     availability = models.CharField(choices=)
#     cost = models.IntegerField(null=False)
#     bill = models.CharField(choices=)
#     description = models.TextField(null=False)
#     negotiable = models.BooleanField(blank=True)
