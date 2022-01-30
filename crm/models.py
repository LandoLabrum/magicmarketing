
   
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import time

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)
    tel = models.BigIntegerField( blank=True)
    session_id = models.CharField(max_length=300, null=True, blank=True)
    cart = models.JSONField(null=True, blank=True, default=dict)
    pw = models.CharField(max_length=200, null=True, blank=True)
    is_member = models.BooleanField(default=False)
    membership= models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return str(self.user.id)

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    industry = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=1500, null=True, blank=True)
    def __str__(self):
        return str(self.user.id)

class Onboarding(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    url=models.JSONField(null=True, blank=True, default=dict)
    plan= models.CharField(max_length=200, null=True, blank=True)
    add_ons=models.JSONField(null=True, blank=True, default=dict)
    agree = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.id)

 
class Agent(models.Model):
    ip = models.CharField(primary_key=True, unique=True, max_length=250)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    browser=models.JSONField(null=True, blank=True, default=dict)
    # Accessing user agent's browser attributes
    # request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    # request.user_agent.browser.family  # returns 'Mobile Safari'
    # request.user_agent.browser.version  # returns (5, 1)
    # request.user_agent.browser.version_string   # returns '5.1'
    os=models.JSONField(null=True, blank=True, default=dict)
    geo=models.JSONField(null=True, blank=True, default=dict)
    # Operating System properties
    # request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    # request.user_agent.os.family  # returns 'iOS'
    # request.user_agent.os.version  # returns (5, 1)
    # request.user_agent.os.version_string  # returns '5.1'
    device_type=models.CharField(null=True, blank=True, max_length=50)
    # request.user_agent.is_mobile # returns True
    # request.user_agent.is_tablet # returns False
    # request.user_agent.is_touch_capable # returns True
    # request.user_agent.is_pc # returns False
    # request.user_agent.is_bot # returns False
    device=models.CharField(null=True, blank=True, max_length=50)
    # Device properties
    # request.user_agent.device  # returns Device(family='iPhone')
    # request.user_agent.device.family  # returns 'iPhone'
    src=models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.BigIntegerField(max_length=250, default=int(time.time()))