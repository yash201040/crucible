# Task: a long deterministic simulation

A machine has a state (a, b, c) of non-negative integers. It starts at (1, 2, 3). One step replaces the state by
(a2, b2, c2), computed in this order:

1. a2 = (a*a + b + 13) mod 1009
2. b2 = (b + c*a2) mod 1013            (this uses the NEW value a2 and the OLD value c)
3. if (a2 + b2) is even: c2 = (c + 5) mod 31, otherwise: c2 = (c*3 + 1) mod 31

Let N = 10^18 (one quintillion).

Report:
(i) the state after exactly N steps, and
(ii) the number of steps t with 1 <= t <= N such that a == 0 in the state right after step t.

Give the final answer as the string "a,b,c,count" (four integers separated by commas, no spaces).
Verify your method before answering: for example, compare it with a direct simulation for small step counts.
Report the checks you ran.
