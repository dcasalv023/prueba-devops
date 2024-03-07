# -*- coding: utf-8 -*-
"""
This module contains tests for the Flask application.
"""

# import pytest
from app import app  # Flask instance of the API

def test_index_route():
    """
    Test the index route.
    """
    response = app.test_client().get('/status')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'OK'

def test_landing():
    """
    Test the landing page.
    """
    landing = app.test_client().get('/')
    html = landing.data.decode()
    assert landing.status_code == 200
    assert "Daniel Castillejo Álvarez" in html
    assert "It is currently " in html


