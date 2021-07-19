# Description 
This the first of a series of coding challenges. 

AI Learning Program Challenge 01 - Your Personal Sorting Hat with Python

## Purpose
New semester is coming! There will be tons of freshmen crowding into the Hogwarts.
We need to group them into several groups/teams for teaching, accommodation and competing.
As a AI wizard, it's time for you to create a sorting hat!

**Step 1**
Create your own categories for grouping students. The following we take Hogwarts for example.

| key | value      |   
|-----|------------|
| a   | Ravenclaw  |   
| b   | Slytherin  |
| c   | Hufflepuff |
| d   | Gryffindor |

**Step 2**
Sequentially ask 5 questions, each question includes 4 options, each option maps to one house
ex. 
Q1. You enter a magical garden. What do you look at first?
a. Luminous Pool with something in its depths
b. Statue with a twinkling eye
c. A silver tree with golden apples
d. Talking Toadstools
input>>> d
as the input from user is "d", add 1 point to house that has d as key, that is Gryffindor, the result is as listed in table below.

| key | value      | Q1 | Q2 | Q3 | Q4 | Q5 |
|-----|------------|----|----|----|----|----|
| a   | Ravenclaw  |  0 |    |    |    |    |
| b   | Slytherin  |  0 |    |    |    |    |
| c   | Hufflepuff |  0 |    |    |    |    |
| d   | Gryffindor |  1 |    |    |    |    |




**Step 3**
After answering all of those 5 questions, calculate which house got the highest score and print out the house name
if house can not be determined, print message and tell user.

| key | value      | Q1 | Q2 | Q3 | Q4 | Q5 | Total |
|-----|------------|----|----|----|----|----|-------|
| a   | Ravenclaw  |  0 | 1  |  0 |  1 |  0 |   2   |
| b   | Slytherin  |  0 | 0  |  1 |  0 |  0 |   1   |
| c   | Hufflepuff |  0 | 0  |  0 |  0 |  1 |   1   |
| d   | Gryffindor |  1 | 0  |  0 |  0 |  0 |   1   |


output>>> Ravenclaw


# Requirements 
* Python 3.6 or higher

# How to run 

```
python main.py 
```
