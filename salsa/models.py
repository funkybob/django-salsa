
from django.db import models

from cte_tree.models import CTENode

from django_hstore import hstore

from salsa.utils import buffered_property

class Page(CTENode):
    path = models.SlugField(blank=True)

    attributes = hstore.DictionaryField(db_index=True)
    objects = hstore.Manager()

    @buffered_property
    def fragment(self):
        '''Yields a dict of the bound fragments on this page.'''
        # Get list of sub-classes and where their pre-fetch is saved
        sub_classes = dict(
            (rel.var_name, rel.get_cache_name())
            for rel in Fragment._meta.get_all_related_objects()
            if issubclass(rel.field.model, Fragment)
        )
        result = OrderedDict()
        # We want all fragments related to this Page, ordered by their fragment order
        qs = Fragment.objects.filter(pagefragment__page=self).order_by('pagefragment__order')
        # We need to also grab their name from the PageFragment
        qs = qs.extras(select={'name': 'salsa_pagefragment.slot'})
        # And finally, grab all the subclasses
        qs = qs.select_related(*sub_classes.keys())

        # Now, resolve each fragment into its sub-class
        for frag in qs:
            for name in sub_classes.itervalues():
                sfrag = frag.__dict__.get(name)
                if sfrag is not None:
                    break
            result[frag.name] = sfrag

        return result

    def __getitem__(self, name):
        '''Allow dict access to attributes'''
        return self.attributes[name]


class PageFragment(models.Model):
    page = TreeForeignKey('Page')
    fragment = models.ForeignKey('Fragment')
    slot = models.SlugField(max_length=64)
    order = models.PositiveIntegerField(default=0)


class Fragment(PolymorphicModel):
    '''Base class for all Fragments'''
    description = models.CharField(max_length=100,
        help_text='Helps you remember what this is for.'
    )


    def handle_request(self, request, page, name):
        '''Allow plugins to react to the request'''
        pass
