import json


def validate_nodeinfos(nodeinfos):
    result = []

    for nodeinfo in nodeinfos:
        if validate_nodeinfo(nodeinfo):
            result.append(nodeinfo)

    return result


def validate_nodeinfo(nodeinfo):
    if 'location' in nodeinfo:
        if 'latitude' not in nodeinfo['location'] or 'longitude' not in nodeinfo['location']:
            return False

    if 'node_id' in nodeinfo:
        # Allow node_id from MAC without ":"
        # Allow node_id like "gw1"
        if re.search(r'[^a-zA-Z0-9]', nodeinfo['node_id']):
            return False
    else:
        # Reject if node_id is missing
        return False

    return True
