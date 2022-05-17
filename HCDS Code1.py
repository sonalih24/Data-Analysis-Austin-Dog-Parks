# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_graph():
    # Initialize the lists for X, Y1, and Y2
    data = pd.read_csv('C:\\Users\\sonal\\OneDrive\\Desktop\\Education\\06 Spring 2022\\Comp Sci\\Homework\\HCDS Data1.csv')
    df = pd.DataFrame(data)
    x = np.arange(7)
    y1 = list(df.iloc[:, 1])
    y2 = list(df.iloc[:, 2])
    width = 0.40
    # Plot data in grouped manner of bar type
    plt.ylim(ymin = 0, ymax = 100)
    plt.bar(x-0.2, y1, width, color='b')
    plt.bar(x+0.2, y2, width, color='r')
    plt.xticks(x,list(df.iloc[:, 0]))
    plt.title("Hancock vs Norwood Estate Dog Park: Amount of Dogs Who Shed & Other Attributes")
    plt.xlabel("\nDog and Owner Information")
    plt.ylabel("Amount of Dogs in Percent")
    plt.legend(["Hancock", "Norwood Estate"])
    # Show the plot
    plt.show()

create_graph()
     
