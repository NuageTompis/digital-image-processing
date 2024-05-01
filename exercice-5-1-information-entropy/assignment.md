## Task

> Calculate information entropy in case of the situation you encounter commonly, and consider the increase and decrease of the information entropy when the occurrence probability changes. 

I considered the situation where we roll 4 dice, and check whether there is at least one die that rolled to a *6*.

Then we will remove a die and consider the same question, and look at the entropy difference.

> Note: this scenario is inspired from a board game which I often play with my friends.

The probability of rolling at least one die on *6* amongst 4 dice, which we shall write $p_4$, is equal to $1-p_4'$, where $p_4'$ is the probability of rolling no *6* in the set.

We can compute $p_4'$ with ease (assuming that the dice are fair): $p_4' = (\frac{5}{6})^4$. Thus we can express $p_4$:

$p_4 = 1 - (\frac{5}{6})^4 \approx 0.52$

Similarly we have $p_3 = 1 - (\frac{5}{6})^3 \approx 0.42$ for the second situation.

Thus, the entropy for the variable $X$ which states whether or not we rolled a *6* within $n$ dice can be expressed (in base 2) as the following:

$S_n(X) = -\sum_{i=1}^{N}{p_ilog_2(p_i)} = - p_nlog_2(p_n) - (1-p_n)log_2(1-p_n)$

Using this formula, I obtain $S_4(X) \approx 0.999$ and $S_3(X) \approx 0.982$.

We can see that $S_3 < S_4$, which *means* that asking the question `did we roll a six amongst four dice` retrieves less information that asking the question for three dice.