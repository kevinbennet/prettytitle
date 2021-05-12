import math
import argparse

def title_maker(title,length=119,caps=False):

    '''

    This program prettifies commented titles for copying into python scripts.

    Parameters
    ----------
    title : string, required
            title name to prettify
    length : int, optional
             set length of title box (default: 119)
    caps : bool, optional
            capitalize title (default: False)

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

    if caps:
        title = title.upper()
    placement = (len(title)+2)/2
    title_line = "#"*(math.floor(length/2)) + " {} " + "#"*(math.ceil(length/2))
    start_point = math.floor(placement)
    end_point = -math.ceil(placement)

    if type(length)!=int:
        print("length argument needs to be int type!")
    else:
        print("\nCopy the below code into your script:\n")
        print("#"*length)
        print(title_line.format(title)[start_point:end_point])
        print("#"*length+"\n")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('title', type=str, help="title name to prettify")
    parser.add_argument('-l', '--length', type=int, dest='length', help="set length of title box (default: 119)")
    parser.add_argument('-c', '--caps', action='store_true', help="capitalize title")
    args = parser.parse_args()

    if args.caps:
        args.title = args.title.upper()

    if args.length:
        title_maker(title=args.title,length=args.length)
    else:
        title_maker(title=args.title)
