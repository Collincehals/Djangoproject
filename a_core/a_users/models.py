from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profilepics/', blank=True, null=True, default='profilepics/default.png')
    realname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def delete(self, *args, **kwargs):
        self.user.delete()
        super(Profile, self).delete(*args, **kwargs)
        
        
    def __str__(self):
        return str(self.user)