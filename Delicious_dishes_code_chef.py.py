﻿"""
Chef is the owner of the loveliest restaurant in ChefTown.
To make his work easier, all dishes are numbered by distinct positive integers, and you can order with this positive integer in Chef’s restaurant.
Amazingly Chef has many kinds of recipes, so every positive integer denotes exactly one dish.
To taste dish numbered with some integer C, you have to pay exactly C dollars.
Unfortunately not all the dishes are delicious.
After years of working in his restaurant, Chef discovered that a dish is considered to be delicious if the number that denotes this dish consists of different digits.
Let’s call such numbers “delicious numbers”.
For example numbers 123, 1, 91, 102 are delicious but 122, 11, 900 are not.
Ira is a little girl from the University of Lublin and she’s fond of traveling.
Tonight she stops in ChefTown and wants to have a meal at Chef’s restaurant.
On the one hand she has R dollars in her pocket and she is ready to spend it, on the other hand she wants to seem rich, so she won’t spend less than L dollars.
Of course, since she is a little girl, she wants to order just one dish.
It is difficult to make a choice for Ira because of variety of dishes.
Now she asks you to find out the number of delicious dishes Ira may order, considering her conditions.

Input
First line contains single integer T (1 ≤ T ≤ 200000) – the number of test cases. Each test case consists of two positive integers in a line - L and R (1 ≤ L ≤ R ≤ 1018).

Output
For every test case, output the answer on a separate line.
"""
import sys

in_ = raw_input().replace("\n","").split()
T = int(in_[0])

if T>=1:
    for case in range(0,T):

        if case>=200000:
            break
        
        in_ = raw_input().replace("\n","").split()
        start = int(in_[0])
        end = int(in_[1])

        input_range = range(start,end+1)

        cnt=0
        for no in input_range:
            no=list(str(no))
            
            for n in no:                    
                c=no.count(n)           
                if c>1:
                    cnt+=1
                    break

        print len(input_range)-cnt
