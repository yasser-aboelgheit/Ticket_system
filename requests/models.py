from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse
class Request(models.Model):
    STATUS_CHOICES = (
        ('assigned', 'Assigned'),
        ('not-assigned', 'NotAssigned'),
        ('closed',"Closed")
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'is_staff': False})
    title =  models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title',unique=True,null=True)
    issue =  models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default="not-assigned")
    employee = models.ForeignKey(User, limit_choices_to={'is_staff': True,'is_superuser': False}, on_delete=models.CASCADE, null=True, blank=True, related_name='employee')
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False) 


    def snippet(self):
        return self.issue[:50]+'...'

    def get_absolute_url(self):
        return reverse('request_single', kwargs={'slug': self.slug})


    def __str__(self):
        return '%s owned by %s' % (self.title, self.owner)

    def save(self, *args, **kwargs):
        if self.is_closed==True:
            self.status="closed"
        elif self.employee:
            self.status="assigned"  
        else:
            self.status='not-assigned'
        super().save(*args, **kwargs)
    
    class Meta:
        order_with_respect_to = 'is_closed'