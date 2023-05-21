import os



"""
https://docs.python.org/3/library/tempfile.html
"""

import pytest

from moviebag import create_app

"""
References to source code
"""


# -----------------------------------------------------------------------------

"""
May 20th 2023

doc: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/



- to print add -s to pytest command line

pytest -s

- For markers like in hello

pytest -m hello

- to test-run a specific file

pytest tests/test_factory.py

- to test-run a specific test within a file

pytest tests/test_factory.py::test_hello


"""


@pytest.fixture
def app():
    """
    From doc

    The app fixture will call the factory and pass test_config to configure the application and database for testing
    instead of using your local development configuration.
    """

    """Create and configure a new app instance for each test."""

    # create the app with common test config
    app = create_app({"TESTING": True })
    print("SALUT")

    print("TESTING C")
    yield app
    print("TESTING D")

# @pytest.fixture
# def runner(app):
#     """A test runner for the app's Click commands."""
#     return app.test_cli_runner()


@pytest.fixture
def client(app):
    """A test client for the app."""
    print("FIxTURE CLIENT")
    return app.test_client()

