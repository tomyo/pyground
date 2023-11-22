from typing import Callable, NamedTuple


class TestCases(NamedTuple):
    args: list
    kwargs: dict
    expected: any
    description: str = ""

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

        args = [a.__repr__() for a in caso[0]]
        kwargs = [f"{k}={v.__repr__()}" for k, v in caso[1].items()]
        fpprint = f'{fun.__name__}({", ".join(args)}{(", " if kwargs else "") + ", ".join(kwargs)})'
        description = caso[3] if len(caso) == 4 else f"{fpprint} -> {caso[2]}"

        if ok:
            print("[OK ✔]", description)
        else:
            got = result if not exception else exception.__repr__()
            print("[Fail ❌]", description)
            print(f""">>> {fpprint}""")
            print(f"Returned: {got}")
            print(f"Expected: {caso[2].__name__ if exception else caso[2]}")

        print("")  # Add a new line after each test result
