from operations import *

def normalize(vector, method="linear"):
    if method == "linear":
        minVal = float(min(vector))
        scale = - minVal + max(vector)
        try:
            return [(xi - minVal)/scale for xi in vector]
        except ZeroDivisionError:
            print "Maximum and minimun are the same value!"
            return

    elif method.lower() =="z" or method.lower() == "z-transform":
        meanVal = mean(vector)
        stdVal = std(vector)
        try:
            return [(xi - meanVal)/stdVal for xi in vector]
        except ZeroDivisionError:
            print "All points are of the same value!"
            return


