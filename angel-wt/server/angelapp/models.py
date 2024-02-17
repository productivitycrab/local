from django.db import models
from django.utils.timezone import now

class Reminder(models.Model):
    SIT_STAND = 'sit_stand'
    FOOD = 'food'
    MEDICATION = 'medication'
    TOOTHBRUSH = 'toothbrush'
    UNCATEGORIZED = 'uncategorized'

    TYPE_CHOICES = [
        (SIT_STAND, 'Sit/Stand'),
        (FOOD, 'Food'),
        (MEDICATION, 'Medication'),
        (TOOTHBRUSH, 'Toothbrush'),
        (UNCATEGORIZED, 'Uncategorized'),
    ]
    
    reminder_type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=UNCATEGORIZED
    )

    reminder_date = models.DateField(null=True)

    # def generate_reminders():

    # def sync_reminders(): 

    # def snooze_reminder():


