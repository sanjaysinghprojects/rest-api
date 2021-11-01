from .models import student
from .serializers import studentserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET','POST'])
def studentlist(request):
    if request.method == 'GET':
        model_instace= student.objects.all()
        serial_instance= studentserializer(model_instace,many=True)
        return Response(serial_instance.data)

    elif request.method == 'POST':
        s_instance=studentserializer(data=request.data)
        if s_instance.is_valid():
            s_instance.save()
            return Response(s_instance.data)
        return Response(s_instance.errors)

@api_view(['GET','PUT','DELETE'])
def studentdetail(request,pk):
    if request.method == 'GET':
        model_instace= student.objects.get(pk=pk)
        serial_instance= studentserializer(model_instace)
        return Response(serial_instance.data)

    elif request.method == 'PUT':
        model_instace = student.objects.get(pk=pk)
        s_instance = studentserializer(model_instace,data=request.data)
        if s_instance.is_valid():
            s_instance.save()
            return Response(s_instance.data)
        # return Response(s_instance.errors)

    elif request.method =='DELETE':
        model_instace = student.objects.get(pk=pk)

