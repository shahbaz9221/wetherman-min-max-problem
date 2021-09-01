def string_to_integer(ch):
    temp = 0
    for i in range(len(ch)):
        temp = temp * 10 + (ord(ch[i]) - ord('0'))
    return temp


def check_null_value(temp):
    if temp is None:
        return -1
    return temp


MONTH_NAME = ['Jan', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']

EXTREME_WEATHER_REPORT_HELPER = ['Highest:', 'Lowest:', 'Humidity:']

MONTHLY_WEATHER_REPORT_HELPER = ['Max Temperature', 'Min Temperature', 'Mean Humidity']

UNIT_VALUES = ['C', 'C', '%']

