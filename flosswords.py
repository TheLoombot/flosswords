#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import random 
import numpy
import operator

f = open('./3-6.txt')
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
  if len(matrix) != len(matrix[0]):
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

def newNewMethod(size):
  print "Going for size " + str(size) + " using new new method..."
  result = []
  possibleWords = [j for j in words if len(j)==size]
  print str(len(possibleWords)) + " possible words in the set..."
  for row in range(size): 
    scoredWordsDict = {}
    random.shuffle(possibleWords)
    # hacky optimization to restrict evaluations to n random words
    limit = (row+1)*len(possibleWords)/size/1
    print "Evaluating " + str(limit) + " words for row " + str(row)
    abridgedList = possibleWords[:limit]
    for index, word in enumerate(abridgedList):
      if index % 100 == 0:
        print "  Evaluated " + str(index) + " words..." 
      curWordScore = 0
      for x in range(size):
        columnWordPrefix = ''.join(columnOfMatrix(result, x)) + word[x]
        possibleColumnWords = [k for k in possibleWords if (k.startswith(columnWordPrefix))]
        curWordScore = curWordScore + len(possibleColumnWords)
      if curWordScore >= size:
        scoredWordsDict[word] = curWordScore
    print "Top words:" 
    topWords = sorted(scoredWordsDict.items(), key = operator.itemgetter(1))[-10:]
    print topWords
    if len(topWords) == 0:
      print "CRAP! No eligible words found... aborting..."
      break
    else:
      bestWord = random.choice(topWords)[0]
      result.append(list(bestWord))
      print "Chose " + bestWord
  print numpy.matrix(result)
  if checkColumns(result):
    print "👌🏽"
  else: 
    print "😰 uh oh!"

newNewMethod(4)
