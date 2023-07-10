from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello():
        return f'Hello {__name__}'

@bp.route('/wooyoon')
def hello_wooyoon():
    return f'Hello wooyoon'
