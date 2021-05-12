import math

def title_maker(title,length=119):

    '''

    This program prettifies commented titles for copying into python scripts.

    Parameters
    ----------
    title : string, required
            title name to prettify
    length : int, optional
             set length of title box (pre-defined is 119)

    Returns
    -------
    Returns title box ready for copying into script.

    Examples
    --------
    >>> import prettytitle as pt
    >>> pt.title_maker(title="imports", length=44)
    >>> ############################################
        ################## IMPORTS #################
        ############################################

    '''

    placement = (len(title)+2)/2
    title_line = "#"*(math.floor(length/2)) + " {} " + "#"*(math.ceil(length/2))
    start_point = math.floor(placement)
    end_point = -math.ceil(placement)

    print("Copy the below code into your script:\n")
    print("#"*length)
    print(title_line.format(title.upper())[start_point:end_point])
    print("#"*length)
