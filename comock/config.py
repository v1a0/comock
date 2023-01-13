from comock import MockObjTag, MockObjTagList


class MockerConfig:
    def __init__(self):
        pass

    @property
    def all_tags(self) -> MockObjTagList:
        return MockObjTag.all_tags()

    def enable_tag(self, tag_name: str):
        self.all_tags[tag_name].enable()

    def disable_tag(self, tag_name: str):
        self.all_tags[tag_name].disable()

    def enable_global(self):
        self.enable_tag('global')

    def disable_global(self):
        self.disable_tag('global')

    def enable_all_tags(self):
        self.all_tags.enable()

    def disable_all_tags(self):
        self.all_tags.disable()


__all__ = ["MockerConfig"]
