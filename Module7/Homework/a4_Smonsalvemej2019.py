import pylab as plt
import csv

def get_car():#function to get the car by range
    try:
        #getting the input from the user
        print("\nPlease Input the fuel efficiency range (Miles Per Gallon)")
        lower_val = int(input("\nfrom: "))
        higher_val = int(input("\nto: "))

        #reading external csv file
        file = open("epadata2015.csv")
        reader = csv.reader(file)

        #variable initiation
        car_list = list()
        line = 0

        #loop checks trough each row of the file and extracts
        #information within the given range 
        for row in reader:
            if line == 0:
                car_list.append("Fuel Efficiency by car withing the given range: ")
                line += 1
                continue
            if (
                (lower_val <= int(row[10]) and 
                int(row[10]) <= higher_val) 
                and (row[2] + " " + row[3]) not in car_list
                ):
                car_list.append(row[2] + " " + row[3])

        #gives a warning if car was not found within the given range
        if len(car_list) == 1:
            print("\n\x1b[0;30;42m" + " NO CARS FOUND WITHIN GIVEN RANGE " + "\x1b[0m\n")
            return
        #display data with different colors so it is easier to read
        line = 0
        print("\n")
        for cars in car_list:
            if line % 2:
                print("\x1b[0;37;40m" + cars + "\x1b[0m")
                line += 1
            else:
                print("\x1b[0;30;47m" + cars + "\x1b[0m")
                line += 1

        #closing the file
        file.close()

    #handle input errors
    except ValueError:
        print("\n\x1b[0;30;41m" + " ERROR: INPUT FOR MILES PER GALLON SHOULD BE AN INTEGER" + "\x1b[0m\n")





def get_chart():#function to extract information and plot it on the coordinate plane
    try:
        #get input from users
        print("\nwhat kind of data would you like to be display?")
        data_option = input("\nFuel efficiency in the highway(H)\nFuel efficiency in the city(C)\nOverall fuel efficiency(O)\n")
        data_option = data_option.lower()
        print("\nWould you like to:")
        display_option = input("\nSave the plot chart (S)\nDisplay the plotchart on the screen (D)\n")
        display_option = display_option.lower()

        #validate the inputs
        if data_option == 'h':
            column = 6
        elif data_option == 'c':
            column = 5
        elif data_option == 'o':
            column = 4
        else:
            raise ValueError

        if display_option == 's':
            _save = 1
        elif display_option == 'd':
            _save = 0
        else:
            raise ValueError

        #open and read the file
        file = open("epadata2020.csv")
        reader = csv.reader(file)

        #variable initialization
        x = list()
        y = list()
        line = 0;

        #transfer the require data into the necessary lists
        for row in reader:
            if line == 0:
                line += 1
                continue
            x.append(int(row[0].lstrip('Prelim. ')))
            y.append(float(row[column]))
        
        #close the file
        file.close()

        #UNCOMMENT TO CHECK DATA
        # for i in y:
        #     print(i)

        #table variables and methods
        fig, ax = plt.subplots(1, figsize=(11,7))
        ax.set_axisbelow(True)
        #grid
        ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
        ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
        #plots the data
        plt.plot(x,y,'r.-')
        #labels
        plt.xlabel('year')
        plt.ylabel('MPG')
        #ticker display
        plt.xticks(plt.arange(min(x), max(x), 2))
        plt.yticks(plt.arange(min(y),max(y), 0.5))
        plt.xticks(rotation=45)
        #user option of saving or displaying
        if _save == 1:
            plt.savefig('mpg_plotchart.png')
        else:
            plt.show()



    except ValueError:
        print("\n\x1b[0;30;41m" + " ATTENTION: INVALID MENU OPTIONS " + "\x1b[0m\n")


print("""\nThis program will display data taken from csv files on the 
command line interface  or plot data on a coordinate plane using pylab\n""")

while(1):
    print("What would you like to do?")
    try:
        option = int(input("\nGet car model from fuel efficiency interval(1) \
            \nGet plot chart of fuel efficiency over the years(2) \nExit Program(0)\n"))

        if(option == 1):
            get_car()
        elif(option == 2):
            get_chart()
        elif(option == 0):
            break
        else:
            raise ValueError
    except ValueError:
        print("\n\x1b[0;30;41m" + " ATTENTION: INVALID MENU OPTION " + "\x1b[0m\n")