from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    # ── Public pages ──────────────────────────────────────────
    path('',           views.home,      name='home'),
    path('about/',     views.about,     name='about'),
    path('skills/',    views.skills,    name='skills'),
    path('projects/',  views.projects,  name='projects'),
    path('education/', views.education, name='education'),
    path('contact/',   views.contact,   name='contact'),

    # ── Custom Admin Panel ─────────────────────────────────────
    path('portfolio-admin/',                        admin_views.admin_dashboard,      name='admin_dashboard'),
    path('portfolio-admin/profile/',                admin_views.admin_profile,        name='admin_profile'),

    path('portfolio-admin/skills/',                 admin_views.admin_skills,         name='admin_skills'),
    path('portfolio-admin/skills/add/',             admin_views.admin_skill_add,      name='admin_skill_add'),
    path('portfolio-admin/skills/<int:pk>/edit/',   admin_views.admin_skill_edit,     name='admin_skill_edit'),
    path('portfolio-admin/skills/<int:pk>/delete/', admin_views.admin_skill_delete,   name='admin_skill_delete'),

    path('portfolio-admin/projects/',                 admin_views.admin_projects,       name='admin_projects'),
    path('portfolio-admin/projects/add/',             admin_views.admin_project_add,    name='admin_project_add'),
    path('portfolio-admin/projects/<int:pk>/edit/',   admin_views.admin_project_edit,   name='admin_project_edit'),
    path('portfolio-admin/projects/<int:pk>/delete/', admin_views.admin_project_delete, name='admin_project_delete'),

    path('portfolio-admin/education/',                 admin_views.admin_education,       name='admin_education'),
    path('portfolio-admin/education/add/',             admin_views.admin_education_add,   name='admin_education_add'),
    path('portfolio-admin/education/<int:pk>/edit/',   admin_views.admin_education_edit,  name='admin_education_edit'),
    path('portfolio-admin/education/<int:pk>/delete/', admin_views.admin_education_delete,name='admin_education_delete'),

    path('portfolio-admin/messages/',                  admin_views.admin_messages,        name='admin_messages'),
    path('portfolio-admin/messages/<int:pk>/',         admin_views.admin_message_view,    name='admin_message_view'),
    path('portfolio-admin/messages/<int:pk>/delete/',  admin_views.admin_message_delete,  name='admin_message_delete'),
]