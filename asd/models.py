from django.db import models

# Create your models here.
class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="User's external id",
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Username",
    )
    def __str__(self):
        return f'#{self.external_id} {self.name}'
    class Meta:    
        verbose_name ="Profile"
        verbose_name_plural ="Profile"

class Message(models.Model):
    profile = models.ForeignKey(
        to='asd.Profile',
        verbose_name='Profile',
        on_delete=models.PROTECT,
    )        
    text = models.TextField(
        verbose_name='Text',
    )
    created_at = models.DateTimeField(
        verbose_name='time taken',
        auto_now_add=True,
    )
    def __str__(self):
        return f'Message {self.pk} from {self.profile}'
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Message'
