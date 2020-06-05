---
layout: default
---

# Theory
The game was built using the model of manipulative lying proposed by Wang et al.(2011), which is based on the logic of communication and change by Benthem et al. (2005). Communication between agents implies changes in the world and the knowledge of agents. The communication takes place as actions in an epistemic model, hence influencing knowledge and belief of the agents. The actions in our game are public announcements made by the players.

## Lying in public announcements
The public announcement in our game follow deception and manipulating the other agents into believing a lie. Generally, if an announcement ![phi](https://latex.codecogs.com/svg.latex?%5Cphi) is made, then the belief of each agent is rightly updated to ![phi](https://latex.codecogs.com/svg.latex?%5Cphi), and similarly for ![negphi](https://latex.codecogs.com/svg.latex?%5Cneg%20%5Cphi). In manipulation however, the agent lies that and misleads the public to believe ![phi](https://latex.codecogs.com/svg.latex?%5Cphi). So, there are two possible annoucement actions:
* Announcing ![phi](https://latex.codecogs.com/svg.latex?%5Cphi) when it is true, hence all updates are true
* Lying ![phi](https://latex.codecogs.com/svg.latex?%5Cphi) is true when it is false, hence manipulating the public's belief

## Axioms of lying
Taking the notations defined by Wang et al.(2011), lying is denoted as ![lie](https://latex.codecogs.com/svg.latex?%5Ctextexclamdown%20%5Cphi) and truthful public annoucement as ![true](https://latex.codecogs.com/svg.latex?%21%20%5Cphi). Together, the two are referenced as manipulative update ![manipulate](https://latex.codecogs.com/svg.latex?%5Cddagger%20%5Cphi).

The axioms of manipulative update are the KD45 axioms system with the rules for belief ![belief](https://latex.codecogs.com/svg.latex?B_i). The axioms for lying are as follows:
* ![axiom1](https://latex.codecogs.com/svg.latex?%5B%5Ctextexclamdown%20%5Cphi%5D%20%5Cpsi%20%5Cleftrightarrow%20%5Cneg%20%5Cphi%20%5Crightarrow%20%5Cpsi)
* ![axiom2](https://latex.codecogs.com/svg.latex?%5B%5Ctextexclamdown%20%5Cphi%5D%20%5Cneg%20%5Cpsi%20%5Cleftrightarrow%20%5Cneg%20%5Cphi%20%5Crightarrow%20%5B%5Ctextexclamdown%20%5Cphi%5D%20%5Cneg%20%5Cpsi)
* ![axiom3](https://latex.codecogs.com/svg.latex?%5B%5Ctextexclamdown%20%5Cphi%5D%20%5Cneg%20%28%5Cpsi_1%20%5Cland%20%5Cpsi_2%29%20%5Cleftrightarrow%20%5B%5Ctextexclamdown%20%5Cphi%5D%20%5Cpsi_1%20%5Cland%20%5B%5Ctextexclamdown%20%5Cphi%5D%20%5Cpsi_2)
* ![axiom4](https://latex.codecogs.com/svg.latex?%5B%5Ctextexclamdown%20%5Cphi%5D%20B_i%20%5Cpsi%20%5Cleftrightarrow%20%5Cneg%20%5Cphi%20%5Crightarrow%20B_i%20%5B%21%20%5Cphi%5D%20%5Cpsi)

