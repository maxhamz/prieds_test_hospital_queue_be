from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from visitors.models import Visitor
from visitors.serializers import VisitorSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def visitor_list(request, format=None):
    if (request.method == 'GET'):
        visitors = Visitor.objects.all()
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data)

    if(request.method == 'POST'):
        serializer = VisitorSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def visitor_detail(request, pk, format=None):
    try:
        visitor = Visitor.objects.get(pk=pk)
    except Visitor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VisitorSerializer(visitor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VisitorSerializer(visitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        visitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
