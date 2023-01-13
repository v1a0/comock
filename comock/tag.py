import typing
from dryco import method_not_allowed


class MockObjTag:
    _registered_tags = {'global': False}

    @classmethod
    @property
    def registered_tags(cls) -> dict:
        return cls._registered_tags

    def __init__(self, name: str, default_status: bool = None):
        if not name:
            Exception("MockObjTag name can't be empty")

        self.name = str(name)
        self.__register_tag(name=self.name, default_status=default_status)

    def __str__(self):
        return f"<MockObjTag: name='{self.name}', enabled={self.status}>"

    @property
    def status(self) -> bool:
        return self.registered_tags[self.name]

    @classmethod
    def __register_tag(cls, name: str, default_status: bool = None):
        if name not in cls._registered_tags.keys():
            if default_status is None:
                default_status = False
            cls._registered_tags[name] = default_status

        elif default_status is not None:
            Exception(
                f"Group {name} already initialized with default status as {cls._registered_tags[name]}, "
                f"changing this parameter ar not allowed"
            )

        else:
            pass

    @classmethod
    def __change_tag_status(cls, name: str, status: bool):
        cls._registered_tags[name] = status

    @classmethod
    @property
    def all_tags_names(cls):
        return cls._registered_tags.keys()

    @classmethod
    def all_tags(cls):
        return MockObjTagList(*cls.all_tags_names)

    def enable(self):
        self.__change_tag_status(self.name, True)

    def disable(self):
        self.__change_tag_status(self.name, False)


class MockObjTagList(list):
    """
    Regular list with few extra properties
    """

    def __init__(self, *args: typing.Union[MockObjTag, typing.AnyStr]):
        tags = [self._any_to_tag(tag) for tag in args]
        super(MockObjTagList, self).__init__(tags)

    def __str__(self):
        return f"[{', '.join(str(tag) for tag in self)}]"

    def __getitem__(self, item: typing.Union[int, typing.AnyStr]) -> MockObjTag:
        match item:
            case int():
                return super(MockObjTagList, self).__getitem__(item)
            case str():
                if item not in self:
                    raise Exception(f"No tag named '{item}' in MockTagList")
                return MockObjTag(item)
            case _:
                TypeError(
                    f"Unsupported type '{type(item)}' for __getitem__ method. Use integer or string instead."
                )

    def __contains__(self, item: typing.Union[MockObjTag, typing.AnyStr]) -> bool:
        match item:
            case str():
                return item in self.names
            case MockObjTag():
                return super(MockObjTagList, self).__contains__(item)
            case _:
                TypeError(
                    f"Unsupported type '{type(item)}' for __contains__ method. Use MockObjTag or string instead."
                )

    @classmethod
    def _any_to_tag(cls, tag: typing.Union[MockObjTag, typing.AnyStr]) -> MockObjTag:
        match tag:
            case MockObjTag():
                return tag
            case _:
                return MockObjTag(tag)

    @property
    def is_any_enabled(self) -> bool:
        return any(tag.status for tag in self)

    @property
    def is_all_disabled(self) -> bool:
        return not self.is_any_enabled

    @property
    def names(self) -> list:
        return list(tag.name for tag in self)

    def enable(self):
        for tag in self:
            tag: MockObjTag
            tag.enable()

    def disable(self):
        for tag in self:
            tag: MockObjTag
            tag.disable()

    @method_not_allowed
    def clear(self) -> None:
        pass

    @method_not_allowed
    def insert(self) -> None:
        pass

    @method_not_allowed
    def index(self) -> None:
        pass

    @method_not_allowed
    def pop(self) -> None:
        pass

    @method_not_allowed
    def append(self) -> None:
        pass


__all__ = ["MockObjTag", "MockObjTagList"]
