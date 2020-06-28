from typing import Any, Type, Optional


class MagicList(list):
    def __init__(self, cls_type: Type = None, *args, **kwargs) -> None:
        self._cls_type = cls_type  # type: Optional[cls_type]
        super(MagicList, self).__init__(*args, **kwargs)

    def __setitem__(self, index: int, value: Any) -> None:
        if index == len(self):
            self.append(value)
        else:
            # this may raise IndexError for missing indexes
            super(MagicList, self).__setitem__(index, value)

    def __getitem__(self, item: int) -> Any:
        try:
            return super(MagicList, self).__getitem__(item)
        except IndexError:
            if self._cls_type:
                self[item] = self._cls_type()
                return super(MagicList, self).__getitem__(item)
            else:
                raise
