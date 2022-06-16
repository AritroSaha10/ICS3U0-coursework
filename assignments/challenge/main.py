#-----------------------------------------------------------------------------
# Name:        Text Parser
# Purpose:     Parses and generates information based on a large piece of text
#
# Author:      Aritro Saha
# Created:     24-May-2022
# Updated:     24-May-2022
#-----------------------------------------------------------------------------

import os

clamp = lambda n, smallest, largest: max(smallest, min(n, largest))

def findAllIterative(fullStr, substr):
  fullStr = fullStr.lower()
  substr = substr.lower()
  
  startingIdx = 0
  instances = []

  while (idx := fullStr.find(substr, startingIdx)) != -1:
    instances.append(idx)
    startingIdx = idx + len(substr)

  return instances

def requireValidInput(inpStr: str, incorrectNote: str, checker) -> str:
  # Handle type errors
  if not isinstance(inpStr, str):
    raise TypeError("inpStr is not a string")
  elif not isinstance(incorrectNote, str):
    raise TypeError("incorrectNote is not a string")
  elif not callable(checker):
    raise TypeError("checker is not a callable")

  # Only exit once checker confirms
  while not checker(result := input(inpStr)):
    print(incorrectNote)
    print()

  return result

sentenceEndTokens = [".", "?", "!"]
falseSentenceEndTokens = [":--"]
wordFrequencyChart = {}
allText = ""

# Margin of error: 100
wordCount = 0
paragraphCount = 0
sentenceCount = 0

print("--- Text Parser ---")

fname = requireValidInput("Please input the name of the file you'd like to parse: ", "Please provide a real file.", lambda myFname: os.path.exists(myFname))  

with open(fname) as file:
  allText = file.read()
  file.seek(0)
  
  for line in file.readlines():
    if line != "\n":
      paragraphCount += 1
      
    for token in sentenceEndTokens:
      sentenceCount += line.count(token)

    for token in falseSentenceEndTokens:
      sentenceCount -= line.count(token)

    line.strip()
    
    for word in line.split(" "):
      word = word.lower().strip()
      cleanedWord = ''.join([char for char in word if char.isalnum() or char in "'"])
      
      if word.strip() == "":
        continue 
        
      if cleanedWord in wordFrequencyChart:
        wordFrequencyChart[cleanedWord] += 1
      else:
        wordFrequencyChart[cleanedWord] = 1

      wordCount += 1


wordFrequencyChart = dict(sorted(wordFrequencyChart.items(), key=lambda item: item[1], reverse=True))

print("Paragraph Count:", paragraphCount)
print("Word Count:", wordCount)
print("Sentence Count:", sentenceCount)

while True:
  choice = requireValidInput("What would you like to do? All Word Freq(af), Word Freq (f), Search (s), Quit (q): ", "Please provide a valid choice (f, s, q)", lambda inp: inp.lower() in "afsq")

  if choice == "af":
    for i, (key, value) in enumerate(wordFrequencyChart.items()):
      print(f"{i+1}: {key} - {value}")
      if i > 500:
        print(f"{len(wordFrequencyChart.items()) - 500} more words...")
        break
    print()
  
  if choice == "f":
    wordForFreq = requireValidInput("Provide a word to check its frequency: ", "Please provide a word in the text", lambda inp: inp.lower() in wordFrequencyChart)
  
    freq = wordFrequencyChart[wordForFreq.lower()]
    print(f"Frequency of {wordForFreq}: {freq}\n")

  if choice == "s":
    searchTerm = input("Search term: ")
    allIdx = findAllIterative(allText, searchTerm)
    originalLen = len(allIdx)
    allIdx = allIdx[:clamp(800, 0, len(allIdx))]
    
    for myIdx in allIdx:
      findInContext = allText[clamp(myIdx-10, 0, len(allText)):clamp(myIdx+10, 0, len(allText))].replace('\n', '<nl>').strip()
      
      print(f"At index {myIdx}: {findInContext}")

    if len(allIdx) == 0:
      print("There seem to be no occurences of your substring...")

    if originalLen > len(allIdx):
      print(f"{originalLen - len(allIdx)} more results...")

  if choice == "q":
    print("Exiting...")
    exit()