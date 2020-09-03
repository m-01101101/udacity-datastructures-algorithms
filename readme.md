# Data Structures & Algorithms

Notes and work from Udacity's [Data Structure's and Algorithm's nanodegree](https://www.udacity.com/courses/data-structures-and-algorithms-nanodegree)

At its core, this program is about how to write code to solve problems and to do so efficiently.

Algorithms are the instructions, the things we want the computer to do. It's how we process the inputs and the outputs. Data structures are how these inputs and outputs are presented.

> Inputs > Algorithms > Output
 
The essence of a good algorithm is its ability to scale with the problem.

## On thinking

If, like me, you have little background in programming or writing software, then it helps to have a way of thinking how to approach the task at hand. Staring at a blank ~canvas~ test editor can be daunting, you know the problem and have some intuition of how you'd solve the problem. However, converting that into code, the translation of thought to function, can be tricky.

One piece of advice I was given to build a natural programming workflow was to write out instructions for making a peanut butter and ~jelly~ jam sandwich.

Here is my attempt. *I tried to think what these things would mean in terms of code, obviously they are nonsense and more for illustrative purposes.*

(1) Get ingredients.

```python
ingredients = ['bread', 'peanut butter', 'jam']
```

(2) Get knife.

```python
class Slicer:
    def __init__(self):
        self.knife

    def slice

knife = Slicer()
```

(3) Slice bread.

```python
def cut_bread(Slicer, thing_to_slice) -> sliced_bread, sliced_bread:
    sliced_bread = slicer.slice(thing_to_slice)

    return sliced_bread, sliced_bread

sliced_bread1, sliced_bread2 = cut_bread(knife, ingredients[0])
```

(4) At this point I'm aware you could toast the bread, you can weight the peanut butter and jam, depending on where you lie on the scale of artist versus scientsit. You could heat the peanut butter, maybe you want a different texture. However, we'll go with "spread peanut butter and jam"

```python
def spread(thing_to_spread, thing_to_spread_on) -> thing_smoothered_in_spreaded_thing:
    return thing_to_spread_on * thing_to_spread

smoothered_bread1 = spread(ingredient[1], sliced_bread1)

smoothered_bread2 = spread(ingredient[2], sliced_bread2)
```

(5) Construct sandwich. Place the two bits of bread together basically.

`final_sandwich = smoothered_bread1 + smoothered_bread2`

We could go on, (6) serve, (7) eat...

## The process, thinking backwards

- Construct a mental model what we want to happen
- Break that mental model down into steps
- Walk back through those steps in our head to verify it's all accurate and we're not missing anything
- Record instructions for the computer to use
- Run the program on the computer
- Compare the result we expected from our mental model with the result from the computer
- If they align, then we are done! =D
- If they don't align, then we need to troubleshoot to find out what caused the issue. 

This can be:

  - We wrote something wrong when converting our instructions into computer instructions (e.g. referenced "bag of bread" instead of "slice of bread")
  - We're using the wrong function/method for something (e.g. if someone used "slice" instead of "spread)
  - Our mental model missed an edge case (e.g. peanut butter on the "top" of the slice of bread)
  - Something else

The best way to build this skill is to build it like a muscle. Keeping on using it and flexing it over time

Eventually you get faster and faster with more abstractions and more intuition around how to build something -- Todd Wolfson

For a fun illustration, watch the video below. The point is, there is no room for ambiguity.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/cDA3_5982h8/0.jpg)](https://www.youtube.com/watch?v=cDA3_5982h8)
