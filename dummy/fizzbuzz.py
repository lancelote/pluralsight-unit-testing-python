def fizzbuzz(n, additional_rules=None):
    """Fizzbuzz simple implementation

    Args:
        n (int): Number to check
        additional_rules (dict): {int: 'to be returned', ...}

    Returns:
        str

    Examples:
        >>> fizzbuzz(2)
        '2'
        >>> fizzbuzz(3)
        'Fizz'
        >>> fizzbuzz(15)
        'FizzBuzz'
        >>> fizzbuzz(35, {7: 'Whizz'})
        'BuzzWhizz'
    """
    answer = ''
    rules = {3: 'Fizz', 5: 'Buzz'}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer = str(n)
    return answer
