from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from features.models import FeatureEvent, MaterialisedFeature
from features.materialize import get_feature


def add_block(request, block_id):
    add_block_event = FeatureEvent(feature_id=1, event_fields={'type': 'add_block', 'block_id': block_id})
    add_block_event.save()
    return HttpResponse(status=201)


def remove_block(request, block_id):
    remove_block_event = FeatureEvent(feature_id=1, event_fields={'type': 'remove_block', 'block_id': block_id})
    remove_block_event.save()
    return HttpResponse(status=200)


ALLOWED_STATUSES = ('draft', 'active', 'promoted')


def change_status(request, new_status):
    if new_status not in ALLOWED_STATUSES:
        return HttpResponse(status=400)
    
    # cannot go directly from draft to promoted
    feature = get_feature()
    if feature['status'] == 'draft' and new_status == 'promoted':
        return HttpResponse(status=400)
    
    change_status_event = FeatureEvent(feature_id=1, event_fields={'type': 'change_status', 'status': new_status})
    change_status_event.save()
    return HttpResponse(status=200)


def view_feature(request):
    feature = get_feature()
    
    feature_events = FeatureEvent.objects.filter(feature_id=1).all()
    feature['events'] = [feature_event.event_fields for feature_event in feature_events]
    
    return JsonResponse(data=feature)


def read_feature(request):
    materialized_feature = MaterialisedFeature.objects.get(id=1)
    return JsonResponse(data=materialized_feature.feature_body)
