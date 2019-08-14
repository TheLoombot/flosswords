# flosswords

Script and word list to create "mini" crossword puzzles like the New York Times. Just the grid... you have to write your own clues!

The fundamental thing that will make this good or not is the word list. 

I am using an abridged version of the Crossword Nexus Word List, cropped to 3-6 letter words. 

Method 1 was totally random... it just picked random words for rows, then checked the columns. It could make 3 and 4 letter puzzles easily, but wouldn't stumble onto a valid 5x5 after many, many runs.

Method 2 tried to restrict subsequent row choices based on valid column words. It failed.

Method 3 picks a random word for row 0, then scores all the words in the set for the next row, and picks a top-scorer. The score is simply the number of words in the list that start with the resulting column letters if the word were picked (summed across all columns). We repeat this for all rows until we find a valid matrix. We cache the scores of all strings as we run so we don't have to do redundant calculation (this was a HUGE time-saver). Works well after a few tries for size 5... takes many many attempts but can eventually successfully create a size 6. For example:

```
[['P' 'A' 'S' 'C' 'A' 'L']
 ['A' 'S' 'T' 'A' 'R' 'E']
 ['S' 'H' 'A' 'R' 'I' 'A']
 ['S' 'A' 'T' 'E' 'E' 'N']
 ['E' 'M' 'E' 'R' 'G' 'E']
 ['S' 'E' 'N' 'S' 'E' 'D']]
```

One downside to this approach is that you see a lot of the same words over and over, because words with common letters (S, A, E, T) tend to score highly. That's why the first row (row 0) is purely random. If we scored the first row, we'd always start with the same word.

Some relevant links:

https://crosswordnexus.com/downloads/wordlist.txt.zip

https://www.reddit.com/r/crossword/comments/7n72a1/word_list_for_crossword_creation/
