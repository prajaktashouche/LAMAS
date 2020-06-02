# Rules
 > The goal is to be the first player to get rid of all their cards. When a player puts their last card on the table and either is not doubted or, upon being doubted, is shown to have announced correctly, they win the game

 \- [Bicycle Cards website](https://bicyclecards.com/how-to-play/i-doubt-it/)
 
A detailed description of the game can be found on the reference website. 

# Restrictions
In our implementation of the game, we use a smaller version to simplify the game mechanics as follows:
* players in the game can be between 2-10 but we only consider 3 players 

* original deck size of 52 cards is reduced to 6 cards where the value is from Ace, 2, and 3 with 2 cards each of suit heart and spades. This way each player gets 2 cards each.

We implemented one play of game, where each player gets 2 cards. Each player puts either one or both cards face down and makes an annoucement about the value of the cards. The other players can either doubt this announcement, based on their current knowledge and common knowledge, or update their knowledge and make a decision about their strategy to play. 