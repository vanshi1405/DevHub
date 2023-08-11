from django.db import models
from django.contrib.auth.models import User


def validate_mobile_number(value):
    mobile_number_str = str(value)
    if len(mobile_number_str) != 10:
        raise models.ValidationError("mobile number contains 10 digit ")
    return value


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    mobile_number = models.BigIntegerField(validators=[validate_mobile_number])
    dob = models.DateField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Group(models.Model):
    name = models.CharField(max_length=100,unique=True)
    member = models.ManyToManyField(Profile, related_name='groups',null=True,blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
