# Best-empty-space-to-put-a-kitchen-in
Updated BFS algorithm via Python

You are given a building floor map like so:

WWWWWWWWWWWWW
W E   W E   W
W	W	W
W           W
W	W     W
W E	W E   W
WWWWWWWWWWWWW

W - wall
E - employee
[SPACE] - empty space

You need to find the best empty space to put a kitchen in.
The kitchen needs to be located in the empty space for which the sum of distances
to all employees is minimal.
The distance from an empty space to an employee is the shortest path from the employee
to the empty space.
Employees can only walk in north, south, east or west directions (no diagonals).
Employees cannot walk through walls (of course).

Write a program that receives as input a file with the floor
plan and outputs the best kitchen location.
If the floor plan does not allow for a kitchen (for example if the floor
plan does not allow some employees to reach some spaces) then state that it is so.
We recommend using python but any programming language can do.
If you are not proficient in programming write pseudo-code
and explain your algorithm.
Try to make the algorithm as efficient as possible.
Googling for a solution for this specific riddle is not allowed.

Good luck!
