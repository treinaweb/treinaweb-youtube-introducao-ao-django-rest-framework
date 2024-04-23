from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Skill
from .serializers import SkillSerializer


class SkillListView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SkillDetailView(APIView):
    def get(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    def delete(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(skill, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
