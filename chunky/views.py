from models import Chunk
from . import decorators


def user_test(user):
    return user.is_superuser

@decorators.jsonapi(allowed_methods=["POST"])
def edit_api(request):
    if not request.user.is_superuser:
        raise decorators.APIError(403, "Only logged in superusers can do this. Please log in.")
    try:
        chunk, created = Chunk.objects.get_or_create(slug=request.POST["slug"])
        chunk.content = request.POST["content"]
        chunk.save()
        return { "success": True }
    except Exception, e:
        raise decorators.APIError(500, str(e))
