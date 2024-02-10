# Keycloak + Pyhton + Javascript integration test

This is a project for me to learn about Keycloak and how to integrate it to web app. Currently this app can authenticate uses in frontend but backend does not yet support it.

This uses pythons FastAPI to serve the files, Keycloak in [auth.ileska.fi](https://auth.ileska.fi) and Javascript with [`/js/keycloak.js`](https://auth.ileska.fi/js/keycloak.js) to handle Javascript

# Frontend
Frontend uses the Keycloaks `/js/keycloak.js` file to handle Javascript and the frontend `functions.js` is based on these [guys work on youtube](https://www.youtube.com/watch?v=9Rge8XpzbwI) 

# Backend
Currently only backend functionality is to serve the frontend static files. In future I should include the logging in to the app also into the backend. The backend **un**working code is based on [this stackoverflow post](https://stackoverflow.com/a/77186511)

# TODO
1. Get backend account managin working
