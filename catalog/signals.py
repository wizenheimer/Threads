from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry
from .models import Product


@receiver(post_save, sender=Product)
def update_document(sender, instance, **kwargs):
    instances = Product.objects.filter(is_active=True)
    for _instance in instances:
        registry.update(_instance)


@receiver(post_delete, sender=Product)
def delete_document(sender, instance, **kwargs):
    instances = Product.objects.filter(is_active=True)
    for _instance in instances:
        registry.update(_instance)
