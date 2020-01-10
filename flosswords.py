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
  for i in range(len(matrix)):
    columnWord = ''.join(columnOfMatrix(matrix, i))
    if not isWord(columnWord):
      return False
  if len(matrix) != len(matrix[0]):
    return False
  return True

def randomMethod(size):
  print "Going for size " + str(size) + " basically just randomly"
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

def stillPrettyRandomMethod(size):
  #print "Going for size " + str(size) + " using a dumb method"
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
      #print numpy.matrix(result)
      return result
    else:
      if count % 100 == 0:
        print str(count) + " attempts so far..."
        #print numpy.matrix(result)
      continue

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



