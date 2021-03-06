---
layout: default
---

This project is done as part of the course **Logical Aspects of Multi-Agent Systems** at the University of Groningen. It is done in collaboration with the following students:

Shaniya Hassan Ali, Prajakta Shouche, Andrei Miculita & Vinayak Prasad

# Introduction

The card game **I Doubt it**, also popularly known as “Bluff” is a multiplayer game. The goal of each player is to get rid of all of their cards. It is a game where the ability to deceive other players at the same time detect other player's deception comes into play. Each player gets to place some cards face down, and make an announcement which need not be true. Decision needs to be made based on previous knowledge as well as the last player’s announcement to call out a bluff or not. The dynamic of lying makes the game an interesting one to analyze from the perspective of player’s knowledge, common knowledge, belief and public announcement logic.

# Rules

 > The goal is to be the first player to get rid of all their cards. When a player puts their last card on the table and either is not doubted or, upon being doubted, is shown to have announced correctly, they win the game

 \- [I Doubt It Official Rules](https://bicyclecards.com/how-to-play/i-doubt-it/)

A detailed description of the game can be found on above referenced website.

# Restrictions

In our implementation of the game, we use a smaller version to simplify the game mechanics as follows:

* players in the game can be between 2-10 but we only consider three players

* original deck size of 52 cards is reduced to 6 cards where the value is from Ace, 2, and 3 with two cards each of suit heart and spades. This way each player gets two cards each.

* put down only one card at each turn 

With the imposed restrictions the Kripke model consists of 90 possible worlds and 5400 relations.
<center><img src="assets/images/formula.png" align="center" height="100" width="500"></center>

We show multiple plays of the game, where each player gets two cards. Each player puts one card face down and makes an announcement about the value of the card. The other players can either doubt this announcement, based on their current knowledge and common knowledge, or update their knowledge and make a decision about their strategy to play.
