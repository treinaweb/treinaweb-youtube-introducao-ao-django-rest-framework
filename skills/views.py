from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Skill
from .serializers import SkillSerializer


class SkillListView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
