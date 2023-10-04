init_code = """
if not "a" in USER_GLOBAL:
    raise NotImplementedError("Where is 'a' variable?")

if not "b" in USER_GLOBAL:
    raise NotImplementedError("Where is 'b' variable?")
    
a = USER_GLOBAL['a']
b = USER_GLOBAL['b']

if not isinstance(a, int):
    raise TypeError("'a' variable must be an integer")

if not isinstance(b, int):
    raise TypeError("'b' variable must be an integer")

if a != 2:
    raise ValueError("'a' variable must have a value of 2")

if b != 5:
    raise ValueError("'b' variable must have a value of 5")
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