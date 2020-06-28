import json
from sanic import Sanic
from sanic import response
from sanic_jwt import Initialize, protected, exceptions

from typing import Dict, List

with open('auth.pw') as fh:
    _USERS_AUTH = json.load(fh)


async def authenticate(request, *args, **kwargs):
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user_password = _USERS_AUTH.get(username)
    if user_password is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user_password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return {username: user_password}


app = Sanic("App Name")
Initialize(app, authenticate=authenticate)


@app.route("/", methods=['POST', ])
@protected()
async def parse_input_api(request):
    return response.json(parse_input(request.json))


def parse_input(input_obj: List[Dict]) -> Dict:
    return {e['name']: next(v for k, v in e.items() if 'val' in k.lower()) for e in input_obj}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
