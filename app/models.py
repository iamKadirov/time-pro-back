from django.db import models


class DemoRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Card(models.Model):
    SECTIONS = [
        ('features', 'Features'),
        ('how', 'How it works'),
    ]
    section = models.CharField(max_length=20, choices=SECTIONS)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)

    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.section} - {self.title}"


class Stats(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    number = models.CharField(max_length=100, blank=False)
    percent = models.CharField(max_length=100, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class ChartData(models.Model):
    title = models.CharField(max_length=100, unique=True)
    chart_style = models.CharField(max_length=20)

    labels = models.JSONField(blank=True, default=list)
    values = models.JSONField(blank=True, default=list)

    updated_at = models.DateTimeField(auto_now=True)


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)

    description = models.TextField()
    icon = models.CharField(max_length=100)

    is_popular = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PlanFeature(models.Model):
    plan = models.ForeignKey(Plan, related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text
    

class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number_1 = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200)

    telegram_link = models.URLField(blank=True)

    def __str__(self):
        return self.email