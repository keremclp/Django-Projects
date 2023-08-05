from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    is_student = models.BooleanField('Is student', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_parent = models.BooleanField('Is parent', default=False)

    def clean(self):
        if self.is_student + self.is_teacher + self.is_parent != 1:
            raise ValidationError(_('A user can only be registered as a student, teacher, or parent.'))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
