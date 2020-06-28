import collections
from typing import Any


class MagicList(list):
    def __setitem__(self, index: int, value: Any) -> None:
        if index == len(self):
            self.append(value)
        else:
            # this may raise IndexError for missing indexes
            super(MagicList, self).__setitem__(index, value)
