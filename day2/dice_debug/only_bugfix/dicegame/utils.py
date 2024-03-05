class InputError(Exception):
    pass


def i_just_throw_an_exception():
    """
    BUGFIX:
    -removed unnecessary functions;
    -renamed class for handling the wrong input parameter
    -better error description
    """
    raise InputError("Error! Unable to understand if you want to continue playing. For now, it is better to stop.")
