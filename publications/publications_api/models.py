from django.db import models


class Publication(models.Model):
    author = models.ForeignKey('users_api.CustomUser',
                               related_name='publications',
                               on_delete=models.CASCADE)
    text = models.TextField()
    is_public = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
