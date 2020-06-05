---
layout: default
---

# Example

Suppose we have 3 players: Alice, Bob and Carol. The deck consists of 🂡 🂢 🂣 🂱 🂲 🂳. At the beginning of the game, each player is given two cards at random from the deck. Suppose:
 * Alice gets 🂡 and 🂳, 
 * Bob gets 🂢 and 🂣,
 * Carol gets 🂱 and 🂲.

Alice places down 🂡 and truthfully announces she has put down an ace. Bob could doubt, however neither of his cards are aces, so he believes it would be wise not to. Carol could also doubt, since she has the 🂱, however she does not know whether it is Alice or Bob has the 🂡, so she waits. As neither has doubted, Bob can now infer that Carol does not have 2 aces, and Carol can infer that Bob does not have 2 aces.

 State:
 * Alice: 🂳
 * Bob: 🂢🂣
 * Carol: 🂱🂲
 * Cards down: 🂡

Bob places down 🂣 and lies that he has placed down a 2. Alice chooses not to doubt, as she does not own any 2s. Carol does not doubt either, as she does not have both 2s. But now, again, as neither of them has doubted, Alice and Carol both know that the other does not have both 2s.

 State:
 * Alice: 🂳
 * Bob: 🂢
 * Carol: 🂱🂲
 * Cards down: 🂡🂣

Carol must now place down one or more 3s. However, she does not have any, and so she places down 🂱 and lies that she has put down a 3.

 State:
 * Alice: 🂳
 * Bob: 🂢
 * Carol: 🂲
 * Cards down: 🂡🂣🂱

Alice must once again place down an ace. She places down her 🂳. However, Carol has just put down her ace, so now she knows that either Alice was lying the first round, or she is lying now. She decides to doubt her. The last card in the stack is now turned face up, and it is indeed revealed that Alice was lying. Alice now takes all the 4 cards in the stack into her hand. By Carol announcing the doubt, now Alice and Bob are informed of the fact that Carol either has an ace, or put down an ace in the previous round.

 State:
 * Alice: 🂡🂣🂱🂳
 * Bob: 🂢
 * Carol: 🂲
 * Cards down: 
 
Once Alice takes the stack, she knows that Carol no longer has that ace, since both aces were in the stack. What's more, Alice actually knows that both Bob and Carol have 2s, since all the aces and 3s are now in her hand.

And so on...