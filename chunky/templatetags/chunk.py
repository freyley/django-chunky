from django import template
from chunky.models import Chunk

register = template.Library()



@register.inclusion_tag('chunk_template.html', takes_context = True)
def chunk(context, slug):

    if not slug:
        raise Exception("""
        You have to have a slug in your 'chunk' tag.
        Note: {% chunk foo_bar %} is resolving 'foo_bar' as a variable.
        Normal usage is {% chunk "foo_bar" %}
        """)

    chunk, created = Chunk.objects.get_or_create(slug=slug)

    return {
        "content":chunk.content,
        "slug":chunk.slug,
    }

