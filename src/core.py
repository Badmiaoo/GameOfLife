import numpy as np


def evolve(game, rule):
    # Evolves the Game of Life for one turn

    X = game.shape[0] + 4
    Y = game.shape[1] + 4

    resizeGame = np.zeros((X, Y))
    resizeGame[2:X - 2, 2:Y - 2] = np.copy(game)
    neigh = np.zeros((X, Y))

    upLeft = resizeGame[:-2, :-2]
    up = resizeGame[:-2, 1:-1]
    upRight = resizeGame[:-2, 2:]
    left = resizeGame[1:-1, :-2]
    rigth = resizeGame[1:-1, 2:]
    downLeft = resizeGame[2:, :-2]
    down = resizeGame[2:, 1:-1]
    downRight = resizeGame[2:, 2:]

    neigh[1:-1, 1:-1] = (
      upLeft + up + upRight +
      left + rigth +
      downLeft + down + downRight
    )

    livingBoard = np.zeros((X, Y))
    for nb in str(rule['b']):
      livingBoard = np.logical_or(neigh == int(nb), livingBoard > 0)
    for nb in str(rule['s']):
      livingBoard += np.logical_and(resizeGame == 1, neigh == int(nb))

    return livingBoard[2:X - 2, 2:Y - 2]


def core(game, frame, rule):
    # Returns the game after all frame generations
    evolution = np.zeros((frame, game.shape[0], game.shape[1]), dtype=bool)
    for t in range(frame):
        evolution[t, :, :] = game
        game = evolve(game, rule)
    return evolution
