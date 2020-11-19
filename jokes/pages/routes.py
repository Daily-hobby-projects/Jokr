from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template
)

app_bp=Blueprint('app',__name__,template_folder='templates',static_url_path='/static')


@app_bp.route('/')
def index():
    return render_template('index.html')