from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def get_data(request):
    limit = int(request.GET.get('limit', 10))
    offset = int(request.GET.get('offset', 0))
    students = Student.objects.all()[offset:offset+limit]
    serializer = StudentSerializer(students, many=True)
    data = {f'student{i+1}': student for i, student in enumerate(serializer.data)}
    response = {'success': True, 'message': 'List of students', 'response': data}
    return Response(response)
