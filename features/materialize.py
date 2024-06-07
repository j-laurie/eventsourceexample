from features.models import FeatureEvent

def get_feature():
    feature = {'feature_id': 1, 'blocks': set(), 'status': 'draft'}

    feature_events = FeatureEvent.objects.filter(feature_id=1).all()

    for feature_event in feature_events:
        event_fields = feature_event.event_fields
        if event_fields['type'] == 'add_block':
            block_id = event_fields['block_id']
            feature['blocks'].add(block_id)
        elif event_fields['type'] == 'remove_block':
            block_id = event_fields['block_id']
            if block_id in feature['blocks']:
                feature['blocks'].remove(block_id)
        elif event_fields['type'] == 'change_status':
            feature['status'] = event_fields['status']

    feature['blocks'] = list(feature['blocks'])
    return feature
