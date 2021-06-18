#we will be using pylab for module 7 homework, I thought it would be a good idea to go ove it
import pylab as plt

#mathplot library is the whole library pylab is mathplot + numpy

#lets plot some numbers
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x,y, 'r-') #plots x vs y with a red line
plt.ylabel('y') #labels y
plt.xlabel('x') #lables x
#we can save the chart by doing
plt.savefig('my_chart.png')
#we can show the chart by doing
plt.show() # shows tplot



#linetypes include 
# - , –, -., , . , , , o , ^ , v , < , > ,
#  s , + , x , D , d , 1 , 2 , 3 , 4 , h , H , p , | , _

#colors include
#b, g, r, c, m, y, k, w


#there is more to pylab so please see the mathplot documentation