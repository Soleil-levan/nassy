from django.dispatch import receiver
from .models import Event, Message
from django.db.models.signals import pre_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from time import ctime
from django.core.signals import request_finished


@receiver(pre_save, sender=Event)
def broadcast_event_to_groups(sender, instance, **kwargs):
    print(ctime)
    # channel_layer = get_channel_layer()
    # group_uuid = str(instance.group.uuid)
    # event_message = str(instance)
    # async_to_sync(channel_layer.group_send)(group_uuid,
    #     {
    #     "type":"event_message",
    #     "message":event_message,
    #     "status":instance.type,
    #     "user":str(instance.user)
    #     }
    # )
