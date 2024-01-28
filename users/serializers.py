from django.contrib.auth.models import User
from orders.serializers import OrderSerializer, AddressSerializer
from users.models import ProcsUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = ProcsUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "phone_number",
            "image",
            "birthday",
            "addresses",
        ]
   

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input-type': 'password'}, write_only=True)

    class Meta:
        model = ProcsUser
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Error": "Passwords Does Not Match"})

        if ProcsUser.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email Already Exists"})

        account = ProcsUser(email=self.validated_data['email'])
        account.set_password(password)
        account.save()

        return account

