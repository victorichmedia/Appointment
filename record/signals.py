from django.db.models import signals
from django.dispatch import receiver
from record.models import CreateAppointment

@receiver(signals.post_save, sender=CreateAppointment)
def create_appointment(sender, instance, created, **kwargs):
  print("A new appointment is created")