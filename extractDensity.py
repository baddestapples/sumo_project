import xml.etree.ElementTree as ET
import pprint
import os

basepath=os.path.dirname(os.path.abspath(__file__))
filepath_am=basepath+'/laneData_am.xml'
filepath_ampm=basepath+'/laneData_ampm.xml'
filepath_pm=basepath+'/laneData_pm.xml'
tree = ET.parse(filepath_am)
root = tree.getroot()[0]

edges=['590855737#2.97','590855742#3.305','8832625#3','-590855714#1']

def calcLanes(root):
    lanes=[]
    for edge_node in root:
        if any(edge_node.attrib['id'] in edge for edge in edges):
            for lane_node in edge_node:
                lane = {}
                lane['id'] = lane_node.attrib['id']
                if('laneDensity' in lane_node.attrib.keys()):
                    lane['laneDensity'] = lane_node.attrib['laneDensity']
                else:
                    lane['laneDensity'] = 0
                lanes.append(lane)
    return lanes

laneData = {}
laneData['am'] = calcLanes(root)

tree = ET.parse(filepath_ampm)
root = tree.getroot()[0]

laneData['ampm'] = calcLanes(root)
tree = ET.parse(filepath_pm)
root = tree.getroot()[0]

laneData['pm'] = calcLanes(root)

pp = pprint.PrettyPrinter(depth=6)
print (pp.pprint(laneData))
    
