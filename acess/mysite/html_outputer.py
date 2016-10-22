# coding:utf-8
import django
django.setup()
from mycraw.models import Result

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect(self, data):
        if data is None:
            return
        else:
            self.datas.append(data)

    def output(self):
        for data in self.datas:
            Result.objects.create(title=data['title'], summary=data['summary'])
