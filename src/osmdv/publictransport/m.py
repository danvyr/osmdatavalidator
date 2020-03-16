#from django.db import models
from django.contrib.gis.db import models


# https://developers.google.com/transit/gtfs/reference?hl=ru
# route trip stops

# https://wiki.openstreetmap.org/wiki/Public_transport


# когда несколько маршрутов.
# когда маршрут в какое-то время может изменится что бы заехать куда-то или ехать в депо
# замена типа транспорта на маршруте


# возможности
#



class Agency(models.Model):
    agency_id = models.CharField(max_length=30)
    agency_name = models.CharField(max_length=30)
    agency_lang = models.CharField(max_length=30)
    agency_phone = models.CharField(max_length=30)
    agency_timezone = models.CharField(max_length=30)

    agency_fare_url = models.CharField(max_length=30)
    agency_email = models.EmailField(max_length=30)
    agency_url = models.URLField(max_length=30)

class Network(models.Model):
    network_name = models.CharField(max_length=30)


# 
#
#
# master_route
# 
# route (    
# type: with_passanges, service, to_depo
#    
# )
#
#
#
#


class Stop(models.Model):
    # TODO LOCATION_TYPES
    LOCATION_TYPES = (('0', 'empty'),
                      ('1', 'place with few stops'),
                      ('2', ''),
                      ('3', 'common pathways'),
                      ('4', 'platform')
                      )

    stop_id = models.CharField(max_length=30)
    stop_code = models.CharField(max_length=30)
    stop_name = models.CharField(max_length=30)
    stop_desc = models.CharField(max_length=30)

    stop_lat = models.CharField(max_length=30)
    stop_lon = models.CharField(max_length=30)
    stop_point = models.PointField()

    zone_id = models.CharField(max_length=30)
    stop_url = models.CharField(max_length=30)
    location_type = models.CharField(max_length=1, choices=LOCATION_TYPES)
    parent_station = models.ForeignKey(Stop)
    stop_timezone = models.CharField(max_length=30)
    wheelchair_boarding = models.CharField(max_length=30)  # TODO
    level_id = models.CharField(max_length=30)
    platform_code = models.CharField(max_length=30)


class StopPosition(models.Model):
    stop_point = models.PointField()
    stop = models.ForeignKey(Stop)

    # TODO maybe move that to Stop
    bus = models.BooleanField()
    trolleybus = models.BooleanField()
    trum = models.BooleanField()
    train = models.BooleanField()
    # TODO: continue


class Route(models.Model):
    ROUTE_TYPES = (('0', 'tram'),
                   ('1', 'subway'),
                   ('2', 'rail'),
                   ('3', 'bus'),
                   ('4', 'ferry'),
                   ('5', 'cable_tram'),
                   ('6', 'Aerial lift'),
                   ('7', 'funicular'),
                   ('11', 'trolleybus'),
                   ('12', 'monorail'))

    from_stop = models.ForeignKey(Stop)
    to_stop = models.ForeignKey(Stop)
    # operator 
    #service tourism (trains for tourists, often historic vehicles),
    # night (night trains with sleeping cars),
    # car_shuttle (car shuttle trains through tunnels),
    # car (long distance trains with double-deck car carrier),
    # commuter (urban mass transit service, short headways; e.g., S-train),
    # regional (local train),
    # long_distance (long distance trains; e.g., InterCity, EuroCity, InterRegio)
    # high_speed (high speed trains; e.g., ICE, TGV)

    route_type = models.CharField(max_length=2, choices=ROUTE_TYPES)
    stop_id = models.CharField(max_length=30)
    agency_id = models.ForeignKey(Agency)
    route_short_name = models.CharField(max_length=30)
    route_long_name = models.CharField(max_length=30)
    route_desc = models.CharField(max_length=120)
    route_url = models.URLField(max_length=30)
    route_color = models.CharField(max_length=8)
    route_text_color = models.CharField(max_length=12)
    route_sort_order = models.CharField(max_length=30)


class Trip(models.Model):

    WHEELCHAIR_ACCESSIBLE_TYPES = (('0', 'no_info'),
                                   ('1', 'yes'),
                                   ('2', 'no'))
    BIKES_ALLOWED_TYPES = (('0', 'no_info'),
                           ('1', 'yes'),
                           ('2', 'no'))

    route_id = models.ForeignKey(Route)
    service_id = models.CharField(max_length=30)
    trip_id = models.ForeignKey(Trip)
    trip_headsign = models.CharField(max_length=30)
    trip_short_name = models.CharField(max_length=30)
    direction_id = models.CharField(max_length=30)
    block_id = models.CharField(max_length=30)
    shape_id = models.CharField(max_length=30)
    wheelchair_accessible = models.CharField(
        max_length=1, choices=WHEELCHAIR_ACCESSIBLE_TYPES)
    bikes_allowed = models.CharField(max_length=1, choices=BIKES_ALLOWED_TYPES)


class Stop_Time(models.Model):
    trip_id = models.ForeignKey(Trip)
    stop_id = models.ForeignKey(Stop)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    # the number of stop in a trip for ordering #Order of stops for a particular trip
    departure_time = models.TimeField(auto_now=False, auto_now_add=False)
    stop_sequence = models.PositiveSmallIntegerField()

    stop_headsign = models.CharField(max_length=30)
    pickup_type = models.CharField(max_length=30)
    drop_off_type = models.CharField(max_length=30)
    shape_dist_traveled = models.CharField(max_length=30)
    timepoint = models.CharField(max_length=30)


class calendar(models.Model):
    AVAILABLE_TYPE = (('0', 'no'),
                      ('1', 'yes'))

    service_id = models.CharField(max_length=30)
    monday = models.CharField(max_length=1, choices=AVAILABLE_TYPE)
    tuesday = models.CharField(max_length=1, choices=AVAILABLE_TYPE)
    wednesday = models.CharField(max_length=1, choices=AVAILABLE_TYPE)
    thursday = models.CharField(max_length=1, choices=AVAILABLE_TYPE)
    friday = models.CharField(max_length=1, choices=AVAILABLE_TYPE)
    saturday = models.CharField(max_length=1, choices=AVAILABLE_TYPE)
    sunday = models.CharField(max_length=1, choices=AVAILABLE_TYPE)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)


class CalendarDate(models.Model):
    EXCEPTION_TYPES = (('1', 'added'),
                       ('2', 'removed'))

    service_id = models.ForeignKey(calendar.service_id)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    exception_type = models.CharField(max_length=1, choices=EXCEPTION_TYPES)


class Shape(models.Model):
    line = models.LineString()
    # shape_pt_lat
    # shape_pt_lon
    # shape_pt_sequence
    # shape_dist_traveled


class FareAttributes(models.Model):
    fare_id = models.CharField(max_length=30)
