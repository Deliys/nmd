from django.db import models


class Autor(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)

class DocSorpbd(models.Model):

    id = models.AutoField(primary_key=True)
    registration_certificate_number = models.CharField(max_length=50)#номер свидетельства
    database_name = models.CharField(max_length=100)#название базы данных
    request_number = models.CharField(max_length=50)#номер заявки
    requestdate = models.DateField()#дата заявки
    registrationdate = models.DateField()#дата регистрации
    authors = models.ManyToManyField(Autor)#автор
    individual_owners = models.ManyToManyField('Owner', related_name='individual_owners')#правообладатель 
    organization_owners = models.ManyToManyField('Owner', related_name='organization_owners')#

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    owner_types =  models.BooleanField()


