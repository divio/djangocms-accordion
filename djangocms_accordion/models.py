from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Accordion(CMSPlugin):
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)

    def __unicode__(self):
        return _(u"%s columns") % self.cmsplugin_set.all().count()


class AccordionEntry(CMSPlugin):
    title = models.CharField(_('title'), max_length=200, default='')
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)

    def __unicode__(self):
        return self.title

