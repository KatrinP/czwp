from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title_pl = models.CharField(max_length=200, default=None)
    title_cz = models.CharField(max_length=200, default=None)
    text_pl = models.TextField(default=None)
    text_cz = models.TextField(default=None)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    cz_months = {
        1: "ledna",
        2: "unora",
        3: "brezna",
        4: "dubna",
        5: "kvetna",
        6: "cervna",
        7: "cervence",
        8: "srpna",
        9: "zari",
        10: "rijna",
        11: "listopadu",
        12: "prosince"
    }
    pl_months = {
        1: "stycznia",
        2: "lutego",
        3: "marca",
        4: "kwietnia",
        5: "maja",
        6: "czerwca",
        7: "lipca",
        8: "sierpnia",
        9: "wrznia",
        10: "padziernika",
        11: "listopada",
        12: "grudnia"
    }

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title_pl

    def get_pl_date(self):
        day = self.published_date.day
        month = self.pl_months[self.published_date.month]
        year = self.published_date.year
        return str(day) + ". " + month + " " + str(year)

    def get_cz_date(self):
        day = self.published_date.day
        month = self.cz_months[self.published_date.month]
        year = self.published_date.year
        return str(day) + ". " + month + " " + str(year)

