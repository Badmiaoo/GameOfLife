import re

from setupRleFile import setupRle


# !

def rleReader(rleFile):
  # Dict for stock params from rle file
  rleParams = {}

  isBreak = False
  # Open rle file to read it
  with open(rleFile, 'r') as f:
    # Read line by line
    for line in f:
      # Remove space en \n
      lineTrimed = line.replace(' ', '').strip()
      # Get two first letter like potentialy #C or #P
      twoFirstLetter = lineTrimed[:2]
      # To skip empty line
      if lineTrimed == '':
        continue
      # Check if this letter is  available
      elif twoFirstLetter in setupRle.keys():
        rleParams[twoFirstLetter] = setupRle.get(
            twoFirstLetter)(line, rleParams)
      # Check the params of position
      elif re.search(r'x=[0-9]*,y=[0-9]*', lineTrimed):
        rleParams['#P'] = setupRle.get('pos')(lineTrimed)
        # Check the params of rule
        if re.search(r'rule=[0-8/sbSB]*', lineTrimed):
          rleParams['#r'] = setupRle.get('rule')(lineTrimed)
      # Check if pattern is contains only with o, b, $ or !
      elif not re.compile(r'[^0-9$!bo]').search(lineTrimed):
        if '!' in lineTrimed:
          lineTrimedSplited = lineTrimed.split('!')
          lineTrimed = lineTrimedSplited[0]
          isBreak = True
        rleParams['pattern'] = setupRle.get('pattern')(lineTrimed, rleParams)
        if isBreak:
          break
      # Raise Error
      else:
        setupRle.get('error')(line)
  return rleParams
