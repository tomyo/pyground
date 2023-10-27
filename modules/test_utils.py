from typing import Callable, NamedTuple


class TestCases(NamedTuple):
    args: list
    kwargs: dict
    expected: any
    description: str

    def __repr__(self) -> str:
        return f"TestCases({self.args}, {self.kwargs}, {self.expected}, {self.description})"


def run_tests(fun: Callable, casos: list[TestCases]) -> None:
    print("Ejecutando tests...\n")
    for caso in casos:
        exception = None
        ok = False
        try:
            result = fun(*caso[0], **caso[1])
            ok = result == caso[2]
        except Exception as e:
            exception = e
            if type(e) == caso[2]:
                # The exception was the expect one, so it's ok
                ok = True

        if ok:
            print("[OK ✔]", caso[3])
        else:
            got = result if not exception else exception.__repr__()
            print("[Fail ❌]", caso[3])
            args = [a.__repr__() for a in caso[0]]
            kwargs = [f"{k}={v.__repr__()}" for k, v in caso[1].items()]
            print(f">>> {fun.__name__}({','.join(args)}, {','.join(kwargs)})")
            print(f"Returned: {got}\nExpected: {caso[2]}")
