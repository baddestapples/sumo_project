import xml.etree.ElementTree as ET
import pprint

filepath='C:/Users/Jon/OneDrive/Documents/Project1SUMO/detectors/twinbrook_Detector_results_hourly.xml'
tree = ET.parse(filepath)
root = tree.getroot()

sensor_dict = {}

am_time_end = 10800
ampm_time_end = 32400
pm_time_end = 46800

for child in root:
        id = child.attrib['id']
        begin = float(child.attrib['begin'])
        period = ''
        
        if begin < am_time_end:
                period = 'am'
        elif begin < ampm_time_end:
                period = 'ampm'
        else:
                period = 'pm'

        if not period in sensor_dict.keys():
                sensor_dict[period] = {}

        period_sensor = sensor_dict[period]
        
        if not id in period_sensor.keys():
                period_sensor[id] = {}
                period_sensor[id]['count'] = 0
                period_sensor[id]['flow'] = []

        period_sensor[id]['count'] = period_sensor[id]['count'] + 1
        period_sensor[id]['flow'].append(child.attrib['flow'])

results_dict = {}

for period in sensor_dict:
        results_dict[period] = {}
        for sensor in sensor_dict[period]:
                results_dict[period][sensor] = {}
                flow_added = 0
                for flow_rate in sensor_dict[period][sensor]['flow']:
                        flow_added = flow_added + float(flow_rate)
                
                results_dict[period][sensor]['avgFlow'] = flow_added / sensor_dict[period][sensor]['count']

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(results_dict)
                                        
                
                
	
