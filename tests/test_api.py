import json
import unittest

from api import parse_input


class InputProcessingTest(unittest.TestCase):
    def test_example(self):
        input_josn = '''
[
    {
        "name": "device",
        "strVal": "iPhone",
        "metadata": "not interesting"
    },
    {
        "name": "isAuthorized",
        "boolVal": "false",
        "lastSeen": "not interesting"
    }
]
'''
        input_obj = json.loads(input_josn)
        output_obj = parse_input(input_obj)
        self.assertDictEqual(
            output_obj,
            {
                'device': 'iPhone',
                'isAuthorized': 'false',
            }
        )
