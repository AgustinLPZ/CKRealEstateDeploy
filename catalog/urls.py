from django.urls import path
from . import views
from .views import LogoutViewGET, add_listing, agent_profile

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('properties/<int:property_id>/', views.detailed_property, name='detailed_property'),
    path('agent_detailed_property/<int:property_id>/', views.agent_detailed_property, name='agent_detailed_property'),
    path('listings/', views.listings, name='listings'),
    path('edit_listing/<int:listing_id>/', views.edit_listing, name='edit_listing'),
    path('discover/', views.discover, name='discover'),
    path('agent_home/', views.agent_home, name='agent_home'),
    path('agent_discover/', views.agent_discover, name='agent_discover'),
    path('agent_listings/', views.agent_listings, name='agent_listings'),
    path('agent_agent_profile/', views.agent_agent_profile, name='agent_agent_profile'),
    path('accounts/logout/', LogoutViewGET.as_view(), name='logout'),
    path('add_listing/', add_listing, name='add_listing'),
    path('agent_profile/', agent_profile, name='agent_profile'),


]

