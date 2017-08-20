from django.db import models

class History(models.Model):
    date = models.DateField('Date visited')
    url = models.CharField(max_length=2048)
    title = models.CharField(max_length=1024)
    time = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "[{0}, {1}, {2}, {3}]".format(self.date, self.url, self.title, self.time)
