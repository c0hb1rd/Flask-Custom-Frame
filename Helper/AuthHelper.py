import hashlib
from functools import wraps

from flask import redirect
from flask import session
from flask import url_for

from Config import SEC_KEY


def loginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('authSession.login', returnUrl="/"))
        return f(*args, **kwargs)
    return decorated_function


def addSalt(obj):
    return SEC_KEY + obj + SEC_KEY[::-1]


def getMd5(obj):
    m = hashlib.md5()
    m.update(obj.encode('utf-8'))
    return m.hexdigest()
