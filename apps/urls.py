from django.urls import path
from . import views


urlpatterns = [
    path('technologies/', views.technologies, name='technologies'),
    path('service-categories/', views.Service_Categories, name='service_categories'),
    path('team-members/', views.GET_Team_Members, name='team_members'),
    path('journeys/', views.GET_Journeys, name='journeys'),
    path('why-choose-us/', views.GET_Why_Choose_Us, name='why_choose_us'),
    path('projects/', views.GET_Projects, name='projects'),
    path('progression-metrics/', views.GET_Our_Progress, name='progression_metrics'),
    path('write-message/', views.POST_Contact_Us_Message, name='write_message'),
    path('social-media/', views.Social_Media_Links, name='social_media')
]
