import pandas as pd
from classes import StopNode

# resource ID for stop_times: 4e504fcf-c784-4a58-944a-14bb540dbbc7
stops = pd.read_csv('data/stops.csv')
stop_times = pd.read_csv('data/stop_times.csv')
trips = pd.read_csv('data/trips.csv')

# stop times for trip 9877020 for route 51b
stops_test = pd.merge(stop_times, stops, how='left', on='stop_id')
stops_test = stops_test.loc[stops_test['trip_id']==9877020, ['stop_id', 'stop_sequence', 'stop_name', 'trip_id', 'arrival_time', 'departure_time', 'stop_lat', 'stop_lon']]

## making graph representation (dicts for nodes and adjacency list for edges) ##

## nodes
node_subset = stops_test.set_index('stop_id')
node_subset = node_subset.loc[:, ['stop_name', 'stop_lat', 'stop_lon']]
stops_test_dict = node_subset.to_dict('index')

# new syntax wow! dictionary comprehension. 
# {key:value for item in collection}
nodes_dict = {
    stop_id: StopNode(**value)
    for stop_id, value in stops_test_dict.items()
}

## edges
edges = stops_test.sort_values(['trip_id', 'stop_sequence'])
edges['next_stop_id'] = edges.groupby('trip_id')['stop_id'].shift(-1)
edges = edges.dropna(subset=['next_stop_id'])
edges_dict = edges.groupby('stop_id')['next_stop_id'].apply(set).to_dict()
