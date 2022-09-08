"""Initialize Flask app."""

from pathlib import Path
import os
from flask import Flask

import music.adapters.repository as repo
from music.adapters.csvdatareader import TrackCSVReader
from music.adapters.memory_repository import MemoryRepository


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = Path('music') / 'adapters' / 'data'

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    data = TrackCSVReader(str(data_path) + "/raw_albums_excerpt.csv", str(data_path) + "/raw_tracks_excerpt.csv")
    data.read_csv_files()

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository(data)

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

    return app
