# 7. Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the
# age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or
# young if they are above or below the average age.

lst = [('sushmita', 'rai', 21), ('ashmita', 'pradhan', 25), ('salina', 'thapa', 27), ('sitosma', 'bahadur', 31),('silpa','shetty',None)]

summation = 0
for item in lst:
    if item[2] is not None:
        summation += item[2]
    avg = float(summation/len(lst))
for item in lst:
    if item[2] is not None and float(item[2]) < avg:
        print("{} {}, young.".format(item[0], item[1]))
    elif item[2] is not None :
        print("{} {}, old.".format(item[0], item[1]))
    else:
        print("{} {}, unknown age.".format(item[0], item[1]))
