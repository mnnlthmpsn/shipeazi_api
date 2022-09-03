def test_create_entity(client):
    response = client.post('/accounts/new_entity', json={
        "name": "Shipeazi",
        "email": "enquiries@shipeazi.com",
        "phone": "0540609437",
        "is_business": True
    })

    assert response.status_code == 200
    assert response.json["message"] is not None
    assert response.json["message"] == "Entity added successfully"
