
from django import template

register = template.Library()

class SlotNode(template.Node):
    def __init__(self, name, template_name=None, kwargs):
        self.name = name
        self.template_name = template_name
        self.kwargs = kwargs

    def render(self, context):
        # XXX
        return ''

@register.tag
def slot(parser, token):
    bits = token.split_contents()
    slot_name = bits[1]
    kwargs = token_kwargs(bits, parser)

    return SlotNode(slot_name, **kwargs)

