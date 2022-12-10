from .models import  Artist, Playlist, Profile, Resent, Songs
from django.contrib.auth.models import User
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("gender", "image", "age",)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "profile",
        )
        extra_kwargs = {"id": {"read_only": True},}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile")
        profile = instance.profile
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.set_password(validated_data.get("password"))
        profile.birth_date = profile_data.get("birth_date", profile.birth_date)
        profile.gender = profile_data.get("gender", profile.gender)
        profile.image = profile_data.get("image", profile.image)
        profile.age = profile_data.get("age", profile.age)
        instance.save()
        profile.save()
        return instance

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ( "name","image","DOB","language")

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "image", "song","language","artist")

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("user", "song","playlist_name")
        read_only_fields = ("user",)

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("user", "song",)
        read_only_fields = ("user",)
        
class ResentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resent
        fields = ("user", "song",)
        read_only_fields = ("user",)