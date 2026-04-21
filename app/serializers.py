from rest_framework import serializers
from .models import (
  Card, 
  ChartData, 
  ContactInfo, 
  DemoRequest, 
  Plan, 
  PlanFeature, 
  Stats, 
  PrivacyPolicy, 
  TermsOfService,
  CookiePolicy
)
import phonenumbers

class DemoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoRequest
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'description',
        ]

    # def validate_phone_number(self, value):
    #     try:
    #         parsed = phonenumbers.parse(value, None)
    #         if not phonenumbers.is_valid_number(parsed):
    #             raise serializers.ValidationError("Invalid phone number.")
    #     except:
    #         raise serializers.ValidationError("Invalid phone number format.")
        
    #     return value
    


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = [
            'title',
            'icon',
            'number',
            'percent',
        ]


class ChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartData
        fields = [
            'title',
            'chart_style',
            'labels',
            'values',
        ]    

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'title',
            'description',
            'icon',
        ]


class PlanFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanFeature
        fields = [
            'text',
        ] 

class PlanSerializer(serializers.ModelSerializer):
    features = PlanFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = [
            'name',
            'price',
            'description',
            'icon',
            'is_popular',
            'features',
        ]
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            'email',
            'phone_number_1',
            'phone_number_2',
            'address',
            'telegram_link'
        ]


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = [
            'title',
            'content',
        ]

class TermsOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsOfService
        fields = [
            'title',
            'content',
        ]

class CookiePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CookiePolicy
        fields = ['title', 'content']
        