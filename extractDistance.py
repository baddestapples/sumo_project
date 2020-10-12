import xml.etree.ElementTree as ET
import pprint

am_time_end = 10800
ampm_time_end = 32400
pm_time_end = 46800

basepath='C:/Users/Jon/OneDrive/Documents/Project1SUMO/detectors/'
files=['twinbrook_EB0_Detector_results.xml',
       'twinbrook_EB1_Detector_results.xml',
       'twinbrook_EB2_Detector_results.xml',
       'twinbrook_EB3_Detector_results.xml',
       'twinbrook_NB0_Detector_results.xml',
       'twinbrook_NB1_Detector_results.xml',
       'twinbrook_SB0_Detector_results.xml',
       'twinbrook_WB0_Detector_results.xml',
       'twinbrook_WB1_Detector_results.xml',
       'twinbrook_WB2_Detector_results.xml']

results = {}

for filename in files:
    filepath=basepath + filename
    tree = ET.parse(filepath)
    root = tree.getroot()
    skip = True
    prev_gap = None
    for child in root:        
        if('gap' in child.attrib.keys()):
            gap = float(child.attrib['gap'])

            if skip:
                skip = False
                prev_gap = gap
                continue
            
            id = child.attrib['id']
            time = float(child.attrib['time'])
            period = ''
            if time < am_time_end:
                period = 'am'
            elif time < ampm_time_end:
                period = 'ampm'
            else:
                period = 'pm'

            if not period in results.keys():
                results[period] = {}

            period_dict = results[period]
            
            if not id in period_dict.keys():
                period_dict[id] = {}
                period_dict[id]['count'] = 0
                period_dict[id]['distance'] = []
                              
            period_dict[id]['count'] = period_dict[id]['count'] + 1
            speed = float(child.attrib['speed'])
            # the front of the car enters so we need to subtract the length of the
            # car to get the actual distance between cars
            length = float(child.attrib['length'])
            period_dict[id]['distance'].append(speed * prev_gap - length)
            prev_gap = gap

for period in results:
    period_dict = results[period]
    for sensor in period_dict:
        sensor_dict = period_dict[sensor]
        sum_distance = sum(sensor_dict['distance'])
        avg_distance = sum_distance / max(1,(sensor_dict['count'] - 1))
        period_dict[sensor] = avg_distance

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(results)
