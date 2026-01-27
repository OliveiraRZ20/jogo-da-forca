# imports internos

# imports externos

hangmanPoses: list[str] = [
r"""
    +---------+
    |         |
    |
    |
    |
    |
    |
    |
    |
====================""",
r"""
    +---------+
    |         |
    |         O
    |
    |
    |
    |
    |
    |
====================""",
r"""
    +---------+
    |         |
    |         O
    |         |
    |
    |
    |
    |
    |
====================""",
r"""
    +---------+
    |         |
    |         O
    |        /|
    |
    |
    |
    |
    |
====================""",
r"""
    +---------+
    |         |
    |         O
    |        /|\
    |
    |
    |
    |
    |
====================""",
r"""
    +---------+
    |         |
    |         O
    |        /|\
    |        /
    |
    |
    |
    |
====================""",
r"""
    +---------+
    |         |
    |         X
    |        /|\
    |        / \
    |
    |
    |
    |
====================""",
]

class Hangman:
    def __init__(self):
        self.erros: int = 0
        self.poses: list[str] = hangmanPoses
    
    def errou(self):
        self.erros += 1
    
    def get_pose(self) -> str:
        return self.poses[self.erros]
