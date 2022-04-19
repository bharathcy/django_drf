from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BlogSerializer, BothSerializer
from .utils import get


@api_view(['GET'])
def BlogList(request):
    data = get(request)
    return Response(data.values())


@api_view(['POST'])
def CreateAPI(request):
    item = BlogSerializer(data=request.data)
    print( item.is_valid(),item)
    if item.is_valid():
        item.save()
    return Response(item.data)
