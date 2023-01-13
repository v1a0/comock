import typing
from functools import wraps

from comock import MockObjTag, MockObjTagList
from comock import MockValue as mv


class MockerEngine:
    def __init__(self):
        pass

    def _init_mock_obj(self, obj: any, tags: MockObjTagList = None):
        """
        Add all necessary attributes to mock object
        """
        setattr(obj, f'__smoks__obj_tags', tags)

    def mock_callable(
        self,
        _callable: callable,
        _return: any,
        _call: callable,
        call_args: tuple,
        call_kwargs: dict,
        _raise: any = mv.NOTHING,
        execute: bool = False,
        tags: typing.Iterable[typing.Union[MockObjTag, typing.AnyStr]] = None,
    ) -> typing.Callable:
        """
        Mock any callable object

        :param _callable: Object to mock
        :param _return: Returning value
        :param _call: Function to call instead of original call object
        :param call_args: Args to give into _call
        :param call_kwargs: Kwargs to give into _call
        :param _raise: Exception to raise when object called
        :param execute: Should be original object be executed (called) or not
        :param tags: Mock object tags
        :return:
        """
        if tags is None:
            tags = MockObjTagList(MockObjTag('global'))
        elif isinstance(tags, (list, tuple)):
            tags = MockObjTagList(*tags)

        self._init_mock_obj(_callable, tags)

        @wraps(_callable)
        def mocked_callable(*args, **kwargs):
            # Checking is mocking enabled for any MockObj tags
            if not tags.is_any_enabled:
                return _callable(*args, **kwargs)

            # Raise exception if it should
            if _raise is not mv.NOTHING:
                raise _raise

            # Execute (call) anyway
            if execute:
                _callable(*args, **kwargs)

            # Something should be called instead or after
            if _call:
                result = _call(*call_args, **call_kwargs)

                # Specific return value is not set, return called 'something' results
                if _return is mv.NOTHING:
                    return result

            # Otherwise if specific value to return is set
            return _return

        return mocked_callable


__all__ = ["MockerEngine"]
