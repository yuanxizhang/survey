from django.conf import settings
from django.db import models
from django.utils import timezone

class Survey(models.Model):
     
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    # surveys will be sorted using published_date, created_date
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    last_udpated_on = models.DateTimeField(auto_now=True)
    # to delete a survey, we will simply set is_active to False
    is_active = models.BooleanField(default=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    choice = models.CharField(max_length=255, null=False, blank=False)  
    def __str__(self):
        return self.choice