from rest_framework.parsers import BaseParser

# 自定义解析方法
class P1902Parser(BaseParser):
    media_type = "text/p1902"
    def parse(self, stream, media_type=None, parser_context=None):
        data_dict={}
        data=stream.read().decode("utf-8")
        for keyval in data.split(","):
            key,val=keyval.split("=")
            data_dict[key]=val

        return data_dict



