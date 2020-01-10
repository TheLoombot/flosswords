#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import random 
import numpy
import operator
import time 

f = open('./wiki.txt')
words = [line.rstrip('\n').upper() for line in f]
scoreCache = {}

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
  if len(matrix) != len(matrix[0]):
    return False
  for i in range(len(matrix)):
    columnWord = ''.join(columnOfMatrix(matrix, i))
    if not isWord(columnWord):
      return False
    rowWord = ''.join(matrix[i])
    if rowWord == columnWord:
      return False
  return True

def stringScore(inputString, size):
  stringKey = (inputString, size)
  if stringKey not in scoreCache:
    possibleWords = [k for k in words if (k.startswith(inputString) and len(k)==size)]
    scoreCache[stringKey] = len(possibleWords)
    #print "Score cache now " + str(len(scoreCache)) + " entries long" 
  return scoreCache[stringKey]
    
def basicScoringMethod(size):
  # print "Going for size " + str(size) + " using basic scoring method..."
  # print "Score cache size is " + str(len(scoreCache)) 
  result = []
  possibleWords = [j for j in words if len(j)==size]
  #print str(len(possibleWords)) + " possible words in the set..."
  for row in range(size): 
    if row == 0:
      firstWord = random.choice(possibleWords)
      #print "Choosing " + firstWord + " randomly for row 0" 
      result.append(list(firstWord))
      continue
    scoredWordsDict = {}
    for index, word in enumerate(possibleWords):
      curWordScore = 0
      for x in range(size):
        columnWordPrefix = ''.join(columnOfMatrix(result, x)) + word[x]
        curWordScore = curWordScore + stringScore(columnWordPrefix, size)
      if curWordScore >= size:
        scoredWordsDict[word] = curWordScore
    #print "Top words for row " + str(row) + ":"  
    topWords = sorted(scoredWordsDict.items(), key = operator.itemgetter(1))[-3:]
    #print topWords
    if len(topWords) == 0:
      #print "CRAP! No eligible words found... aborting..."
      break
    else:
      bestWord = random.choice(topWords)[0]
      result.append(list(bestWord))
      #print "Chose " + bestWord
  #print numpy.matrix(result)
  if checkColumns(result):
    # print "👌🏽"
    return result
  else: 
    # print "😰 uh oh!"
    pass

loopCount = 0
while True:
  # print "\nAttempt " + str(loopCount)
  startTime = time.time()
  loopCount = loopCount + 1 
  result = basicScoringMethod(5)
  if result:
    print "After " + str(loopCount) + " tries:" 
    print numpy.matrix(result)
    # break
  else:
    pass
  # print "Attempt %i, %.2f seconds" % (loopCount, (time.time() - startTime))



