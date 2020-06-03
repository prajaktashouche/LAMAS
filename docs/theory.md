---
layout: default
---

# Theory
The game was built using the model of manipulative lying proposed by Wang et al.(2011), which is based on the logic of communication and change by Benthem et al. (2005).Communication between agents implies changes in the world and the knowledge of agents. The communication takes place as actions in an epistemic model, hence influencing knowledge and belief of the agents. The actions in our game are public annoucements made by the players.

## Lying in public announcements
The public annoucement in our game follow deception and manipulating the other agents into believing a lie. Generally, if an annoucement $\phi$ is made, then the belief of each agent is rightly updated to $\phi$, and similarly for $\neg \phi$. In manipulation however, the agent lies that and misleads the public to believe $\phi$. So, there are two possible annoucement actions:
* Announcing $\phi$ when it is true, hence all updates are true
* Lying $\phi$ is true when it is false, hence manipulating the public's belief

## Axioms of lying
Taking the notations defined by Wang et al.(2011), lying is denoted as $\textexclamdown phi$ and truthful public annoucement as $! \phi$. Together, the two are referenced as manipulative update $\ddagger \phi$. The axioms of manipulative update are the KD45 axioms system with the rules for belief $B_i$. The axioms for lying are as follows:
* $[\textexclamdown phi] \psi \leftrightarrow \neg \phi \rightarrow \psi$
* $[\textexclamdown phi] \neg \psi \leftrightarrow \neg \phi \rightarrow [\textexclamdown phi] \neg \psi$
* $[\textexclamdown phi] \neg (\psi_1 \land \psi_2) \leftrightarrow [\textexclamdown phi] \psi_1 \land [\textexclamdown phi] \psi_2$
* $[\textexclamdown phi] B_i \psi \leftrightarrow \neg \phi B_i [\textexclamdown phi] \psi$