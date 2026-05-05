#**Public Transit Router (SF Bay Area)**#

A public transit routing engine built from the ground up using raw GTFS (General Transit Feed Specification) data to solve the "Shortest Path" problem in dynamic transit networks. I love the Bay Area and I love public transit! <3 

**Project Vision**
Most routing applications rely on opaque third-party APIs. This project explores the underlying engineering required to turn static tabular schedules into a live, traversable graph. The goal is to move beyond simple geographic distance and model the network based on connectivity, sequence, and eventually, the temporal constraints of a real-world schedule.

**Current Progress: Infrastructure & Connectivity**
I have established a solid data pipeline and visualization engine:

Vectorized Data Pipeline: Instead of slow iterative processing, I used Pandas vectorized operations (Shift, GroupBy, and Apply) to map relationships between thousands of stops. 

Graph Architecture: Nodes are modeled as discrete objects containing geographic metadata, while edges represent the directed flow of a specific transit trip.

Connectivity Routing (BFS): Successfully implemented a Breadth-First Search algorithm to determine the "naive" shortest path across test cases. BFS works here because edges are unweighted, therefore the shortest path is simply the least number of 'edges', which is the least number of stops. The algorithm successfully "hops" between different bus lines at shared stops, creating an interconnected East Bay transit map.

Interactive UI: Built a frontend using Streamlit and Folium that renders the stops and calculated shortest paths on an interactive map.

**Scaling**
As I scaled from a single-trip proof of concept to the entire AC Transit dataset, I hit a wall. The full network represents a significant jump in memory overhead and computational complexity. Loading the entire state into memory caused significant bloat, to the point of exceeding the limits of (my hosting service) Render's memory limit.

I am working on refactoring the data representation to be more memory-efficient.

**What’s Next?**

Temporal logic + Dijkstra’s algorithm: Transitioning from "least stops" to "least time." I weight the edges based on the travel time between stops and accounting for the "waiting time" at platforms.

Optimization: More efficient data representation that uses less memory. Also some way to speed up the graph traversal process - some form of caching maybe. 

Better visualization: Using different colours to represent "hopping" between lines.
