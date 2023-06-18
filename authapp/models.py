from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.safestring import mark_safe


class User(AbstractUser):
    is_bride = models.BooleanField(verbose_name='Клиент или поставщик', default=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, verbose_name='Телефон',
                             null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'User {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ProfileVendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, null=True, blank=True)
    avatar = models.ImageField(verbose_name='Аватарка', upload_to='media/avatar', null=True, blank=True)
    city = models.CharField(verbose_name='Город работы', max_length=20)
    number_people = models.PositiveSmallIntegerField(verbose_name='Номер поставщика', null=True, blank=True)

    def avatar_preview_vendor(self):
        if self.avatar:
            return mark_safe('<img src="{url}" width="150"/>'.format(
                url=self.avatar.url
            ))

    def __str__(self):
        return f'Profile {self.user.first_name} {self.user.last_name} - {"bride/spouse" if self.user.is_bride else "vendor"}'

    @receiver(post_save, sender=User)
    def create_profile_client(sender, instance, created, **kwargs):
        if created:
            ProfileVendor.objects.create(user=instance)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class ProfileClient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, null=True, blank=True)
    avatar = models.ImageField(verbose_name='Аватарка', upload_to='media/avatar', null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=30)
    date_events = models.DateField(verbose_name='Дата ивента', null=True, blank=True, unique=True)
    number_people = models.PositiveSmallIntegerField(verbose_name='Номер клиента', null=True, blank=True)

    def avatar_preview_client(self):
        if self.avatar:
            return mark_safe('<img src="{url}" width="100"/>'.format(
                url=self.avatar.url
            ))

    def clean(self):
        if self.date_events < timezone.now().date():
            raise ValueError('The date of the event cannot be less than the current date')

    def __str__(self):
        return f'Profile {self.user.first_name} {self.user.last_name} - {"bride/spouse" if self.user.is_bride else "vendor"}'

    @receiver(post_save, sender=User)
    def create_profile_client(sender, instance, created, **kwargs):
        if created:
            ProfileClient.objects.create(user=instance)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class ImageProfileVendor(models.Model):
    image = models.ImageField(verbose_name='Изображение профиля поставщика', upload_to='profile_vendor')
    profile = models.ForeignKey(ProfileVendor, models.CASCADE, verbose_name='Изображение профиля', related_name='image')

    class Meta:
        verbose_name = 'Картинка поставщика'
        verbose_name_plural = 'Картинки поставщиков'


class ImageProfileBride(models.Model):
    image = models.ImageField(verbose_name='Изображение профиля клиента', upload_to='profile_bride')
    profile = models.ForeignKey(ProfileClient, models.CASCADE, verbose_name='Изображение профиля', related_name='image')

    class Meta:
        verbose_name = 'Картинка клиента'
        verbose_name_plural = 'Картинки клиентов'
