from django.db import models
from ckeditor.fields import RichTextField


class List(models.Model):
    email_list = models.CharField(max_length=25)

    def __str__(self):
        return self.email_list
    
    def count_emails(self):
        count = Subscriber.objects.filter(email_list=self).count()
        return count
    

class Subscriber(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.email_address
    

class Email(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = RichTextField()
    attachment = models.FileField(upload_to='email_attachments/', blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    def open_rate(self):
        total_sent = self.email_list.count_emails()
        opened_count = EmailTracking.objects.filter(email=self, opened_at__isnull=False).count()
        # Formula
        open_rate = (opened_count/total_sent) * 100 if total_sent > 0 else 0
        return round(open_rate, 2)
    
    def click_rate(self):
        total_sent = self.email_list.count_emails()
        opened_count = EmailTracking.objects.filter(email=self, opened_at__isnull=False).count()
        if opened_count > 0:
            clicked_count = EmailTracking.objects.filter(email=self, clicked_at__isnull=False).count()
            # Formula
            click_rate = (clicked_count/opened_count) * 100 if total_sent > 0 else 0
        else:
            click_rate = 0
        return round(click_rate, 2)
    

class Sent(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True, blank=True)
    total_sent = models.IntegerField()

    def __str__(self):
        return str(self.email) + ' - ' + str(self.total_sent) + ' emails sent'     # email subject - 3 emails sent

    
class EmailTracking(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True, blank=True)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, null=True, blank=True)
    unique_id = models.CharField(max_length=255, unique=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    clicked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email.subject