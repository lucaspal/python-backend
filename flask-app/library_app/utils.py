"""
Description: Util functions.
"""


def werkzeug_rule_endpoint(rule):
    tmp = []
    for is_dynamic, data in rule._trace:
        if is_dynamic:
            tmp.append(u"<%s>" % data)
        else:
            tmp.append(data)
    return repr((u"".join(tmp)).lstrip(u"|")).lstrip(u"u")
