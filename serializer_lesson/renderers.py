from rest_framework.renderers import BaseRenderer


class P1902Renderer(BaseRenderer):
    media_type = "text/p1902"
    format = "p1902"
    charset = "iso-8859-1"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        returned_data=[]
        if isinstance(data,list):
            for user in data:
                for key,value in user.items():
                    returned_data.append("{}={}".format(key,value))
        elif isinstance(data,dict):
            for key,value in data.items():
                returned_data.append("{}={}".format(key,value))

        return ":".join(returned_data).encode(self.charset)




