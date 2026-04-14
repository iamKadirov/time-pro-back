from rest_framework import serializers
from .models import Card, ChartData, ContactInfo, DemoRequest, Plan, PlanFeature, Stats
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

    def validate_phone_number(self, value):
        try:
            parsed = phonenumbers.parse(value, None)
            if not phonenumbers.is_valid_number(parsed):
                raise serializers.ValidationError("Invalid phone number.")
        except:
            raise serializers.ValidationError("Invalid phone number format.")
        
        return value
    


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

    def validate(self, data):
        labels = data.get('labels', [])
        values = data.get('values', [])

        if len(labels) != len(values):
            raise serializers.ValidationError("Labels and values must have the same length.")
        return data
    

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