from math import sqrt

def mean(data):
# average
    length = len(data)
    try:
        return sum(data)/length
    except ZeroDivisionError:
        print "The data is empty!"
        return

def var(data, sample=True):
# standard deviation
    average = mean(data)
    ss = sum((x-average)**2 for x in data)
    try:
        if sample:
        # sample deviation
            return ss/(len(data) - 1)
        else:
        # population deviation
            return ss/len(data)

    except ZeroDivisionError:
        print "The data is empty!"
        return

def std(data, sample=True):
    return sqrt(var(data, sample))
