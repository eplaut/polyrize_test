from sanic import Sanic
from sanic.response import json

from typing import Dict, List


app = Sanic("App Name")


@app.route("/", methods=['POST', ])
async def parse_input_api(request):
    return json(parse_input(request.json))


def parse_input(input_obj: List[Dict]) -> Dict:
    return {e['name']: next(v for k, v in e.items() if 'val' in k.lower()) for e in input_obj}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
