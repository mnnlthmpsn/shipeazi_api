from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/create_move_category', methods=['POST'])
def create_move_category():
    pass
