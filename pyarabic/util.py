from typing import Callable


class Composer(Callable):
    """
        represents a macroCommand that applies several transforms one after another

        :param transforms: list of callables to be applied
        :type transforms: list[typing.Callable]
    """

    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, le_input):
        for transform in self.transforms:
            le_input = transform(le_input)
        return le_input
