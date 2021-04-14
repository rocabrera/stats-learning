# Expected Value

Let $X$ be a random variable with a finite number of finite outcomes $X = (x_1, x_2, ...x_k)$ occurring with probabilities $(p1,p2, ..., p_k)$. The **expectation** of **X** is defined as:

​			
$$
\begin{equation} E[X] = \sum_i^k x_ip_i \end{equation}
$$

#### Example 1 - Fair Coin:

The outcomes are $X = (0,1)$ and all outcomes have the same probability $p_i = \frac{1}{2}, \forall i \in Outcomes$.
$$
\begin{equation} E[X] = \sum_{i=0}^1 ip_i = \frac{1}{2}\sum_{i=0}^1 i = \frac{1}{2}(1) = 0.5\end{equation}
$$

#### Example 2 - Fair Die:

The outcomes are $X = (1,2,3,4,5,6)$ and all outcomes have the same probability $p_i = \frac{1}{6}, \forall i \in Outcomes$.
$$
\begin{equation} 
E[X] = \sum_{i=1}^6 ip_i = \frac{1}{6}\sum_{i=1}^6 i = \frac{1}{6}(21) = 3.5
\end{equation}
$$


---

# Variance

The variance of a random variable $X$ is the **expected value **  of the squared deviation from the **mean**:
$$
\begin{equation} 
Var(X) = E[(X-\mu)^2] = E[X^2] - E[X]^2, \text{ where } \mu = E(X)
\end{equation}
$$

Proof:

- $E$ is a linear function:

$$
\begin{align}
E[(X-E[X])^2] = E[X^2 - 2E[X]X +E(X)^2] = E[X^2] + E[-2E[X] X] + E[E[X]^2]
\end{align}
$$



- The $E[X]$ is a number, therefore $E[X]^2$ is also a number. The expected value of a number is the number itself. So $E[E[X]^2] = E[X]^2$:
  $$
  E[X^2] + E[-2E[X] X] + E[X]^2
  $$

$E$ is a linear function (Constant multiplication) $c = -2E[X]$:
$$
E[X^2] + E[cE[X]] + E[X]^2 = E[X^2]  + cE[E[X]] + E[X]^2
$$
Same argument as before $E[E[X]] = E[X]$, therefore:
$$
E[X^2] + cE[X] + E[X]^2 = E[X^2] -2E[X]E[X] + E[X]^2
$$
Finally:
$$
E[X^2] -2E[X]^2 + E[X]^2 = E[X^2] - E[X]^2
$$




