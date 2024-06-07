from django.db import models


class FeatureEvent(models.Model):
    event_fields = models.JSONField()
    feature_id = models.IntegerField()


class MaterialisedFeature(models.Model):
    id = models.IntegerField(primary_key=True)
    feature_body = models.JSONField()

from features.signals import *
