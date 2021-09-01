import os
import csv
import constant
import utils
from record import Records


class FileParser:
    """
    This class is used to parse file into annual data and monthly data
    """

    def __init__(self, filepath) -> None:
        """
        It contructs the files directory
        :param filepath:
        stores the files path
        """
        self.file_path = filepath

    def read_yearly_data(self, year) -> [Records]:
        """
        This function generates the file names from directories
        which needs to be open and read and use the function
        read_months_data_from_file
        :param year:
        This parameter helps you to open only specific year of files
        that needs to be open
        :return:
        list of Record class with months data
        """
        files_name = []
        for file in os.listdir(self.file_path):
            date = file.split("_")
            if file.endswith(".txt") and date[constant.YEAR_CHECK] == year:
                files_name.append(os.path.join(self.file_path, file))

        yearly_record_list = FileParser.reading_months_data_from_file(files_name)

        return yearly_record_list

    def read_month_data(self, year, month) -> [Records]:
        """
        This function generates file directory and its name by
        using the function read_months_data_from_file
        :param year:
        This parameter helps to open specific year of file
        :param month:
        This parameter helps to open specific month of file
        :return:
        list of record with monthly data in it
        """
        files_name = []
        for file in os.listdir(self.file_path):
            date = file.split("_")
            months = date[constant.MONTH_CHECK]
            if file.endswith(".txt") and date[constant.YEAR_CHECK] == year and \
                    months[:constant.MONTHS_LENGTH] == utils.MONTH_NAME[utils.string_to_integer(month)]:
                files_name.append(os.path.join(self.file_path, file))

        monthly_record_list = FileParser.reading_months_data_from_file(files_name)
        return monthly_record_list

    @staticmethod
    def reading_months_data_from_file(files_name) -> [Records]:
        """
        This static method is used to read data from file in weather
        Record
        :param files_name:
        This parameter contains the file path and file name
        :return:
        List of Record class object with all the data that read
        from the file
        """
        weather_record_list = []
        for iterator in range(len(files_name)):
            with open(files_name[iterator], 'r') as csv_file:
                read_from_file = csv.reader(csv_file)
                next(read_from_file)
                for reader in read_from_file:
                    weather_record = Records(utils.check_null_value(reader[constant.PKT]),
                                             utils.check_null_value(reader[constant.MAX_TEMPERATURE_C]),
                                             utils.check_null_value(reader[constant.MEAN_TEMPERATURE_C]),
                                             utils.check_null_value(reader[constant.MIN_TEMPERATURE_C]),
                                             utils.check_null_value(reader[constant.MAX_DEW_POINT_C]),
                                             utils.check_null_value(reader[constant.MEAN_DEW_POINT_C]),
                                             utils.check_null_value(reader[constant.MIN_DEW_POINT_C]),
                                             utils.check_null_value(reader[constant.MAX_HUMIDITY]),
                                             utils.check_null_value(reader[constant.MEAN_HUMIDITY]),
                                             utils.check_null_value(reader[constant.MIN_HUMIDITY]),
                                             utils.check_null_value(reader[constant.MAX_SEA_LEVEL_PRESSURE_PA]),
                                             utils.check_null_value(reader[constant.MEAN_SEA_LEVEL_PRESSURE_PA]),
                                             utils.check_null_value(reader[constant.MIN_SEA_LEVEL_PRESSURE_PA]),
                                             utils.check_null_value(reader[constant.MAX_VISIBILITY_KM]),
                                             utils.check_null_value(reader[constant.MEAN_VISIBILITY_KM]),
                                             utils.check_null_value(reader[constant.MIN_VISIBILITY_KM]),
                                             utils.check_null_value(reader[constant.MAX_WIND_SPEED]),
                                             utils.check_null_value(reader[constant.MEAN_WIND_SPEED]),
                                             utils.check_null_value(reader[constant.MAX_GUST_SPEED]),
                                             utils.check_null_value(reader[constant.PRECIPITATION_MM]),
                                             utils.check_null_value(reader[constant.CLOUD_COVER]),
                                             utils.check_null_value(reader[constant.EVENTS]),
                                             utils.check_null_value(reader[constant.WIND_DIR_DEGREES]))
                    weather_record_list.append(weather_record)
        return weather_record_list
