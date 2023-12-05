def time_description(hours, minutes):
    if hours < 0 or hours > 12 or minutes < 0 or minutes > 59:
        return 'Incorrect input data!'
    nums_to_words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
                        4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                        8: 'eight', 9: 'nine', 10: 'ten'}
    if minutes == 0:
        return f'{nums_to_words[hours]} o\'clock'
    elif minutes == 15:
        return f'quarter past {nums_to_words[hours]}'
    elif minutes == 30:
        return f'half past {nums_to_words[hours]}'
    elif minutes <= 30:
        pass
