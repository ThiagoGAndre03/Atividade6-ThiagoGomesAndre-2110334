
from django.contrib import admin
from django.urls import path
from appdoTG import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.atividade1),
    path('stats/', views.list_stats, name="stats-list"),
    path('stats/create/', views.create_stats),
    path('teams/', views.list_teams, name="teams-list"),
    path('teams/create/', views.create_teams),
    path('stats/delete/<stats_id>', views.delete_stats),
    path('stats/edit/<stats_id>', views.edit_stats),
    path('teams/delete/<teams_id>', views.delete_teams),
    path('teams/edit/<teams_id>', views.edit_teams),


]


