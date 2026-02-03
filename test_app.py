import pytest
import os
from app import app, DATA_FILE

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    # Cleanup test data
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_home_page(client):
    """Test home page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Visitor Log Application' in response.data

def test_add_visitor(client):
    """Test adding a visitor"""
    response = client.post('/add', data={'name': 'Test User'})
    assert response.status_code == 200
    assert b'Test User' in response.data

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'