import pandas as pd
from classes import StopNode

## Conducted data exploration from CSV source files in data_exploration.ipynb.
## Once I had the pipeline down, I exported/copied over to data.py.
## I would have preferred exporting variables, but there's no easy way of doing that
## from ipynb -> py files. This was the easiest approach.   

## ---------- TEST ---------- ##
# Displaying all stops taken on one 51b trip. 
# Note a trip is an instance (?) of routes. One line may have many routes (weekend, weekday, public holiday etc.)
# One route will have many trips (will run multiple times in a day => this will
# be reflected in the time_stop timestamps.)

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
num_nodes = len(node_subset)
stops_test_dict = node_subset.to_dict('index')

# new syntax wow! dictionary comprehension. 
# {key:value for item in collection}
nodes_dict = {
    stop_id: StopNode(**value)
    for stop_id, value in stops_test_dict.items()
}

## edges 
# dict adjacency_list: {int stop_id: {set all_connected_stop_ids}}
edges = stops_test.sort_values(['trip_id', 'stop_sequence'])
edges['next_stop_id'] = edges.groupby('trip_id')['stop_id'].shift(-1)
edges = edges.dropna(subset=['next_stop_id'])
edges['next_stop_id'] = edges['next_stop_id'].astype(int)
edges_dict = edges.groupby('stop_id')['next_stop_id'].apply(set).to_dict()

## ----------- GRAPH TRAVERSAL ALGORITHMS ----------- ##

# For unweighted edges (= no time logic); single route; simplest case
# Note this amounts to fewest number of stops.
def bfs(edges_dict, start, end):
    #return 0
    q = []
    vertices = list(edges_dict.keys())
    visited = [False] * (max(vertices) + 1) # visited[stop_id] = True or False
    path = []

    visited[start] = True
    q.append(start)

    # you can stop when end is visited
    while q and not visited[end]:
        # pop first item in q and add to path
        curr = q.pop()
        path.append(curr)

        # for all unvisited neighbours of current node, visit and add to queue
        for stop in edges_dict[curr]:
            if not visited[stop]:
                visited[stop] = True
                q.append(stop)
    path.append(end)
    return path


#print(bfs(nodes_dict, edges_dict, 743, 747))
path_stop_ids = bfs(edges_dict, 743, 386)
path_coords = [(nodes_dict[coord].lat, nodes_dict[coord].lon) for coord in path_stop_ids]
print(path_coords)
