from app.utils import send_telegram_message

from .serializers import (
  DemoRequestSerializer,
  PrivacyPolicySerializer,
  StatsSerializer, 
  ChartDataSerializer, 
  CardSerializer,
  PlanSerializer,
  ContactSerializer,
  TermsOfServiceSerializer,
  CookiePolicySerializer
  )
from .models import (
  ChartData,
  ContactInfo,
  DemoRequest, 
  Stats,
  Card, 
  Plan, 
  PlanFeature,
  PrivacyPolicy,
  TermsOfService,
  CookiePolicy
)
from rest_framework import generics
from rest_framework.response import Response
from django.utils.timezone import localtime
from rest_framework.generics import ListAPIView, RetrieveAPIView


class DemoRequestCreateView(generics.CreateAPIView):
    queryset = DemoRequest.objects.all()
    serializer_class = DemoRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        formatted_time = localtime(instance.created_at).strftime('%Y-%m-%d | %H:%M:%S')
        
        message = f"""🆕 <b>New Demo Request!</b>

👤 <b>Name:</b> {instance.first_name} {instance.last_name}
📞 <b>Phone:</b> {instance.phone_number}
📝 <b>Description:</b> <i>{instance.description}</i>
📅 <b>Requested At:</b> {formatted_time} (uz)"""
        send_telegram_message(message)


class StatsView(ListAPIView):
    serializer_class = StatsSerializer

    def get_queryset(self):
        return Stats.objects.filter(is_active=True).order_by('order')
    
class ChartDataListView(generics.ListAPIView):
    queryset = ChartData.objects.all()
    serializer_class = ChartDataSerializer


class FeaturesView(ListAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(section='features', is_active=True).order_by('order')


class HowItWorksView(ListAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(section='how', is_active=True).order_by('order')


class PlansView(ListAPIView):
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.filter(is_active=True).order_by('order')


class ContactView(RetrieveAPIView):
    serializer_class = ContactSerializer

    def get_object(self):
        obj = ContactInfo.objects.first()
        if not obj:
            raise Exception("Contact info not found")  # minimal change
        return obj


class PrivacyPolicyView(RetrieveAPIView):
    serializer_class = PrivacyPolicySerializer

    def get_object(self):
        obj = PrivacyPolicy.objects.first()
        if not obj:
            raise Exception("Privacy policy not found")
        return obj


class TermsOfServiceView(RetrieveAPIView):
    serializer_class = TermsOfServiceSerializer

    def get_object(self):
        obj = TermsOfService.objects.first()
        if not obj:
            raise Exception("No terms found")
        return obj


class CookiePolicyView(RetrieveAPIView):
    serializer_class = CookiePolicySerializer

    def get_object(self):
        obj = CookiePolicy.objects.first()
        if not obj:
            raise Exception("No cookie policy found")
        return obj