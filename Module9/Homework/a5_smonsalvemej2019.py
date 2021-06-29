import csv

def file_reader(reader):
    iris = {}
    for row in reader:
        if row["species"] not in iris:
            iris[row["species"]] = {"sepal_length": float(row["sepal_length"]), "sepal_width": float(row["sepal_width"]), 
                                    "petal_length":float(row["petal_length"]), "petal_width":float(row["petal_width"]), "row_count": 1}
            continue
        else:
            iris[row["species"]]["sepal_length"] += float(row["sepal_length"])
            iris[row["species"]]["sepal_width"] += float(row["sepal_width"])
            iris[row["species"]]["petal_length"] += float(row["petal_length"])
            iris[row["species"]]["petal_width"] += float(row["petal_width"])
            iris[row["species"]]["row_count"] += 1
        
    for val in iris.values():
        val["sepal_length"] /= val["row_count"] 
        val["sepal_width"]  /= val["row_count"]
        val["petal_length"]  /= val["row_count"]
        val["petal_width"] /= val["row_count"]
        del val["row_count"]

    return iris 

def display_data(data):
    pass


try:
    file = open("iris.csv")
    reader = csv.DictReader(file)
    file_reader(reader)



except FileNotFoundError:
    print("\n\x1b[0;30;41m" + " ERROR: FILE NOT FOUND IN DIRECTORY" + "\x1b[0m\n")