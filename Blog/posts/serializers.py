from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    title = serializers.CharField(
        required=True,
        max_length=500,
        error_messages={
            'required': 'title cannot be empty',
            'max_length': 'title cannot exceed 500 characters'
        }
    )
    body = serializers.CharField(
        required=True,
        error_messages={
            'required': 'the body cannot be empty'
        }
    )

    class Meta:
        model = Posts
        fields = ('slug', 'title',
                  'body',
                  'created_at')
