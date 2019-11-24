from ._inspect import is_iterable


def convert_to_list(pattern):
    """
    Convert iterable to a list.
    Nested iterables are converted to lists as well.
    :param pattern: any iterable
    :return: list
    """
    assert is_iterable(pattern), "%s is not iterable" % type(pattern).__name__

    def _convert(obj):
        if hasattr(obj, "__iter__"):
            return [
                _convert(x)
                for x in obj
            ]
        else:
            return obj

    return _convert(pattern)

