# coding: utf-8
from django.db import models


class Result(models.Model):
    title = models.TextField()
    summary = models.TextField()
    def __unicode__(self):
        return u'%s %s'%(self.title, self.summary)
