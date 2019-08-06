import string
import random 
import numpy

f = open('./3-4-5-wordlist.txt')
words = [line.rstrip('\n').upper() for line in f]

def isWord(word):
  if word in words:
    return True
  else:
    return False

def getWordFromList(size):
  while True:
    word = random.choice(words)
    if (len(word) == size):
       return list(word)

def columnOfMatrix(matrix, i):
  return[row[i] for row in matrix]

def checkColumns(matrix):
  for i in range(len(matrix)):
    columnWord = ''.join(columnOfMatrix(matrix, i))
    if not isWord(columnWord):
      return False
  return True

def newCrossWord(size):
  count = 0
  while True:
    count += 1
    result = []
    for i in range(size):
      result.append(getWordFromList(size))
    if checkColumns(result):
      print "After " + str(count) + " attempts"
      print numpy.matrix(result)
      return result
    else:
      if count % 10000 == 0:
        print count
      continue

newCrossWord(3)
newCrossWord(3)
newCrossWord(3)
newCrossWord(4)
newCrossWord(4)
newCrossWord(4)
