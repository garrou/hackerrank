# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n: int) -> None:
    for i in range(1, n + 1):
        print(('#' * i).rjust(n))

"""
input : 6

     #
    ##
   ###
  ####
 #####
######
"""