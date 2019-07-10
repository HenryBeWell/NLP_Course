from __future__ import unicode_literals
import json

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
last_station = None
for subway_line,subway_stations in subway_items.items():
    stations = []
    for station in subway_stations:
        # if station not in station_dict.keys() and last_station != None:
        if station not in station_dict.keys():
            station_dict.setdefault(station,[])
            if last_station:
                station_dict.get(last_station).append(station)
                station_dict.get(station).append(last_station)
        elif station not in station_dict.get(last_station):
            station_dict.get(last_station).append(station)
        elif last_station not in station_dict.get(station):
            station_dict.get(station).append(last_station)
        last_station = station

with open('2.json','w') as fp:
    json_obj = json.dumps(station_dict,ensure_ascii=False)
    fp.writelines(json_obj)