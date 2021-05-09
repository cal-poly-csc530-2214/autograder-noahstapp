# Autograder

I decided to write a much much simpler version of the entire original code to automated feedback pipeline, as described in the paper. Due to time constraints, I limited my space to simple algebraic equations of form similar to

```math
x = 2
1 + 2 + x == 6
```

I also limited my corrections to rules such as x -> x, x - 1, x + 1, suggesting that every occurence of x in the given equation should be replaced with one of itself, x + 1, or x - 1. By limiting both the program space and correction space to this very simple algebraic one, implementing the full pipline was achievable in just over four hours.

## Process
First, a list of corrections, a list of variable assignments, and an algebraic equation are specified in the main() function of the translator_algebra.py file. Then, the corrections and assignments are transformed into mappings for efficient substitution. Then, the corrections are applied to the equation to give a human-readable representation of the equation with all possible choices for each variable. Next, the corrections are translated to sketch functions, with each possible choice being a different if branch conditional on a sketch ?? hole. The assignments are translated into calls of these correction functions, passing in the assigned value as the argument. Finally, the equation is made into a sketch assert statement, and the completed sketch program is written out to a .sk file. 

Sketch is then run on the translated file, outputting the synthesized C++ code that solves the equation using the given corrections. Automated feedback is given by parsing this output C++ file and seeing what corrections were chosen, representing what should change in the original program's assignments to make the equation solvable.

An example input and output is given below:

```
corrections = ["n -> n, n - 1, n + 1", "m -> m, 2 * m, 3 * m"]
vars = ["n = 4", "m = 4"]
program = "1 + 2 + 3 + m + n == 23"

python3 translator_algebra.py

("n -> n, n - 1, n + 1"), ("m -> m, 2 * m, 3 * m")
n = 4, m = 4
1 + 2 + 3 + m + n == 23 -> 1 + 2 + 3 + {4, 2 * 4, 3 * 4} + {4, 4 - 1, 4 + 1} == 23
SKETCH version 1.7.6
Benchmark = translated.sk
[SKETCH] DONE
Total time = 335
Original program:
	n = 4
	m = 4
	1 + 2 + 3 + m + n == 23
Corrections:
	The value of n should be 4 + 1 instead of 4
	The value of m should be 3 * 4 instead of 4
```