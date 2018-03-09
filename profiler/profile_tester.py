import cProfile
from profiler.examples.example_functions import increase_by_1_loop,increase_by_1_list_comp

dummy_list=list(range(0,10000))

cProfile.run('increase_by_1_loop(dummy_list)', filename='first_iteration.cprof' )
cProfile.run('increase_by_1_list_comp(dummy_list)', filename='second_iteration.cprof' )
