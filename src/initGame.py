import numpy as np


def initGame(pattern, pos, mapMaxX, mapMaxY):
  posX = int(pos['x'])
  posY = int(pos['y'])

  game = np.zeros((mapMaxY, mapMaxX)).astype(bool)
  mapCell = np.zeros((mapMaxY, mapMaxX)).astype(bool)

  numberCell = ''
  curX, curY = 0, 0
  for cell in pattern:
    # While cell is [0-9], stock et continue
    if cell.isdigit():
      numberCell += cell
      continue
    # Add `numberCell` of line
    elif cell == '$':
      curX = 0
      curY += 1 if numberCell == '' else int(numberCell)
      numberCell = ''
    # Otherwise add `numberCell` of alive cell in game map
    else:
      numberCell = 1 if numberCell == '' else int(numberCell)
      for _ in range(numberCell):
        mapCell[curY, curX] = False if cell == 'b' else True
        curX += 1
      numberCell = ''

  # Get width max of cell pattern
  cellsY = max(np.where(sum(mapCell) > 0)[0]) + 1

  # Get heigth max of cell pattern
  cellsX = max(np.where(sum(mapCell.T) > 0)[0]) + 1

  # Pattern cell
  cells = mapCell[0:cellsX, 0:cellsY]

  # Put pattern on the map
  game[posY:posY + cells.shape[0], posX:posX + cells.shape[1]] = np.copy(cells)

  return game
