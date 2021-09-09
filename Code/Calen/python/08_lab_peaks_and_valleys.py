'''
Peaks and Valleys
Define the following functions:

peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Visualization of test data:

Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
POI							P			V					P			V			
Example I/O:

                                                  X                 X
                                               X  X  X           X  X
                          X                 X  X  X  X  X     X  X  X
                       X  X  X           X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks(data) # [6, 14]
valleys(data) # [9, 17]
peaks_and_valleys(data) # [6, 9, 14, 17]
'''

from typing import get_args


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data: list) -> list:
   ''' This function is designed to return a peak as defined by having lower ints surrounding its current index in a list '''
   return_data = []
   for i in range(len(data)-1):
      
      if i == 0:
         pass # perform no action as you cannot be a valley being index 0
      
      elif i == len(data)-1:
         pass # perform no action if I is equal to final item in list. this will halt index errors and keep from running checks on final item

      elif data[i] > data[i-1] and data[i] > data[i+1]:
         return_data.append(i)

   return return_data


def valleys(data: list) -> list:
   ''' This function will return any valleys in a list of ints, where a valley is identified by having higher int values surrounding its index '''

   return_data = []
   
   for i in range(len(data)-1):

      if i == 0:
         pass

      elif i == range(len(data)-1):
         pass

      elif data[i] < data[i+1] and data[i] < data[i-1]:
         return_data.append(i)

   return return_data


def peaks_and_valleys(data: list) -> list:
   ''' This function will return a list of two lists containing all peaks and index 0 and valleys at index 1 '''
   return [peaks(data), valleys(data)]


'''
Version 2 (optional)
Using the data list above, draw the image of X's above.

Hint 1: If you wanted to draw this horizontally, you could do so very easily like this.

for num in data:
    print('x' * num)
Hint 2: print can only work on one line at a time, so you'll have to loop and decide to either print a space ' ' or an 'X' for every column
'''


def horizontal_graph(data: list, format='print') -> None:
   ''' this function will convert a list of ints into a plotted graph horizontally '''
   i = len(data)-1
   big_list = []
   while i > -1: # inclusive of zero this way

      horizontal_data = []
      for num in data:
         if num >= i:
            horizontal_data.append('x')
         else:
            horizontal_data.append(' ')
      big_list.append(horizontal_data)
      i -= 1

   if format == 'print':
      for slice in big_list:
         print(slice)
   else: 
      return big_list


'''

Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected, and if you can, draw the following diagram.

                                                  X  O  O  O  O  O  X
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

'''

def calc_water_fill(data: list) -> int:
   ''' this function will take in a list of data, and plot it, presenting you with peaks, valleys, and how much liquid can be stored in them '''
   water_volume = 0
   graph = horizontal_graph(data, 'return')
   # this returns a list of lists with graph data

   for upper_index in range(len(graph)):
      for lower_index in range(len(graph[upper_index])):
         if graph[upper_index][lower_index] == ' ':
            left = list(graph[upper_index][:lower_index])
            right = list(graph[upper_index][lower_index:])
            if 'x' in left and 'x' in right:
               graph[upper_index][lower_index] = 'o'
               water_volume += 1


   return water_volume, graph

water_volume, graph_data_unsliced = calc_water_fill(data)

print(f'Your data can hold {water_volume} units of water.')
for slice in graph_data_unsliced:
   print(slice)

