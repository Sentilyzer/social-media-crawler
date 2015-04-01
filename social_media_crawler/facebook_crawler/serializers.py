from __future__ import absolute_import
from rest_framework import serializers
from .models import Post


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PostSerializer(serializers.ModelSerializer):
    replies = RecursiveField(many=True, required=False)

    class Meta:
        model = Post
        fields = ('date', 'name', 'text', 'likes', 'shares', 'replies')
