# gol
Game of life in python

init:
  size = ((20,20) Default) array 1x2, (width,height)
  random = (True Default) bool, creates a random population if true
  

next_gen()
  evolutes the next generation according to the gol's rules
  ite = (1 Default) int, number of evolutions
  show = (True Default) bool, shows the evolution of the grid if true
  time = (0.1 Default) float, time between each frame or evolution (in seconds)
  
reset()
  creates a new grid with random population
  
show_grid()
  shows the grid
  
  
sample code in console:
>>from gol import GoL
>>mycells = GoL((50,50),True)
>>mycells.next_gen(500,True,0.03)
