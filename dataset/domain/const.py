from enum import IntEnum


class ChunkCode(IntEnum):
    NOT_RELEVANT: int = -1
    SPLIT: int = 1
    NOT_SPLIT: int = 0


class ASTELabels(IntEnum):
    NEU: int = 5
    POS: int = 4
    NEG: int = 3
    OPINION: int = 2
    ASPECT: int = 1
    NOT_PAIR: int = 0
    NOT_RELEVANT: int = -1
