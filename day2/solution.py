"""Solution to day 2."""

from dataclasses import dataclass
from enum import Enum


def get_data(path: str) -> list[str]:
    with open(path) as f:
        return f.readlines()


class RockPaperScissorsSelection(Enum):
    """The possible selections when playing Rock, Paper, Scissors."""

    ROCK = "A", 1
    PAPER = "B", 2
    SCISSORS = "C", 3

    def __init__(self, selection, score):
        self.selection = selection
        self.score = score


class RockPaperScissorsRoundResult(Enum):
    """The possible results when playing rock paper scissors."""

    WIN = "Z"
    DRAW = "Y"
    LOSE = "X"


@dataclass
class RockPaperScissorsPlayer:
    """A player in a round of Rock, Paper, Scissors."""

    name: str
    score: int


class RockPaperScissorsGame:
    """A round of Rock, Paper, Scissors."""

    def __init__(
        self, player_1: RockPaperScissorsPlayer, player_2: RockPaperScissorsPlayer
    ):
        """The selections made by each player."""
        self.player_1 = player_1
        self.player_2 = player_2

    @staticmethod
    def determine_round_winner(
        player1_selection: RockPaperScissorsSelection,
        player2_selection: RockPaperScissorsSelection,
    ):
        """Determine the winner of a round of Rock, Paper, Scissors."""
        if player1_selection == player2_selection:
            return 0
        elif (
            player1_selection == RockPaperScissorsSelection.ROCK
            and player2_selection == RockPaperScissorsSelection.SCISSORS
        ):
            return 1
        elif (
            player1_selection == RockPaperScissorsSelection.PAPER
            and player2_selection == RockPaperScissorsSelection.ROCK
        ):
            return 1
        elif (
            player1_selection == RockPaperScissorsSelection.SCISSORS
            and player2_selection == RockPaperScissorsSelection.PAPER
        ):
            return 1
        else:
            return 2

    def play_round(
        self,
        player1_selection: RockPaperScissorsSelection,
        player2_selection: RockPaperScissorsSelection,
    ):
        """Play a round of Rock, Paper, Scissors."""
        winner = self.determine_round_winner(player1_selection, player2_selection)

        if winner == 0:
            self.player_1.score += player1_selection.score + 3
            self.player_2.score += player2_selection.score + 3

        elif winner == 1:
            self.player_1.score += player1_selection.score + 6
            self.player_2.score += player2_selection.score

        elif winner == 2:
            self.player_1.score += player1_selection.score
            self.player_2.score += player2_selection.score + 6

        else:
            raise ValueError(f"Invalid value obtained for winner ({winner})")


def part_1_solution(data: list[str]) -> int:
    """Get the score of player 2 after playing all the rounds."""
    player_1 = RockPaperScissorsPlayer("Player 1", 0)
    player_2 = RockPaperScissorsPlayer("Player 2", 0)

    game = RockPaperScissorsGame(player_1, player_2)

    round_selection_map = {
        "A": RockPaperScissorsSelection.ROCK,
        "B": RockPaperScissorsSelection.PAPER,
        "C": RockPaperScissorsSelection.SCISSORS,
        "X": RockPaperScissorsSelection.ROCK,
        "Y": RockPaperScissorsSelection.PAPER,
        "Z": RockPaperScissorsSelection.SCISSORS,
    }

    for line in data:
        player1_selection, player2_selection = line.rstrip("\n").split(" ")

        game.play_round(
            round_selection_map[player1_selection],
            round_selection_map[player2_selection],
        )

    return player_2.score


def determine_player2_selection(
    player1_selection: RockPaperScissorsSelection, result: RockPaperScissorsRoundResult
):
    if result == RockPaperScissorsRoundResult.DRAW:
        return player1_selection

    if result == RockPaperScissorsRoundResult.WIN:
        if player1_selection == RockPaperScissorsSelection.ROCK:
            return RockPaperScissorsSelection.PAPER
        elif player1_selection == RockPaperScissorsSelection.PAPER:
            return RockPaperScissorsSelection.SCISSORS
        elif player1_selection == RockPaperScissorsSelection.SCISSORS:
            return RockPaperScissorsSelection.ROCK
        else:
            raise ValueError(
                f"Invalid value for player1_selection ({player1_selection})"
            )

    if result == RockPaperScissorsRoundResult.LOSE:
        if player1_selection == RockPaperScissorsSelection.ROCK:
            return RockPaperScissorsSelection.SCISSORS
        elif player1_selection == RockPaperScissorsSelection.PAPER:
            return RockPaperScissorsSelection.ROCK
        elif player1_selection == RockPaperScissorsSelection.SCISSORS:
            return RockPaperScissorsSelection.PAPER
        else:
            raise ValueError(
                f"Invalid value for player1_selection ({player1_selection})"
            )


def part_2_solution(data: list[str]) -> int:
    """Get the score of player 2 after playing all the rounds."""
    player_1 = RockPaperScissorsPlayer("Player 1", 0)
    player_2 = RockPaperScissorsPlayer("Player 2", 0)

    game = RockPaperScissorsGame(player_1, player_2)

    round_selection_map = {
        "A": RockPaperScissorsSelection.ROCK,
        "B": RockPaperScissorsSelection.PAPER,
        "C": RockPaperScissorsSelection.SCISSORS,
    }

    for line in data:
        player1_selection, round_result = line.rstrip("\n").split(" ")

        player1_selection = round_selection_map[player1_selection]
        round_result = RockPaperScissorsRoundResult(round_result)
        player2_selection = determine_player2_selection(player1_selection, round_result)

        game.play_round(player1_selection, player2_selection)

    return player_2.score


if __name__ == "__main__":
    data = get_data("day2/input.txt")

    print(part_1_solution(data))

    print(part_2_solution(data))
