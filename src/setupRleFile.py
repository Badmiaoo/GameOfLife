import sys


def letter_C(line, rleParams):
  lineC = rleParams.get('#C', False)
  if lineC is not False:
    return '{};{}'.format(lineC, line[2:].strip())
  return line[2:].strip()


def letter_N(line, *args):
  return line[2:].strip()


def letter_O(line, *args):
  return line[2:].strip()


def letter_P(line, *args):
  splited = line[2:].strip().split(' ')
  if len(splited) != 2 or not splited[0].isdigit() or not splited[1].isdigit():
    error(line)
  return {'x': splited[0], 'y': splited[1]}


def letter_r(line, *args):
  splited = line[2:].strip().split('/')
  if len(splited) != 2 or not splited[0].isdigit() or not splited[1].isdigit():
    error(line)
  return {'s': splited[0], 'b': splited[1]}


def pos(lineTrimed):
  splited = lineTrimed.split(',')
  x = splited[0].split('=')[1]
  y = splited[1].split('=')[1]
  return {'x': x, 'y': y}


def rule(lineTrimed):
  splited = lineTrimed.split('rule=')
  rule = splited[1].lower()

  ruleSplited = rule.split('/')

  numOfS = rule.count('s')
  numOfB = rule.count('b')

  if numOfB > 1 or numOfS > 1:
    error(lineTrimed)
  else:
    if 'b' in ruleSplited[1]:
      return {'s': ruleSplited[0].replace('s', ''), 'b': ruleSplited[1].replace('b', '')}
    elif 'b' in ruleSplited[0]:
      return {'s': ruleSplited[1].replace('s', ''), 'b': ruleSplited[0].replace('b', '')}
    elif 's' in ruleSplited[1]:
      return {'s': ruleSplited[1].replace('s', ''), 'b': ruleSplited[0].replace('b', '')}
    elif 's' in ruleSplited[1]:
      return {'s': ruleSplited[0].replace('s', ''), 'b': ruleSplited[1].replace('b', '')}
    else:
      return {'s': ruleSplited[0].replace('s', ''), 'b': ruleSplited[1].replace('b', '')}


def pattern(lineTrimed, rleParams):
  lineCode = rleParams.get('pattern', False)
  if lineCode is not False:
    return f'{lineCode}{lineTrimed}'
  return lineTrimed


def error(line):
  msg = 'This line: \'{}\' is not available.'.format(line) + \
    'See template of this simple version of RLE file supported.'
  raise SyntaxError(msg)
  sys.exit(1)


setupRle = {
    '#C': letter_C,
    '#N': letter_N,
    '#O': letter_O,
    '#P': letter_P,
    '#r': letter_r,
    'pos': pos,
    'rule': rule,
    'pattern': pattern,
    'error': error
}
