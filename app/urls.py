from django.urls import path
from .views import ChartDataListCreateView, ContactView, DemoRequestCreateView, FeaturesView, HowItWorksView, PlansView, StatsView


urlpatterns = [
    path('demo-request/', DemoRequestCreateView.as_view(), name='demo-request'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('chart/', ChartDataListCreateView.as_view(), name='chart-data'),
    path('features/', FeaturesView.as_view(), name='features'),
    path('how/', HowItWorksView.as_view(), name='how-it-works'),
    path('pricing/', PlansView.as_view(), name='pricing'),
    path('contact/', ContactView.as_view(), name='contact'),  
]