init_code = """
if not "robots" in USER_GLOBAL:
    raise NotImplementedError("Where is 'robots' variable?")

robots = USER_GLOBAL['robots']    

if not isinstance(robots, int):
    raise TypeError("'robots' variable must be an integer")

if robots != 2:
    raise ValueError("'robots' variable must have a value of 2")    

if not "droids" in USER_GLOBAL:
    raise NotImplementedError("Where is 'droids' variable?")

droids = USER_GLOBAL['droids']

if not isinstance(droids, int):
    raise TypeError("'droids' variable must be an integer")

if droids != 5:
    raise ValueError("'droids' variable must have a value of 5")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "First": [
        prepare_test(middle_code='''''',
                     test="",
                     answer="")]}