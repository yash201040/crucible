# Technical report TR-2026-17 (excerpt): Parallel candidates versus sequential repair

## 4. Results

We compare two ways of spending a fixed number of model calls on a failing software task. In SEQ, one agent
repairs its own patch for up to six rounds, each round seeing the test output of the previous one. In PAR,
after the second failed round we stop the sequential loop and start four independent candidates, each given a
two-sentence summary of what failed; a selector then picks one candidate by running the project's tests.

Table 2. Resolve rate on the 500-task verified subset (percent of tasks resolved).

| Model   | SEQ  | PAR  | Change |
|---------|------|------|--------|
| Large-A | 70.9 | 77.6 | +6.7   |
| Large-B | 68.2 | 73.0 | +4.8   |
| Mid-C   | 55.4 | 58.9 | +3.5   |
| Small-D | 31.0 | 29.8 | -1.2   |

PAR improved the resolve rate for three of the four models. For Small-D it was slightly worse: its candidates
often failed in the same way, and the selector had little to choose from. We did not test whether the Small-D
difference is statistically significant.

Cost. PAR used more calls on the tasks that reached the parallel stage. Averaged over all tasks, the cost per
task was 3.1 times that of SEQ for Large-A and between 2.4 and 3.3 times for the other models. Wall-clock time
per task fell by 38 percent for Large-A because the candidates ran at the same time.

## 5. Limitations

All tasks come from one benchmark of Python repositories. The selector relies on the project's own tests, so
the result may not carry over to tasks without an executable check. Each configuration was run once.
