#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error_list = []
    for index in range (0,len(predictions)):
        error_list.append( (( (net_worths[index] - predictions[index]) * ( net_worths[index] - predictions[index])) , index ) )

    error_list.sort(key=lambda x: x[0])

    print error_list

    error_list = error_list[:81]

    for x,y in error_list:
        cleaned_data.append( (ages[y], net_worths[y], x))

    print 'The length of cleaned data', len(cleaned_data)

    return cleaned_data

