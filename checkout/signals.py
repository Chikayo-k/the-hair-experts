from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total (update/create)
    """
    # instance.order.calc_total()
    instance.order.culc_total()

@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total (delete)
    """
    # instance.order.calc_total()
    instance.order.culc_total()