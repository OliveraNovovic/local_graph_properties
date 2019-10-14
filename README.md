# local_graph_properties
Page rank, betweenness centrality, node degree and weighted node degree.
Calculating page rank for weighted (un)directed graph. Nodes in the graph are centers of vornoi polygons that represent 
RBS coverage area, and links are aggregated telecom traffic between RBSs. Weight over edges represent telecom 
traffic intensity. Aim of this project is to calculate mean of page rank values for each polygon over 62 days (graphs). 
Additionally we can plot sequential page rank values for each polygon.

Same method is applied to calculate betweenness centrality of each polygon, node degree and weighted node degree.
In this project betweenness centrality is maybe the most desciptive measure beacuse it is a measure of centrality in a 
graph based on shortest paths. 
For every pair of vertices in a connected graph, there exists at least one shortest path between 
the vertices such that either the number of edges that the path passes through (for unweighted graphs) 
or the sum of the weights of the edges (for weighted graphs) is minimized. 
The betweenness centrality for each vertex is the number of these shortest paths 
that pass through the vertex.
