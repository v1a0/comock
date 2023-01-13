
# @mock(
#     args=("foo", "bar"),
#     _call=function,
#     _return="yes"
# )
#
#
# @mock(
#     args={
#         "foo": (int, float),
#         "bar": None
#    },
#     _call=function1,
#     _return=function2
# )
#
# mock.set.mode = mock.mode.ON
#
# MockExceptionTyping
# WrongArgsInCallFunction
#
#
# class MockClass():
# #same methods as original but comock
#     def foo(asd: int):
#         return 4
#
#
# @MockClass
# class OriginalClass:
#     def foo(asd: int):
#         return 2+2

from comock import mock



