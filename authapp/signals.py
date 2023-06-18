from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import Group
from django.dispatch import receiver


@receiver(user_logged_in)
def added_user_in_group(sender, user, request, **kwargs):
    group_bride = Group.objects.get(name='bride')
    group_vendor = Group.objects.get(name='vendor')
    if user.is_authenticated and request.POST.get('is_bride') == 'true':
        user.is_bride = True
        user.save()
        group_vendor.user_set.remove(user)
        user.groups.add(group_bride)
    elif user.is_authenticated and (request.POST.get('is_bride') == 'false' or not request.POST.get('is_bride')):
        user.is_bride = False
        user.save()
        group_bride.user_set.remove(user)
        user.groups.add(group_vendor)
