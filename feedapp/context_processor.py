from feedapp.models import Image

def image_list(request):

    image = Image.objects.all()

    return {
        'images': image,
    }
