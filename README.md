# MTGHands
tldr: Compute mtg hands probabilities

## Why ?
In general, when you ask someone what's the classic hand of their hand, they often give the golden hand as an answer, that perfect line that occurs 1% of the time.

## What ?
The tool will compute all the possible hands of the deck with their probability, sorted.
It allows multiple things:
- Know which hands are the most common in your deck so you can train those particular hands
- Prepare yourself before a tournament, like "this hand I keep, this one I don't, against this mu I need a more agressive mulligan, what are the probabilities of a better hand ?" ...
- Build your deck while looking at potential hands, verify that a "risky" choice isn't out too often, or that your manabase doesn't color death too often

## How ?
L'utilisation:
- You need to save your deck under a file name "deck.mtgo"
-> Double click on the software (HandComputation.exe)
-> It will generate a file called lines.txt with the computed lines
![image](https://github.com/AxelLavielle/MTGHands/assets/12008266/90e328ad-96cd-47b3-937e-ed0dfcdbacbb)

Preview of some lines of a deck:
![image](https://github.com/AxelLavielle/MTGHands/assets/12008266/cfdb4513-5f61-45ba-93de-dc92f16787f1)

## Few details / recommendations
- The probabilities are in 100 000 (for ex, a 17.xxx means 17.xxx/100 000), if you wonder why, the answer is simple, there is 386 206 920 possible hands with a 60 cards deck, 16 007 560 800 with a 100 cards deck, therefore, the unique starting hands are plenty (for my deck, 71 620 different hands). The probabilities are pretty low anyway for any hand.
- In the .mtgo, you can't have more than 12 copy of a card. (something like 16 island will fail). I use factorials in the calculs, and 13! > size of integer (6 227 020 800 > 2 147 483 647) therefore I can't stock it. In the case you use 12+ copy of a card, you just have to separate it in two stacks (like 12 islands and 4 islands if you have 16 islands). In the results, they will be considered as different, but I trust you will understand that 2x island | 1x island = 3x island.
- I don't care about the number of cards in the deck, you can build with 120 cards if you want
- The more differents cards there is in the deck, the more time it takes to make the lines, the probabilites and the writing. That's perfectly normal, it needs to compute more variants. On my pauper deck it takes ~3s to run. Also understand that it's not useful to compute hands with 1 copy of each card (like a singleton format), spoiler alert: every card has the same possibility.
- Please feel free to share the software, of upgrade it ! It is probably badly coded, but I made it opensource that way you can be sure there is no virus in the code, if you're suspicious, read the code, compile it yourself and run it on a virtual machine !
- It doesn't handle the sideboard, but you can change your cards in the file and relaunch the softwware to compute new lines
- I recommand grouping some lands to have fewer hands, for example, if you have 4 Waterfront District and 4 Contaminated Aquifer, call them 8 DimirBilandTap, you will drasticly reduce the number of hands and will have more relevant results
