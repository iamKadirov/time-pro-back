from app.utils import send_telegram_message

from .serializers import (
  DemoRequestSerializer,
  StatsSerializer, 
  ChartDataSerializer, 
  CardSerializer,
  PlanSerializer,
  ContactSerializer,
  )
from .models import (
  ChartData,
  ContactInfo,
  DemoRequest, 
  Stats,
  Card, 
  Plan, 
  PlanFeature,
)
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import localtime


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


class StatsView(APIView):
    def get(self, request):
        stats = Stats.objects.filter(is_active=True).order_by('order')
        serializer = StatsSerializer(stats, many=True)
        return Response(serializer.data)
    
class ChartDataListCreateView(generics.ListCreateAPIView):
    queryset = ChartData.objects.all()
    serializer_class = ChartDataSerializer


class FeaturesView(APIView):
    def get(self, request):
        features = Card.objects.filter(section='features', is_active=True).order_by('order')
        serializer = CardSerializer(features, many=True)
        return Response(serializer.data)

class HowItWorksView(APIView):
    def get(self, request):
        how_it_works = Card.objects.filter(section='how', is_active=True).order_by('order')
        serializer = CardSerializer(how_it_works, many=True)
        return Response(serializer.data)
    

class PlansView(APIView):
    def get(self, request):
        plans = Plan.objects.filter(is_active=True).order_by('order')
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)
    
class ContactView(APIView):
    def get(self, request):
        contact = ContactInfo.objects.first()
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    