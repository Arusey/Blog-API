import json
from rest_framework import renderers


class PostJSONRenderer(renderers.BaseRenderer):
    """Renders a post into a list or single article"""
    media_type = 'application/json'
    format = 'json'
    charset = 'utf-8'

    def render(self, data, valid_media_type=None, renderer_context=None):
        "render a list of articles"
        if isinstance(data, list):
            return json.dumps({'articles': data})

        else:
            """renders a single article"""
            error = data.get('detail')
            if error:
                return json.dumps({'message': data})
            return json.dumps({'article': data})
