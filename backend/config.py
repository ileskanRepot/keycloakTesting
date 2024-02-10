from backend.models import authConfiguration

settings = authConfiguration(
	server_url="https://auth.ileska.fi/",
	realm="PythonTest",
	client_id="testClient",
  # client_secret="",
	authorization_url="https://auth.ileska.fi/realms/PythonTest/protocol/openid-connect/auth",
	token_url="https://auth.ileska.fi/realms/PythonTest/protocol/openid-connect/token",
)
