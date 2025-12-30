from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serilizer
from . import models

# Create your views here.

""" TECH STACK VIEWS """

@api_view(['GET'])
def technologies(request):
    technologies = models.Technologies.objects.all()
    data = serilizer.TechnologiesSerializer(technologies, many=True).data
    return Response(data)

@api_view(['GET'])
def GET_Compleated_Projects(request):
    projects = models.Projects.objects.all()
    data = serilizer.ProjectsSerializer(projects, many=True).data
    return Response(data)

@api_view(['GET'])
def Service_Categories(request):
    service_categories = models.Service_Categories.objects.all()
    data = serilizer.ServiceCategoriesSerializer(service_categories, many=True).data
    return Response(data)

@api_view(['GET'])
def GET_Team_Members(request):
    team_members = models.TeamMembers.objects.all()
    data = serilizer.TeamMembersSerializer(team_members, many=True).data
    return Response(data)

@api_view(['GET'])
def GET_Journeys(request):
    journeys = models.Journeys.objects.all()
    data = serilizer.JourneysSerializer(journeys, many=True).data
    return Response(data)


""" WHY CHOOSE US VIEWS"""

@api_view(['GET'])
def GET_Why_Choose_Us(request):
    why_choose_us = models.WhyChooseUs.objects.all()
    data = serilizer.WhyChooseUsSerializer(why_choose_us, many=True).data
    return Response(data)

"""PROJECTS VIEWS"""

@api_view(['GET'])
def GET_Projects(request):
    projects = models.Projects.objects.all()
    data = serilizer.ProjectsSerializer(projects, many=True).data
    for i in data:
        technologies_ids = i['Technologies']
        technologies = models.Technologies.objects.filter(id__in=technologies_ids)
        i['Technologies'] = serilizer.TechnologiesSerializer(technologies, many=True).data
    return Response(data)

""" OUR Progress VIEWS"""
@api_view(['GET'])
def GET_Our_Progress(request):
    progression_metrics = models.ProgressionMetrics.objects.all()
    data = serilizer.ProrgressionMetricsSerializer(progression_metrics, many=True).data
    return Response(data)


""" MESSAGE VIEWS """

@api_view(['POST'])
def POST_Contact_Us_Message(request):
    serializer = serilizer.MessagesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Message sent successfully'}, status=201)
    return Response(serializer.errors, status=400) 

@api_view(['GET'])
def GET_Contact_Us_Messages(request):
    """ GET MESSAGES """
    messages = models.Messages.objects.all()
    data = serilizer.MessagesSerializer(messages, many=True).data
    return Response(data)

@api_view(['GET'])
def Social_Media_Links(request):
    social_media_links = models.SocialMediaLinks.objects.all()
    data = serilizer.SocialMediaLinksSerializer(social_media_links, many=True).data
    return Response(data)