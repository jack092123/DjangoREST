from rest_framework import serializers
from rest_api.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ('id', 'task', 'status', 'priority', 'due_date', 'note', 'last_modify', 'create_time')
