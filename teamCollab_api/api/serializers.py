from rest_framework import serializers
from .models import User, Project, ProjectMember, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']

class ProjectMemberSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    project = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'user', 'role']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ReadOnlyField(source='assigned_to.username')
    project = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    task = serializers.ReadOnlyField(source='task.title')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']