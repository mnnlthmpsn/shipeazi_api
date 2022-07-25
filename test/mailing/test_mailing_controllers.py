def test_subscribe(client):
    response = client.post('/mailing/subscribe', json={"email": "etntiamoah@st.ug.edu.gh"})

    assert response.status_code == 200
    assert response.json["message"] is not None
    assert response.json["message"] == "Subscription added successfully"
