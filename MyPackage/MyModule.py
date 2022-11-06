def top_n (items, n):
        """Return the top N items in an array, in desc order.

        Args:
            Items (): lost of array-like object
            n (int): num of items to return

        Return:
            array: top n items, in desc order

        Egs:
            >>> top_n([8,3,2,7,4], 3)
            [8,7,3]
        """
    for i in range(n):      # keep sortin until we have the top b items
        for j in range (len(items)-1-i):
            if items[j] > items[j+1]:   # if this item is bigger than the next item...
                items[j], items[j+1] = items[j+1], itmes[j]     # swap the two
    
    # get last two items
    top_n = items[-n:]

    # retunr in descending order
    return top_n[::-1]