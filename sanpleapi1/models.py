from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
# Create your models here.

class Student(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=30,default=' ',blank=True)
    code=models.TextField()
    linenos=models.CharField(default='False',max_length=100)
    languages=models.CharField(choices=LANGUAGE_CHOICES,default='python',max_length=100)
    style=models.CharField(choices=STYLE_CHOICES,default='friendly',max_length=100)

    class Meta:
        ordering=('created',)




