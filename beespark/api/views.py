from unicodedata import name
from rest_framework.views import APIView
from .models import ReserveTable, Tables
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateTableSerializer, TableSerializer

# Create your views here.


class CreateTableView(APIView):
    serializer_class = CreateTableSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            tableof = serializer.data.get('tableof')
            reserved = serializer.data.get('reserved')
            table_qs = Tables.objects.filter(name=name)
            if table_qs.exists():
                nTable = table_qs[0]
                nTable.save(update_fields=['tableof', 'reserved'])
                return Response({'status': 'Table updated successfully'}, status=status.HTTP_200_OK)
            else:
                nTable = Tables(name=name, tableof=tableof,
                                reserved=reserved)
                nTable.save()
                return Response({'status': 'Table Successfully Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

# class CreateTable(APIView):
#     serializer_class = CreateTableSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request)
#         if serializer.is_valid():
#             table = serializer.data.get('table')
#             tableof = serializer.data.get('tableof')
#             reserved = serializer.data.get('reserved')
#             table_qs = Tables.objects.filter(table=table)
#             if table_qs.exists:
#                 Table = table_qs[0]
#                 Table.tableof = tableof
#                 Table.save(update_fields=['tableof'])
#                 return Response({'status':'Table already Exists but successfully updated'}, status=status.HTTP_403_FORBIDDEN)
#             else:
#                 Table = Tables(table=table, tableof=tableof, reserved=reserved)
#                 Table.save()
#                 return Response({'status':'Table Created SuccessFully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'status':'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)


class Reservetableview(APIView):
    serializer_class = TableSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            table = serializer.data.get('table')
            name = serializer.data.get('name')
            arrival = serializer.data.get('arrival')
            table_qs = ReserveTable.objects.filter(
                table__name=table, table__reserved=False)
            if table_qs.exists():
                Table = table_qs[0]
                Table = ReserveTable(table__reserved=True,
                                     name=name, arrival=arrival)
                Table.save(update_fields=[
                           'table__reserved', 'name', 'arrival'])
                return Response({'status': 'Table Reserved Successfully'}, status=status.HTTP_306_RESERVED)
            elif ReserveTable.objects.filter(table__name=table, table__reserved=True):
                return Response({'status': 'Table already Reserved'}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({'status': 'Table not Found, Try another Table'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'status': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
