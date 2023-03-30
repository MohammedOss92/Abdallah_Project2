from django.db import models

# Create your models here.

class MsgsTypes(models.Model):
    name  = models.CharField(max_length=100, null=True)
    new_msg = models.CharField(max_length=2,default=1)

    def __str__(self):
         return self.name

class Msgs(models.Model):
    msgs_types = models.ForeignKey(MsgsTypes, null=True, on_delete=models.SET_NULL)
    msgs_name  = models.CharField(max_length=1000, null=True)
    new_msgs = models.CharField(max_length=2, null=True,default=1)

    def __str__(self):
         return self.msgs_name

# ##################################

class MeesageType(models.Model):
    MsgTypes = models.CharField(max_length=100, null=True)
    new_msg = models.CharField(max_length=2,default=1)

    def __str__(self):
        return self.MsgTypes

class Messages(models.Model):
    MessageName =models.CharField(max_length=1000, null=True)
    ID_Type = models.ForeignKey(MeesageType, null=True, on_delete=models.SET_NULL)
    new_msgs = models.CharField(max_length=2, null=True,default=1)

    def __str__(self):
        return self.MessageName