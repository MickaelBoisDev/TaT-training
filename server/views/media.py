from PIL import Image
# import ffmpeg
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from rest_framework import status
from ..models.media import Media
from ..serializers.media_serializer import MediaSerializer
import os
from django.http import FileResponse, HttpResponseNotFound


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all().order_by('-conversion_date')
    serializer_class = MediaSerializer


def download_original(request):
    media_id = request.GET.get('media_id')
    try:
        media = Media.objects.get(pk=media_id)
        image_path = os.path.join(
            settings.MEDIA_ROOT, media.original_image.name)
        print(" PATHHHHH : ", image_path)
        return download_file(image_path)
    except Media.DoesNotExist:
        return HttpResponseNotFound("Média non trouvé.")


def download_converted(request):
    media_id = request.GET.get('media_id')
    try:
        media = Media.objects.get(pk=media_id)
        image_path = os.path.join(
            settings.MEDIA_ROOT, media.converted_image.name)
        print(" PATHHHHH : ", image_path)
        return download_file(image_path)
    except Media.DoesNotExist:
        return HttpResponseNotFound("Média non trouvé.")


def download_file(file_path):
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(
            file_path)
        return response
    else:
        return HttpResponseNotFound("Fichier non trouvé.")


def upload_and_convert(request):
    if request.method == 'POST':
        # Récupération de l'image
        image = request.FILES['image']
        image_name = image.name

        # To do
        # name = request.POST.get('name', 'Inconnu')

        # Sauvegarde l'image originale dans le dossier `media/`
        original_path = os.path.join(settings.MEDIA_ROOT, 'media', image.name)
        with open(original_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        # Détermine le format de conversion
        # Si l'image est en .jpg, nous voulons la convertir en .png et vice versa
        convert_to = 'PNG' if image.name.lower().endswith('.jpg') else 'JPEG'

        # Ouverture de l'image
        img = Image.open(original_path)
        # Initialisez la variable extension
        extension = ''

        # Conversion de l'image selon le format souhaité
        if convert_to == 'JPEG':
            img = img.convert('RGB')
            extension = '.jpg'
        elif convert_to == 'PNG':
            img = img.convert('RGBA')
            extension = '.png'

        # Utilise directement la variable `extension` pour créer `new_name`
        new_name = os.path.splitext(image.name)[0] + extension

        # Créer le chemin pour la nouvelle image convertie
        converted_path = os.path.join(
            settings.MEDIA_ROOT, 'converted_media', new_name)

        # Sauvegarde l'image convertie
        img.save(converted_path, convert_to)

        # Sauvegarde les chemins dans le modèle Media
        media = Media(original_image=os.path.join('media', image_name),
                      converted_image=os.path.join(
                          'converted_media', new_name),
                      conversion_type=convert_to)

        media.name = image_name.split(".")[0]
        media.save()
        serializer = MediaSerializer(media)
        return JsonResponse({'message': 'Image uploaded and converted successfully.',
                             'media': serializer.data})

    return JsonResponse({'error': 'Invalid method.'})


def delete_media(request, media_id):
    try:
        media = Media.objects.get(pk=media_id)
        media.delete()
        return JsonResponse({'message': 'Supprimé avec succès.'}, status=200)
    except Media.DoesNotExist:
        return JsonResponse({'error': 'Media non trouvé.'}, status=404)


def delete_all_medias(request):
    if request.method == 'DELETE':
        Media.objects.all().delete()
        return JsonResponse({'message': 'Tous les médias ont été supprimés.'}, status=200)
    return JsonResponse({'error': 'Méthode non valide.'}, status=400)
