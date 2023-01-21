import typing
from functools import wraps

from .misc import MockValue as mv
from .config import MockerConfig
from .engine import MockerEngine
from .tag import MockObjTag



class Mocker:
    def __init__(self):
        self.config = MockerConfig()
        self.engine = MockerEngine()

    def callable(
        self,
        _callable: callable = None,
        _return: any = mv.NOTHING,
        _call: callable = None,
        call_args: tuple = None,
        call_kwargs: dict = None,
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
        :return: Mocked callable object
        """

        if _call:
            call_args = call_args if call_args else tuple()
            call_kwargs = call_kwargs if call_kwargs else dict()

        @wraps(_callable)
        def mock_callable_handler(__callable: callable):
            return self.engine.mock_callable(
                __callable,
                _return,
                _call,
                call_args,
                call_kwargs,
                _raise,
                execute,
                tags,
            )

        # calling without kwargs
        if _callable:
            return mock_callable_handler(_callable)

        # calling with kwargs
        return mock_callable_handler

    def method(
        self,
        _method: typing.Callable = None,
        _return: any = mv.NOTHING,
        _call: typing.Callable = None,
        call_args: tuple = None,
        call_kwargs: dict = None,
        _raise: any = mv.NOTHING,
        execute: bool = False,
        tags: typing.Iterable[typing.Union[MockObjTag, typing.AnyStr]] = None,
    ) -> typing.Callable:
        return self.callable(
            _callable=_method,
            _return=_return,
            _call=_call,
            call_args=call_args,
            call_kwargs=call_kwargs,
            _raise=_raise,
            execute=execute,
            tags=tags,
        )
