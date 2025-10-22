from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import ImageItem
from .serializers import ImageItemSerializer
from .services import upload_to_cloudinary

import cloudinary.uploader

class ImageItemViewSet(viewsets.ModelViewSet):
    queryset = ImageItem.objects.all().order_by('-uploaded_at')
    serializer_class = ImageItemSerializer

    def create(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'Файл не найден'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            upload_result = upload_to_cloudinary(file)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        image = ImageItem.objects.create(
            title=request.data.get('title', ''),
            description=request.data.get('description', ''),
            image_url=upload_result['url'],
            cloudinary_public_id=upload_result['public_id']
        )

        serializer = self.get_serializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        cloudinary.uploader.destroy(instance.cloudinary_public_id)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)