
from flask import Blueprint, request, render_template
view2 = Blueprint('view2', __name__)

@view2.route('/hello/')
def view2_index2():
    return "Hello there from view 2!"