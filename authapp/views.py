from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import ProfileVendor, ProfileClient
from .serializers import ProfileVendorModelSerializer, ProfileClientModelSerializer
from catalogapp.permissions import VendorPermission, BridePermission
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileClientView(APIView):
    serializer_class = ProfileClientModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, BridePermission]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ProfileClientModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_bride:
            obj = ProfileClient.objects.filter(user=self.request.user.pk)
            return obj

    def patch(self, request):
        queryset = self.get_queryset().first()
        serializer = ProfileClientModelSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileVendorView(APIView):
    serializer_class = ProfileVendorModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, VendorPermission]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ProfileVendorModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.user.is_authenticated and (
                self.request.user.is_bride is None or self.request.user.is_bride == False):
            queryset = ProfileVendor.objects.filter(user=self.request.user.pk)
            return queryset

    def patch(self, request):
        queryset = self.get_queryset().first()
        serializer = ProfileVendorModelSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://127.0.0.1:8000/api/auth/google/callback/"
