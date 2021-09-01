class Records:
    """
    This class stores the record of all the data read from a file
    """

    def __init__(self) -> None:
        """
        This is the default constructor of record class
        """
        self.pkt = None
        self.max_temperature = None
        self.mean_temperature = None
        self.min_temperature = None
        self.max_dew_point_C = None
        self.mean_dew_point_c = None
        self.min_dew_point_c = None
        self.max_humidity = None
        self.mean_humidity = None
        self.min_humidity = None
        self.max_sea_level_pressure_pa = None
        self.mean_sea_level_pressure_pa = None
        self.min_sea_level_pressure_pa = None
        self.max_visibility_km = None
        self.mean_visibility_km = None
        self.min_visibility_km = None
        self.max_wind_speed = None
        self.mean_wind_speed = None
        self.max_gust_speed = None
        self.precipitation_nm = None
        self.cloud_cover = None
        self.event = None
        self.win_dir_degree = None

    def __init__(self, pkt, max_temperature, mean_temperature, min_temperature, max_dew_point_c, mean_dew_point_c,
                 min_dew_point_c, max_humidity, mean_humidity, min_humidity, max_sea_level_pressure_pa,
                 mean_sea_level_pressure_pa, min_sea_level_pressure_pa, max_visibility_km, mean_visibility_km,
                 min_visibility_km, max_wind_speed, mean_wind_speed, max_gust_speed, precipitation_nm,
                 cloud_cover, event, win_dir_degree) -> None:
        """
        This is the parameterised constructor of record class and following are the parameters
        :param pkt:
        :param max_temperature:
        :param mean_temperature:
        :param min_temperature:
        :param max_dew_point_c:
        :param mean_dew_point_c:
        :param min_dew_point_c:
        :param max_humidity:
        :param mean_humidity:
        :param min_humidity:
        :param max_sea_level_pressure_pa:
        :param mean_sea_level_pressure_pa:
        :param min_sea_level_pressure_pa:
        :param max_visibility_km:
        :param mean_visibility_km:
        :param min_visibility_km:
        :param max_wind_speed:
        :param mean_wind_speed:
        :param max_gust_speed:
        :param precipitation_nm:
        :param cloud_cover:
        :param event:
        :param win_dir_degree:
        """
        self.pkt = pkt
        self.max_temperature = max_temperature
        self.mean_temperature = mean_temperature
        self.min_temperature = min_temperature
        self.max_dew_point_C = max_dew_point_c
        self.mean_dew_point_c = mean_dew_point_c
        self.min_dew_point_c = min_dew_point_c
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.min_humidity = min_humidity
        self.max_sea_level_pressure_pa = max_sea_level_pressure_pa
        self.mean_sea_level_pressure_pa = mean_sea_level_pressure_pa
        self.min_sea_level_pressure_pa = min_sea_level_pressure_pa
        self.max_visibility_km = max_visibility_km
        self.mean_visibility_km = mean_visibility_km
        self.min_visibility_km = min_visibility_km
        self.max_wind_speed = max_wind_speed
        self.mean_wind_speed = mean_wind_speed
        self.max_gust_speed = max_gust_speed
        self.precipitation_nm = precipitation_nm
        self.cloud_cover = cloud_cover
        self.event = event
        self.win_dir_degree = win_dir_degree


