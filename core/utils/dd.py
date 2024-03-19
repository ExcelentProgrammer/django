from core.exceptions import BreakException


def dd(*args, message: str | None = None,
       data: dict | list | None = None) -> None:
    """
    Dump the given variables and then raise a SystemExit exception
    to stop execution of the script.
    """

    raise BreakException(args, message=message,data=data)
