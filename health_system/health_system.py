# HEALTH MONITORING SYSTEM 
# Created by : Sahana Muralikrishnan
 
import turtle
from turtle import Turtle,Screen


def get_pulse():
	""" gets pulse values from user """

	pulse1 = int(input("Enter pulse value : "))		
	pulse2 = int(input("Enter pulse value : "))
	pulse3 = int(input("Enter pulse value : "))	
	return(pulse1, pulse2, pulse3)

def average_pulse(p1, p2, p3):
	"""Accepts 3 pulse values and returns average pulse"""

	if p1 <= 0:
		return None
	elif p2 <= 0:
		return None
	elif p3 <= 0:
		return None
	else:
		average = round((p1 + p2 + p3)/3,2)
		print("Average pulse is : ", average)
		return(round(average,1))

def abnormal_pulse(avg1, avg2, avg3, avg4):
	""" Accepts 4 averages and return abnormal pulse """
	
	if avg1 < 60 or avg1 > 90:
		return(1)
	elif avg2 < 60 or avg2 > 90:
		return(2)
	elif avg3 < 60 or avg3 > 90:
		return(3)
	elif avg4 < 60 or avg4 > 90:
		return(4)
	else:
		return None

def warning_doctor(error):
	""" Accepts abnormal pulse and prints error message """

	if error != None:
		print("Pulse during hour {} was abnormal!!!".format(error))


 
def draw_bar(draw, height, color):
    """ draws each bar """

    draw.fillcolor(color)
    draw.begin_fill()             
    draw.left(90)
    draw.forward(height)
    draw.write(str(height))
    draw.right(90)
    draw.forward(20)
    draw.right(90)
    draw.forward(height)
    draw.left(90)
      
    draw.end_fill()                
 
def draw_chart(avg1, avg2, avg3, avg4):
	""" Accepts averages and draws a bar chart """

	value = [avg1,avg2,avg3,avg4]
	colour = ["purple", "cyan", "black", "orange"]
 
	maxheight = max(value)
	numbers = len(value)
	border = 5
	  
	bar = turtle.Screen()            
	bar.setworldcoordinates(0 - border, 0 - border,
	                       40 * numbers + border,
	                       maxheight + border)
	  
	
	brush = turtle.Turtle()          
	brush.pensize(1)
	  
	for i in range(len(value)):
	     
	    draw_bar (brush, value[i],
	             colour[i])
	 
	bar.exitonclick()

def main():

	(pulse1, pulse2, pulse3) = get_pulse()
	avg1 = average_pulse(pulse1, pulse2, pulse3)

	(pulse1, pulse2, pulse3) = get_pulse()
	avg2 = average_pulse(pulse1, pulse2, pulse3)

	(pulse1, pulse2, pulse3) = get_pulse()
	avg3 = average_pulse(pulse1, pulse2, pulse3)

	(pulse1, pulse2, pulse3) = get_pulse()
	avg4 = average_pulse(pulse1, pulse2, pulse3)

	erroneous = abnormal_pulse(avg1, avg2, avg3, avg4)	

	warning_doctor(erroneous)
	print(erroneous)

	value = [avg1, avg2, avg3, avg4]
	draw_chart(avg1, avg2, avg3, avg4)

if __name__ == "__main__":
	main()
