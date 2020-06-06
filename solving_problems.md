# How to solve problems

How to approach more complicated programming problems. Equally, this can be applied as mental models to more general problems.

Start with making sure you understand the problem.

Don't just jump in.

All computational problems have (1) inputs and (2) desired outputs

The problem is generally defined by a set of possible inputs (infinite for interesting problems).

The solution is a procedure that can take any input in that set and produce the desired output -> this is a very discrete computer science way of looking at things, but the principle generally holds. It's about understanding the relationship and the procedure (what has to happen to inputs to create desired outputs).

Start with;
(1) What are the inputs? 

- How general is the problem, should the procedure work for just the given inputs or more general scope?
- What are the assumptions in are inputs? What do we consider valid/invalid?
- Defensive programming -> we write code to force check that our assumptions are true
- How are the inputs represents? Often it's up to you to decide how to encode the inputs. This is one of the most important decisions you'll make in solving the problem.

(2) What are the outputs?

- How do we want to present the output?
- How do this output be used in a wider context?
- What decisions are being made with this output?

(3) Solving the problem

- Work with some examples, essentially test cases to understand the relationship and what to expect. Build an intuition for the problem.
- Consider systematically how to solve the problem
- Write your logic/algorithm in pseudo-code
- Once you can see the logic, ask yourself, can you solve this in a simpler way. Is there more elegance, patterns that you can make explicit now you have visualised your logic?
- What edge cases will your logic not handle correctly?
- Don't optimise prematurely. Focus on simplicity and completeness.
- Write small bits of code that you can test independently as you go.

(4) Develop a solution incrementally

- Decompose and test as you go
- Dan Bader;
    > Orwell said “all writing is re-writing.” There is never a “perfect” first draft. 
    > <br>Equally, “all programming is re-programming.”
    > <br>Or as Kent Beck (the Test-Driven Development guru) put it:
    > <br>“Make it run, make it right, make it fast.”
    > <br>This is really a mantra to live (to program) by.

Notes from thinking backwards.

Yan Le Cunn's three types of wrong;

Decomposition

Orwell; “All writing is re-writing.” There’s never a “perfect” first draft.
Equally, “all programming is re-programming.”
Or as Kent Beck (the Test-Driven Development guru) put it:
“Make it run, make it right, make it fast.”
This is really a mantra to live (to program) by.