# sumo_project
    
This project focusses on modelling V2X systems.
Our group simulated five Intersections on Braddock Road staring with Twin Brook Lane and ending with Burke Lake Road and studied their vehicular metrics depending on
the type of traffic phase signals using SUMO and NETEDIT.

=====Important files from the project=====

map.osm file is the openstreet map extracted from webwizard.
braddock.net.xml is used to represent the road network. It shows the junctions, edges and lanes. 
braddock.sumocfg is used to simulate the static phase signals, braddock_actuated.sumocfg is used to simulate the actuated phase signals and 
braddock_synchronize.sumocfg is for simulating the synchronized signals.

====Calculating traffic characteristics====

Detectors and Actuators were added to capture the traffic characteristics.
extractFlow.py, extractDistance.py and extractDensity.py have been used to extract the statistics for the Average flow rate, Average inter-vehicular distance, and the vehicular densities respectively.
