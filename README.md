# TSP-For-Map

# I've thought of the idea of creating this pj when I need to go to lots of places in 1 day. 
## Review: 
    - This project implements a Python-based tool for calculating the optimal route to visit multiple user-defined locations. Utilizing OpenStreetMap (OSM) data via the OSMnx library, it builds a graph of road networks within a specified area and then applies a Nearest Neighbor (NN) algorithm to determine the shortest path. Starting from an initial point, the algorithm visits each location and returns to the starting point, creating a route that minimizes total travel distance. This approach is highly suitable for routing applications in urban settings, logistics, and personal travel.

## Issues found in particular situations:
    - Travelling: Cannot design the best route to get through as many tourist attractions as possible.
    - Delivery: Deliver for a local restaurant or small business, they cannot afford to spend for a TSP (Travelling salesman problem) application so to calculate the best path to reach for the location(s) while there are many order is hard.
