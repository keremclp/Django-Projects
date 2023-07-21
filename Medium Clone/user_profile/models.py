from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar')
    instagram = models.CharField(max_length=200)
    # slug = AutoSlugField(blank=True)
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse(
            "read:all_posts_view",
            kwargs={
                "user_slug": self.slug,
            },
        )

