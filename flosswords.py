#!/usr/bin/python

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
  print "Going for size " + str(size) + "..."
  count = 0
  while True:
    count += 1
    result = []
    for i in range(size):
      result.append(getWordFromList(size))
    if checkColumns(result):
      print "After " + str(count) + " attempts:"
      print numpy.matrix(result)
      return result
    else:
      if count % 100000 == 0:
        print str(count) + " attempts so far..."
      continue

def altMethod(size):
  print "Going for size " + str(size) + "..."
  count = 0
  while True:
    count = count + 1
    result = []
    firstAcrossWord = getWordFromList(size)
    result.append(firstAcrossWord)
    # print("First row word is: ", ''.join(firstAcrossWord))
    possibleColumnWords = [i for i in words if (i.startswith(firstAcrossWord[0]) and len(i)==size)]
    columnWord = random.choice(possibleColumnWords)
    # print("First column word is ", ''.join(columnWord))
  
    for i in range(size-1):
      i = i + 1
      possibleRowWords = [j for j in words if (j.startswith(columnWord[i]) and len(j)==size)]
      result.append(list(random.choice(possibleRowWords)))

    if checkColumns(result):
      print "After " + str(count) + " attempts:"
      print numpy.matrix(result)
      return result

    else:
      if count % 100 == 0:
        print str(count) + " attempts so far..."
        print numpy.matrix(result)
      continue


# newCrossWord(3)

altMethod(3)
altMethod(4)
altMethod(5)
