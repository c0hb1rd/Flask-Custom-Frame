from flask import Blueprint

from Config import ROOT_PATH


class BaseBlueprint:
    def __init__(self, name):
        self.app = Blueprint(name, __name__, static_folder="static", template_folder="templates", root_path=ROOT_PATH)

    def addRule(self, url, viewObj, ruleName):
        self.app.add_url_rule(url, view_func=viewObj.as_view(ruleName))
