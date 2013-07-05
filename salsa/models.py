
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
        return dict(
            (pf.name, pf.fragment)
            for pf in self.pagefragment_set.all()
        )


class PageFragment(models.Model):
    page = TreeForeignKey('Page')
    fragment = models.ForeignKey('Fragment')
    slot = models.SlugField(max_length=64)


class Fragment(PolymorphicModel):
    '''Base class for all Fragments'''
    label = models.CharField(max_length=100,
        help_text='Helps you remember what this is for.'
    )

    def handle_request(self, request):
        '''Hook to allow fragments to process request data'''
        pass

