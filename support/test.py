from extra.vartab import *

SCHEMA = {
    'a1': {
        'b1': {
            'c1': 'a1.b1.c1',
            'c2': 'a1.b1.c2'
        },
        'b2': {
            'c1': 'a1.b2.c1',
            '#c2': 'a1.bc.c2',
        },
        'd1': "a1.b1.c2 is ${a1.b1.c1}"
    },
    '#a2': {
        'b1': {
            'c1': 'a2.b1.c1',
            'c2': 'a2.b1.c2'
        },
        'b2': {
            'c1': 'a2.b2.c1',
            'c2': 'a2.bc.c2',
        },
        'd2': "a2.b1.c2 is ${#a2.b1.c1}"
    },
}

v=Vartab(SCHEMA)

import json

json.dumps(v.GetValue())

