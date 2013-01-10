from django.http import HttpResponse
from django.utils import simplejson
from decimal import Decimal
import datetime


class BetterJSONEncoder(simplejson.JSONEncoder):
    """JSON encoder which understands decimals, dates, and __json__"""

    def default(self, obj):
        '''Convert object to JSON encodable type.'''
        if hasattr(obj, '__json__'):
            return obj.__json__()
        if isinstance(obj, Decimal):
            return "%d" % obj
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return simplejson.JSONEncoder.default(self, obj)


class APIError(Exception):
    def __init__(self, code, errors, *args, **kwargs):
        self.code = code
        self.errors = errors
        super(APIError, self).__init__(*args, **kwargs)


def return_error(code, errors):
    resp = HttpResponse(simplejson.dumps(errors),
            mimetype="application/json")
    resp.status_code = code
    return resp


def jsonapi(**decor_kwargs):
    def fnc(fn):
        def to_json(request, *args, **kwargs):

            # check allowed methods if set
            allowed_methods = decor_kwargs.get("allowed_methods", ["POST", "GET", "PUT", "DELETE"])
            if request.method.lower() not in [ am.lower() for am in allowed_methods ]:
                return return_error(403, "Method %s not allowed" % request.method)

            # check for APIErrors
            try:
                context_data = fn(request, *args, **kwargs)
            except APIError, apie:
                return return_error(apie.code, apie.errors)

            # return JSON if a dict is returned, else return an httpresponse
            if isinstance(context_data, HttpResponse):
                return context_data
            resp = HttpResponse(simplejson.dumps(context_data, cls=BetterJSONEncoder),
                    mimetype='application/json')
            resp.status_code = { "POST" : 201, "GET" : 200, "DELETE" : 204, "PUT" : 201 }[request.method]

            return resp

        return to_json
    return fnc
