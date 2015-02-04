from math import sqrt

def mean(data):
# average
    length = len(data)
    try:
        return sum(data)/length
    except ZeroDivisionError:
        print "The data is empty!"
        return

def std(data, sample=True):
# standard variation
    average = mean(data)
    try:
        return sqrt(sum((x-average)**2 for x in data)/((len(data)) - 1))
    except ZeroDivisionError:
        print "The data is empty!"
        return
