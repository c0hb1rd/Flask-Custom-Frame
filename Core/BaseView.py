from flask import request, jsonify
from flask.views import View

from Config import GAP
from Helper.AuthHelper import loginRequired
from Helper.StatusHelper import errorPage


class BaseView(View):
    request = request
    methods = GAP

    def dispatch_request(self, *args, **kwargs):
        METHOD_META = {
            'GET': self.get,
            'POST': self.post
        }
        if request.method in self.methods:
            return METHOD_META[request.method]()
        else:
            return errorPage(title="非法请求", msg="不接受的请求方式")

    def get(self):
        return jsonify({'status': 1})

    def post(self):
        return jsonify({'status': 1})


class RequireLoginView(BaseView):
    
    @loginRequired
    def dispatch_request(self, *args, **kwargs):
        return super(RequireLoginView, self).dispatch_request(*args, **kwargs)

