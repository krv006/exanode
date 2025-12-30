# serializers.py
from rest_framework import serializers
from . import models

class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technologies
        fields = ['id','image', 'technology', 'technology_description']
        
class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhyChooseUs
        fields = ['id','icon', 'title', 'description']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['id','image', 'Owner', 'Title', 'Description', 'Technologies', 'service_category', 'Link']

class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMembers
        fields = ['id','image', 'Name', 'Role', 'about', 'SocialLink']
        
class JourneysSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Journeys
        fields = ['id', 'Year', 'short_Description', 'Description']

class LeadershipTeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeadershipTeamMembers
        fields = ['id', 'team_member_id']

class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutCompany
        fields = ['id', 'company_name', 'description']

class AboutUsSerializer(serializers.Serializer):
    class Meta:
        technologies = TechnologiesSerializer(many=True)
        why_choose_us = WhyChooseUsSerializer(many=True)
        projects = ProjectsSerializer(many=True)
        team_members = TeamMembersSerializer(many=True)
        journeys = JourneysSerializer(many=True)
        leadership_team_members = LeadershipTeamMembersSerializer(many=True)
        about_company = AboutCompanySerializer()

class ServiceCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service_Categories
        fields = ['id', 'icon', 'Title', 'category_name', 'detail', 'Service_Options']

        
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Messages
        fields = ['id', 'Name', "Company", 'phone_number', 'Email', 'service', 'message']


class ProrgressionMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProgressionMetrics
        fields = ['id', 'title', 'description']
        
class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialMediaLinks
        fields = ['id', 'platform', 'url', 'icon']
