# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from djangocms_accordion.models import Accordion, AccordionEntry


class AccordionPlugin(CMSPluginBase):
    model = Accordion
    name = _('Accordion')
    module = _('Accordion')
    render_template = 'djangocms_accordion/accordion.html'
    allow_children = True
    child_classes = ['AccordionEntryPlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'accordion': instance,
            'placeholder': placeholder,
        })
        return context


class AccordionEntryPlugin(CMSPluginBase):
    model = AccordionEntry
    name = _('Accordion Entry')
    module = _('Accordion')
    render_template = 'djangocms_accordion/accordion_entry.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(AccordionPlugin)
plugin_pool.register_plugin(AccordionEntryPlugin)
