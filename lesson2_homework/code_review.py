from __future__ import unicode_literals
import json
from pprint import pprint
from lxml import etree
import requests
base_url = 'http://bj.bendibao.com/ditie/linemap.shtml'

response = requests.get(base_url)
html_tree = etree.HTML(response.text)
subway_objs = html_tree.xpath('//div[@class="line-list"]')
subway_items={}
station_dict = {}
for subway_obj in subway_objs:
    # 地铁线路
    subway_line = subway_obj.xpath('.//strong/a')[0].text
    subway_stations = subway_obj.xpath('.//div[@class="station"]/a/text()')
    subway_items.update({subway_line:subway_stations})
print(subway_items)

for subway_line,subway_stations in subway_items.items():
    last_station = None
    for station in subway_stations:
        if station not in station_dict.keys():
            station_dict.setdefault(station,set())
            if last_station:
                station_dict.get(last_station).add(station)
                station_dict.get(station).add(last_station)
        elif last_station:
            station_dict.get(last_station).add(station)
            station_dict.get(station).add(last_station)
        else:
            pass
        last_station = station
# print(station_dict)
pprint(station_dict)