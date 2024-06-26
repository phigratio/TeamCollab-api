from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-members', ProjectMemberViewSet)

# Create a nested router for tasks within projects
projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'tasks', TaskViewSet, basename='project-tasks')

# Create a nested router for comments within tasks
tasks_router = routers.NestedSimpleRouter(projects_router, r'tasks', lookup='task')
tasks_router.register(r'comments', CommentViewSet, basename='task-comments')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(tasks_router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Add custom action URLs
urlpatterns += [
    path('api/users/register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('api/users/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
]