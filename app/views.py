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

class DemoRequestCreateView(generics.CreateAPIView):
    queryset = DemoRequest.objects.all()
    serializer_class = DemoRequestSerializer


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