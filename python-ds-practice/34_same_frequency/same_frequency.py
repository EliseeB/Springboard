def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    freq1 = {}
    freq2 = {}

    for x in str(num1):
        freq1[x] = freq1.get(x, 0) + 1

    for x in str(num2):
        freq2[x] = freq2.get(x, 0) + 1

    return freq1 == freq2
