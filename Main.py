from flask import Flask
from jinja2 import filters


from Config import (
    SER_HOST,
    SER_PORT,
    THREADED,
    DEBUG)

from Helper.StatusHelper import StatusHelper
from Helper.TimeHelper import TimeHelper


app = Flask(__name__)
app.config.from_object("Config")

'''
    :argument (Blueprint Name)
    app.register_blueprint(name)
'''


filters.FILTERS['formatTime'] = TimeHelper.formatTime


@app.errorhandler(404)
def pageNotFound(e):
    return StatusHelper.errorPage(title="页面未找到", msg="页面未找到")


@app.errorhandler(400)
def webError(e):
    return StatusHelper.errorPage(title="异常", msg="服务端异常")


if __name__ == '__main__':
    app.debug = DEBUG
    app.run(host=SER_HOST, port=SER_PORT, threaded=THREADED)
