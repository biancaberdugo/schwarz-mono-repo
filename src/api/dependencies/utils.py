from typing import Type


def check_protocol(proto: Type):
    def wrapper(cls_def):
        try:
            assert issubclass(cls_def, proto)
        except AssertionError as e:
            e.args = (f"{cls_def} does not implement protocol {proto}",)
            raise
        return cls_def

    return wrapper
