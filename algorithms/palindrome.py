def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    str_x = str(x)
    inv_str_x = str_x[::-1]
    return str_x == inv_str_x

if __name__ == "__main__":
    print(isPalindrome(123))