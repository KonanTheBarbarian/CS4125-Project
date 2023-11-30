from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail  # Django's built-in function to send emails.

# The User model acts as the subject in the observer pattern.
# When a new User instance is created (its state changes), it will emit a post_save signal.
class User(models.Model):
    username = models.CharField(max_length=191)
    email = models.EmailField(unique=True, max_length=191)
    password = models.CharField(max_length=191)
    accountType = models.CharField(max_length=191)
    userID = models.CharField(max_length=191)

    class Meta:
        db_table = 'userB'


# The EmailNotificationObserver class functions as the observer.
# It defines the behavior (send_welcome_email) in response to the subject's state change.
class EmailNotificationObserver:
    @staticmethod
    def send_welcome_email(user):
        # This method sends an email, which is the observer's action upon the subject's state change.
        send_mail(
            'Welcome to Car Rental System',
            'Your account has been successfully created.',
            'no-reply@carrentalsystem.com',  # Replace with your actual email
            [user.email],
            fail_silently=False,
        )

# This receiver function connects the User model's post_save signal to the observer's action.
# When a User instance is created (the subject's state changes), this function is called,
# which in turn calls the observer's method to send the email.
@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        EmailNotificationObserver.send_welcome_email(instance)
