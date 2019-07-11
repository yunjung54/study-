from django.db import models

# Create your models here.
#블로그 형식 만든것
class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #100글자까지만 출력해라