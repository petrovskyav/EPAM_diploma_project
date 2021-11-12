import datetime
import requests
from django.db.models import Avg
from weather_comparator.models import Weather_history

requests.packages.urllib3.disable_warnings()


class Metaweather():
    def __init__(self):
        self.base_url = 'https://www.metaweather.com/api/'

    def api_query(self, sub_url):
        url = self.base_url + sub_url
        r = requests.get(url, verify=False)
        if r.status_code == 200:
            if len(r.json()) > 0:
                return (r.json())
            else:
                raise Exception('NoDataReceived')
        else:
            raise Exception(f'HttpCode_{r.status_code}')

    def get_city_info(self, location):
        sub_url = f'location/search/?query={location}'
        result = self.api_query(sub_url)
        return (result)

    def put_data_to_db(self, data):
        for item in data:
            obj, created = Weather_history.objects.get_or_create(measure_id=item['id'],
                                                                 defaults={'datetime': item['created'],
                                                                           'min_temp': item['min_temp'],
                                                                           'max_temp': item['max_temp'],
                                                                           'the_temp': item['the_temp'],
                                                                           'humidity': item['humidity']})

    def get_data_from_db(self, date):
        result = Weather_history.objects.filter(datetime__year=date.year,
                                                datetime__month=date.month,
                                                datetime__day=date.day)
        if len (result) > 0:
            avg_data = result.aggregate(Avg('min_temp'), Avg('max_temp'), Avg('the_temp'), Avg('humidity'))
            avg_min_temp = round(avg_data['min_temp__avg'], 3)
            avg_max_temp = round(avg_data['max_temp__avg'], 3)
            avg_the_temp = round(avg_data['the_temp__avg'], 3)
            avg_humidity = round(avg_data['humidity__avg'], 3)

            res = {'data': result,
                   'avg_data': {'min_temp': avg_min_temp, 'max_temp': avg_max_temp, 'the_temp': avg_the_temp,
                                'humidity': avg_humidity}}
        else:
            res = {'data': result,
                   'avg_data': {}}
        return (res)


    def get_weather_history(self, location, date):
        data_from_db = self.get_data_from_db(date)
        if len(data_from_db['data']) > 0:
            return (data_from_db)
        else:
            cityid = self.get_city_info(location)[0]['woeid']
            sub_url = f'location/{cityid}/{date.year}/{date.month}/{date.day}/'
            result = self.api_query(sub_url)
            res = []
            for item in result:
                if date.date() == datetime.datetime.strptime(item['created'], "%Y-%m-%dT%H:%M:%S.%fZ").date():
                    res.append(item)
            self.put_data_to_db(res)
            data_from_db = self.get_data_from_db(date)
            return (data_from_db)

    def get_distinct_days(self):
        result = Weather_history.objects.dates('datetime', 'day', order='DESC')
        return (result)

    def erase_db(self):
        Weather_history.objects.all().delete()
        return

    def delete_data(self, date):
        Weather_history.objects.filter(datetime__year=date.year,
                                                datetime__month=date.month,
                                                datetime__day=date.day).delete()
        return

