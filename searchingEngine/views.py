from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DataView1(APIView):
    def get(self, request, *args, **kw):
        result = {'a': 'b'}
        return Response(result, status=status.HTTP_200_OK)


class DataView2(APIView):
    def get(self, request, *args, **kw):
        result = {'jebac': 'biede'}
        return Response(result, status=status.HTTP_200_OK)
