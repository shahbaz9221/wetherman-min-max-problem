import os
import argparse
import constant
from report_generator import ReportsGenerator
from fileparser import FileParser
from computation import WeatherProcessor


def main():
    """
    This function separates the different task according to their flag value

    This flag e makes the list of result class  and append data after read the
    yearly data from file and pass that data to the computation class and that
    class return the highest temperature, lowest temperature and max humidity
    and Display that list.

    The flag a make another list of result class and append data after reading
    only month's data and pass that data to computation class that returns the
    average of max temperature,min temperature and mean humidity and display
    that average through result list

    The flag c only read the monthly data and display two horizontal bar graphs.
    one graph displays highest temperature on one day in one line and another line displays
    min temperature. Second shows the minimum temperature graph and and highest temperature
    on each day on the same line.
    :return:
    None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Directory')
    parser.add_argument('flag', help='Task_division')
    parser.add_argument('date', help='Date')
    args = parser.parse_args()
    os.chdir(args.directory)

    if args.flag == 'e':
        extreme_weather_result_list = []
        file_path = FileParser(args.directory)

        yearly_computational_data = WeatherProcessor(file_path.read_yearly_data(args.date))
        get_highest_temperature = yearly_computational_data.get_highest_temperature()

        extreme_weather_result_list.append(get_highest_temperature)
        get_lowest_temperature = yearly_computational_data.get_lowest_temperature()

        extreme_weather_result_list.append(get_lowest_temperature)
        get_highest_humidity = yearly_computational_data.get_highest_humidity()

        extreme_weather_result_list.append(get_highest_humidity)
        ReportsGenerator.yearly_extreme_weather_report(extreme_weather_result_list)

    elif args.flag == 'a':
        monthly_average_list = []
        file_path = FileParser(args.directory)

        month_and_day_list = args.date.split("/")
        monthly_computational_data = WeatherProcessor(
            file_path.read_month_data(month_and_day_list[constant.YEAR_PARSER],
                                      month_and_day_list[constant.MONTH_PARSER]))

        get_max_temperature_average = monthly_computational_data.get_highest_average_temperature()
        monthly_average_list.append(get_max_temperature_average)

        get_lowest_temperature_average = monthly_computational_data.get_lowest_average_temperature()
        monthly_average_list.append(get_lowest_temperature_average)

        get_mean_humidity_average = monthly_computational_data.get_mean_average_humidity()
        monthly_average_list.append(get_mean_humidity_average)
        ReportsGenerator.monthly_weather_report(monthly_average_list)

    elif args.flag == 'c':
        file_path = FileParser(args.directory)
        month_and_day_list = args.date.split("/")

        monthly_computational_data = WeatherProcessor(
            file_path.read_month_data(month_and_day_list[constant.YEAR_PARSER],
                                      month_and_day_list[constant.MONTH_PARSER]))

        highest_lowest_temperature_data_list = monthly_computational_data.get_highest_lowest_temperature_list()
        ReportsGenerator.horizontal_graph_between_highest_lowest_temperature(highest_lowest_temperature_data_list)
        # ReportsGenerator.\
        #     horizontal_graph_between_highest_lowest_temperature_extended(highest_lowest_temperature_data_list)


if __name__ == "__main__":
    main()
