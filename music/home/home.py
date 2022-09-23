from flask import Blueprint, render_template

import music.utilities.utilities as utilities


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():

    return render_template(
        'home/home.html',
        selected_tracks=utilities.get_top_tracks()
    )

