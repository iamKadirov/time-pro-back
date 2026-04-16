from modeltranslation.translator import translator, TranslationOptions
from .models import (
  Stats,
  Card, 
  Plan, 
  PlanFeature,
  PrivacyPolicy,
  TermsOfService,
  CookiePolicy
)
class PlanTranslationOptions(TranslationOptions):
    fields = ('name', 'price', 'description')

class PlanFeatureTranslationOptions(TranslationOptions):
    fields = ('text',)

class CardTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class StatsTranslationOptions(TranslationOptions):
    fields = ('title', 'percent')

class PrivacyPolicyTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class TermsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class CookieTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(PrivacyPolicy, PrivacyPolicyTranslationOptions)
translator.register(TermsOfService, TermsTranslationOptions)
translator.register(CookiePolicy, CookieTranslationOptions)
translator.register(Stats, StatsTranslationOptions)
translator.register(Card, CardTranslationOptions)
translator.register(Plan, PlanTranslationOptions)
translator.register(PlanFeature, PlanFeatureTranslationOptions)