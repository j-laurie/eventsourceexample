from django.db.models.signals import post_save
from django.dispatch import receiver

from features.models import FeatureEvent, MaterialisedFeature
from features.materialize import get_feature


@receiver(post_save, sender=FeatureEvent)
def on_new_event(sender, instance, created, **kwargs):
    feature = get_feature()
    materialized_feature = MaterialisedFeature(id=instance.feature_id, feature_body=feature)
    materialized_feature.save()
