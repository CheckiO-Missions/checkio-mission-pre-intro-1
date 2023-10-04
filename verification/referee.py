from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.code import CheckiORefereeCode
# from checkio.referees.checkers import to_list

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiORefereeCode(
        tests=TESTS,
        # checker=to_list,
        # function_name={
        #     "python": "sum_two",
        #     "js": "sumTwo"
        # },
        # cover_code={
        #     'python-3': {},
        #     'js-node': {
        #         # "dateForZeros": True,
        #     }
        # }
    ).on_ready)
