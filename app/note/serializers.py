"""
Serializer for note APIs.
"""

from rest_framework import serializers

from core.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Seralier for notes."""

    class Meta:
        model = Note
        fields = ["id", "title", "created_at", "updated_at"]

        read_only_fields = ["id", "created_at"]


class NoteDetailSerializer(NoteSerializer):
    """Serializer for note detail view."""

    class Meta(NoteSerializer.Meta):
        fields = NoteSerializer.Meta.fields + ["content"]
