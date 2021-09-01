import constant
import utils
from results import Results


class WeatherProcessor:
    """
    This class calculates the highest temperature, lowest temperature
    max humidity through annual data. This also computes the average
    of max temperature, min temperature and mean humidity and returns
    computational values to main function in weatherman files

    """
    def __init__(self, weather_data) -> None:
        """
        This is default constructor of Weatherprocessor class
        :param weather_data:
        stores the annual weather data and monthly weather data one by one
        """
        self.weather_detail = weather_data

    def get_highest_temperature(self) -> Results:
        """
        This function returns after the calculation of the highest
        temperature from max temperature
        :return:
        object of Result class with highest extreme value max temperature
        """
        day = constant.DAY
        highest_temperature = utils.string_to_integer(self.weather_detail[constant.INDEX_HANDLER].max_temperature)

        for val in range(len(self.weather_detail)):
            if highest_temperature < utils.string_to_integer(self.weather_detail[val].max_temperature):
                highest_temperature = utils.string_to_integer(self.weather_detail[val].max_temperature)
                day = self.weather_detail[val].pkt

        month = day.split("-")
        return Results(highest_temperature, utils.MONTH_NAME[utils.string_to_integer(month[constant.INDEX_HANDLER])],
                       month[constant.INDEX_HANDLER + 1])

    def get_lowest_temperature(self) -> Results:
        """
        This function returns after the calculation of the lowest
        temperature from lowest temperature
        :return:
        object of Result class with extreme lowest value of temperature
        """
        day = constant.DAY
        lowest_temperature = utils.string_to_integer(self.weather_detail[constant.INDEX_HANDLER].min_temperature)

        for val in range(len(self.weather_detail)):
            if lowest_temperature > utils.string_to_integer(self.weather_detail[val].min_temperature):
                lowest_temperature = utils.string_to_integer(self.weather_detail[val].min_temperature)
                day = self.weather_detail[val].pkt

        month = day.split("-")
        return Results(lowest_temperature, utils.MONTH_NAME[utils.string_to_integer(month[constant.INDEX_HANDLER])],
                       month[constant.INDEX_HANDLER + 1])

    def get_highest_humidity(self) -> Results:
        """
        This function returns after the calculation of the max
        humidity from humidity

        :return:
        object of Result class and the values of extreme humidity
        """
        day = constant.DAY
        highest_humidity = utils.string_to_integer(self.weather_detail[constant.INDEX_HANDLER].max_humidity)
        for val in range(len(self.weather_detail)):
            if highest_humidity < utils.string_to_integer(self.weather_detail[val].max_humidity):
                highest_humidity = utils.string_to_integer(self.weather_detail[val].max_humidity)
                day = self.weather_detail[val].pkt
        month = day.split("-")
        return Results(highest_humidity, utils.MONTH_NAME[utils.string_to_integer(month[constant.INDEX_HANDLER])],
                       month[constant.INDEX_HANDLER + 1])

    def get_highest_average_temperature(self) -> int:
        """
        This function calculates the months highest
        average temperature from max temperature

        :return:
        average of max temperature
        """
        add = constant.COUNTER_STARTER
        count = constant.COUNTER_STARTER
        for val in range(len(self.weather_detail)):
            add = add + utils.string_to_integer(self.weather_detail[val].max_temperature)
            count = count + 1
        return int(add / count)

    def get_lowest_average_temperature(self) -> int:
        """
        This function calculates the months highest
        average temperature from max temperature

        :return:
        average from min temperature
        """
        add = constant.COUNTER_STARTER
        count = constant.COUNTER_STARTER
        for val in range(len(self.weather_detail)):
            add = add + utils.string_to_integer(self.weather_detail[val].min_temperature)
            count = count + 1
        return int(add / count)

    def get_mean_average_humidity(self) -> int:
        """
        This function calculates the months highest
        average temperature from max temperature

        :return:
        average from mean humidity
        """
        add = constant.COUNTER_STARTER
        count = constant.COUNTER_STARTER
        for val in range(len(self.weather_detail)):
            add = add + utils.string_to_integer(self.weather_detail[val].mean_humidity)
            count = count + 1
        return int(add / count)

    def get_highest_lowest_temperature_list(self) -> [Results]:
        highest_lowest_temperature_result_list = []

        for val in range(len(self.weather_detail)):
            highest_lowest_temperature_result_list.append(Results(self.weather_detail[val].max_temperature,
                                                                  self.weather_detail[val].min_temperature))

        return highest_lowest_temperature_result_list

