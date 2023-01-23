from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from registration.signals import user_registered
from django.contrib.auth.models import User

GROUPS = ['Менеджер', 'Разработчик', 'Администратор']
@receiver(post_save, sender=User)
def user(sender: User, instance: User, created: bool, **kwargs) -> None:
    """
    This receiver function will set every staff pages that is created to the group staff.

    :param sender: the model that will trigger this receiver
    :param instance: the instance
    :param created: if it was already created
    :param kwargs:
    :return: None
    """
    if created:
        group = Group.objects.get(name=GROUPS[instance.role])
        instance.groups.add(group)
    else:
        group = Group.objects.get(name=GROUPS[instance.role])
        instance.groups.add(group)
        print("update")

