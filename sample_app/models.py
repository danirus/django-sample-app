from django.db import models
from sample_app.utils import evaluate


class Expression(models.Model):
    varname = models.CharField(primary_key=True, max_length=1)
    original = models.CharField(max_length=256)
    timestamp = models.DateTimeField('operation timestamp')
    
    def __unicode__(self):
        return "expr %d: %s" % (self.id, self.original)

    @property
    def result(self):
        return evaluate(self.original)
    
