# Spiderman and Jumping

N buildings are built in a row, numbered 1 to N from left to right. Spiderman is on buildings number 1, and want to reach building number N. He can jump from building number i to building number j iff i < j and j-i is a power of 2 (1,2,4, so on). Such a move costs him energy |Height[j]-Height[i]|, where Height[i] is the height of the ith  building. Find the minimum energy using which he can reach building N?

## INPUT

First line contains N, number of buildings. Next line contains N space-separated integers, denoting the array Height.

## OUTPUT

Print a single integer, the answer to the above problem.

## CONSTRAINTS

    1≤N≤200000  
    1≤Height[i]≤109

## SAMPLE INPUT

    4  
    1 2 3 4

## SAMPLE OUTPUT

    3
