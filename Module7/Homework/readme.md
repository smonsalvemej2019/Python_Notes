# Documentation
### Introduction to Python Programming
### Assignment A4: Fuel Consumption
### Florida Atlantic University, Summer 2021

This program will take data from the given CSV files and display it in a variety of ways.

When launched you will have two options:

- To filter the data within a given range
- To plot the data on a plane using pylab

When plotting the data, you will have the options to either save the chart as a png file or to display it on the screen. The name of the save file will be 

    mpg_plotchart.png

***ATTENTION:*** The options use to different CSV files. The data used by the plot option is generalized and it is better suited for the plot plane.

### Design Decisions
There is some details about the program that need to be clarified.

1. The program uses the same types of menus as my other assignments; A main while loop and the menus themselves being handled by the functions

2. The program has two main functions: A display data function and a plot data function. Each function checks for input and handles its own errors. I believe this is the best approach to input validation.


