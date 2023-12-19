from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
Utilisateur = get_user_model()

class Message(models.Model):
    texte = models.TextField(blank=False, max_length=2000)
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    util = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)

    def __str__(self):
        return self.texte[:100]


class Chat(models.Model):
    util_1 = models.OneToOneField(Utilisateur, to_field='id', on_delete=models.CASCADE, related_name="chat_util_1")
    util_2 = models.OneToOneField(Utilisateur, to_field='id', on_delete=models.CASCADE, related_name="chat_util_2")
   
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['util_1', 'util_2'], name="%(app_label)s_%(class)s_unique")
        ]

    def __str__(self):
        return f"{self.util_1} - {self.util_2}"
    
    def get_messages(self):
        return Message.objects.filter(chat=self)
    
