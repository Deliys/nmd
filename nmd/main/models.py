from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # 1) имя
    last_name = models.CharField(max_length=50,null=True)  # 2) фамилия
    first_name = models.CharField(max_length=100,null=True)  # 4) отчество
    code = models.CharField(max_length=50 ,null=True)  # 5) шифр научной специальности человека
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # 4) отчество (если есть)
    birth_day = models.DateField(blank=True, null=True)  # 6) дата рождения
    death_day = models.DateField(blank=True, null=True)  # может быть None
    academic_degree = models.CharField(max_length=100, blank=True, null=True)  # 14) шифр научной специальности человека
    research_code = models.CharField(max_length=50,null=True)  # 15) место работы (несколько)
    phone = models.CharField(max_length=20,null=True)  # 17) телефон


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
    def name_doc(self):
        return self.database_name
class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    owner_types =  models.BooleanField()

class SoftwareRegistrationCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    certificate_number = models.CharField(max_length=50)
    software_name = models.CharField(max_length=100)
    request_number = models.CharField(max_length=50)
    request_date = models.DateField()
    registration_date = models.DateField()
    authors = models.ManyToManyField(Autor)
    individual_owners = models.ManyToManyField(Owner, related_name='software_individual_owners')  # Changed related_name
    organization_owners = models.ManyToManyField(Owner, related_name='software_organization_owners')  # Changed related_name
    def name_doc(self):
        return self.software_name
class User(models.Model):
    USER_TYPES = (
        ('user', 'Пользователь'),
        ('manager', 'Менеджер'),
        ('admin', 'Админ'),
    )
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    type_user = models.CharField(max_length=12, choices=USER_TYPES,default='user')