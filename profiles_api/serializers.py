# keeping all the serializers in one file.
from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

# model serializer using meta class to configure the serializer to point to spcefic model in our project.
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    # This is meta class allowing serializer to point to profile model.
    class Meta:
        model = models.UserProfile
        # Specifying a list of fields in our model where we want to manage though serializer.
        # Defining list of fields in fields object
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and resturn a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwagrs = {'user_profile': {'read_only': True}}
