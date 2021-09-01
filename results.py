class Results:
    """
    This class store the extreme values of weather
    e.g. max temperature, min temperature, max humidity
    and display that values
    """

    def __init__(self, extreme_value, month, date) -> None:
        """
        This is default constructor of Result class that constructs
        the extreme values, month and date
        :param extreme_value:
        It store the max temperature, min temperature and max humidity
        :param month:
        It store the month of that temperature
        :param date:
        It store the day of that temperature
        """
        self.extreme_value = extreme_value
        self.month = month
        self.date = date
    
    def __init__(self, highest_temperature, lowest_temperature) -> None:
        self.highest_temperature = highest_temperature
        self.lowest_temperature = lowest_temperature
