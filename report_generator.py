import utils
import graph_color_printing


class ReportsGenerator:
    """
    This class is used to display the extreme values of weather,
    average values of temperature and  draw two horizontal bar
    graph.This class only has static methods to display these results.
    """

    @staticmethod
    def yearly_extreme_weather_report(result) -> None:
        """
        This method is used to display the extreme values of weather
        which are maximum of max_temperature, minimum of Min temperature
        and maximum of max humidity
        :param result:
        This parameter has the computational data that is return from the
        from the computation file and has the extreme values of weather
        :return:
        None
        """
        for val in range(len(result)):
            print("{extreme_values}".format(extreme_values=utils.EXTREME_WEATHER_REPORT_HELPER[val]),
                  result[val].extreme_value, "{unit_values}".format(unit_values=utils.UNIT_VALUES[val]),
                  "on", result[val].date, result[val].month)

    @staticmethod
    def monthly_weather_report(result) -> None:
        """
        This method is used to display the monthly weather report in which
        It shows the average value of max temperature, lowest temperature
        and mean humidity.
        :param result:
        This parameter has the computational data that is return from the
        from the computation file and has the average values of data
        :return:
        None
        """
        for val in range(len(result)):
            print("{extreme_values} Average: ".format(extreme_values=utils.MONTHLY_WEATHER_REPORT_HELPER[val]),
                  result[val], "{unit_values}".format(unit_values=utils.UNIT_VALUES[val]))

    @staticmethod
    def horizontal_graph_between_highest_lowest_temperature(result) -> None:
        """
        This method is used to display horizontal bar graph day to day from
        highest temperature to lowest temperature to each day using the the
        file graph_color_printing. It displays the graph from highest temperature
        and then lowest temperature
        :param result:
        This parameter has the computational data that is return from the
        from the computation file
        :return:
        None
        """
        for iterator in range(len(result)):
            print(iterator, " ", end="")
            for val in range(utils.string_to_integer(result[iterator].highest_temperature)):
                print(graph_color_printing.text_color("[[reset]]+"), end="")
            print(graph_color_printing.text_color(" {temperature}C"
                                                  .format(temperature=utils.string_to_integer(result[iterator].
                                                                                              highest_temperature))))
            print(iterator, " ", end="")
            for val in range(utils.string_to_integer(result[iterator].lowest_temperature)):
                print(graph_color_printing.text_color("[[reset]]+"), end="")
            print(graph_color_printing.text_color(" {temperature}C"
                                                  .format(temperature=utils.string_to_integer(result[iterator].
                                                                                              lowest_temperature))))

    @staticmethod
    def horizontal_graph_between_highest_lowest_temperature_extended(result) -> None:
        """
        This method is extended form of horizontal_graph_between_highest_to_lowest_temperature
        which also displays the horizontal bar graph in different manner. It displays the graph
        first lowest temperature and then highest temperature on the same line
        :param result:
        This parameter has the computational data that is return from the
        from the computation file
        :return:
        None
        """
        for iterator in range(len(result)):
            print(graph_color_printing.text_color("[[Blue]]{iter}".format(iter=iterator)), " ", end="")
            print(graph_color_printing.text_color
                  ("{temperature}C ".format(temperature=utils.string_to_integer(result[iterator].lowest_temperature))),
                  end="")
            for val in range(utils.string_to_integer(result[iterator].lowest_temperature)):
                print(graph_color_printing.text_color("+"), end="")

            for val in range(utils.string_to_integer(result[iterator].highest_temperature)):
                print(graph_color_printing.text_color("[[Red]]+"), end="")
            print(graph_color_printing.text_color
                  (" {temperature}C".format(temperature=utils.string_to_integer(result[iterator].highest_temperature))))
