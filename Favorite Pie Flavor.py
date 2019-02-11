import numpy as np
import matplotlib.pyplot as pp
import matplotlib.pyplot as pp; pp.rcdefaults()

#This data from our survey!
x = ['Cherry', 'Pecan', 'Apple', 'Pumpkin', 'Peach', 'Other']
y_pos = np.arange(len(x))
y = [4, 16, 14, 9, 1, 5]

#Use barh if you want a horizontal bar chart
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
pp.bar(y_pos, y, align='center', color=colors)
pp.xticks(y_pos, x)
pp.ylabel('Responses')
pp.xlabel('Pie Flavors')
pp.title('Favorite Pie Flavor')
pp.show()
