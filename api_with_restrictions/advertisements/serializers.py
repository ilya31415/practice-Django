from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, attrs):

        list_satus_open = Advertisement.objects.filter(status='OPEN', creator=self.context["request"].user).count()

        if self.context['request'].method == 'POST':
            if list_satus_open >= 10:
                raise ValidationError('слишком много открыто объявлений')

        if self.context['request'].method == 'PATCH':
            if list_satus_open >= 10 and attrs.get('status') == 'OPEN':
                raise ValidationError('открыто слишком много объявлений')

        # TODO: добавьте требуемую валидацию

        return attrs
