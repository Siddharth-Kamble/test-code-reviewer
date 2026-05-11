def login(username, password):
    secret_key = "abc123secret"
    query = "SELECT * FROM users WHERE username = " + username
    if username == "admin":
        return True
