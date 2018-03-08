def increase_by_1_loop(dummy_list):
    """
    Increase the value by 1 by looping through each value in the list

    Return
    ------
    A new list containing the new values

    Parameters
    ----------
    dummy_list: A list containing integers
    """
    secondlist=[]
    for i in range(0,len(dummy_list)):
        secondlist.append(dummy_list[i]+1)

    return secondlist

def increase_by_1_list_comp(dummy_list):
    """
    Increase the value by 1 using list comprehension

    Return
    ------
    A new list containing the new values

    Parameters
    ----------
    dummy_list: A list containing integers
    """
    return [x+1 for x in dummy_list]