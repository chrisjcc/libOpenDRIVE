# tests/test_binding.py
import opendrive_bindings

# Load an XODR file
map = opendrive_bindings.OpenDriveMap("tests/test.xodr", center_map=False)
assert isinstance(map.xodr_file, str)
assert isinstance(map.proj4, str)
assert isinstance(map.x_offs, float)
assert isinstance(map.y_offs, float)

# Test roads
roads = map.get_roads()
assert isinstance(roads, list)
if roads:
    print(f"Found {len(roads)} roads")
    assert isinstance(map.id_to_road, dict)

# Test junctions
junctions = map.get_junctions()
assert isinstance(junctions, list)
if junctions:
    print(f"Found {len(junctions)} junctions")
    assert isinstance(map.id_to_junction, dict)

# Test road network mesh
eps = 0.1  # Provide eps value
road_network_mesh = map.get_road_network_mesh(eps)
assert isinstance(road_network_mesh, opendrive_bindings.RoadNetworkMesh)
assert isinstance(road_network_mesh.get_mesh(), opendrive_bindings.Mesh3D)

# Test lanes mesh
lanes_mesh = road_network_mesh.lanes_mesh
assert isinstance(lanes_mesh, opendrive_bindings.LanesMesh)
if lanes_mesh.vertices:
    vert_idx = 0
    print(f"Lane s0: {lanes_mesh.get_lanesec_s0(vert_idx)}")
    print(f"Lane ID: {lanes_mesh.get_lane_id(vert_idx)}")
    print(f"Lane section interval: {lanes_mesh.get_idx_interval_lanesec(vert_idx)}")
    print(f"Lane interval: {lanes_mesh.get_idx_interval_lane(vert_idx)}")
    print(f"Lane outline indices: {lanes_mesh.get_lane_outline_indices()}")
    print(f"Lane section start indices: {lanes_mesh.lanesec_start_indices}")
    print(f"Lane start indices: {lanes_mesh.lane_start_indices}")

# Test roadmarks mesh
roadmarks_mesh = road_network_mesh.roadmarks_mesh
assert isinstance(roadmarks_mesh, opendrive_bindings.RoadmarksMesh)
if roadmarks_mesh.vertices:
    vert_idx = 0
    print(f"Roadmark type: {roadmarks_mesh.get_roadmark_type(vert_idx)}")
    print(f"Roadmark interval: {roadmarks_mesh.get_idx_interval_roadmark(vert_idx)}")
    print(f"Roadmark outline indices: {roadmarks_mesh.get_roadmark_outline_indices()}")
    print(f"Roadmark type start indices: {roadmarks_mesh.roadmark_type_start_indices}")

# Test road objects mesh
road_objects_mesh = road_network_mesh.road_objects_mesh
assert isinstance(road_objects_mesh, opendrive_bindings.RoadObjectsMesh)
if road_objects_mesh.vertices:
    vert_idx = 0
    print(f"Road object ID: {road_objects_mesh.get_road_object_id(vert_idx)}")
    print(f"Road object interval: {road_objects_mesh.get_idx_interval_road_object(vert_idx)}")
    print(f"Road object start indices: {road_objects_mesh.road_object_start_indices}")

# Test road signals mesh
road_signals_mesh = road_network_mesh.road_signals_mesh
assert isinstance(road_signals_mesh, opendrive_bindings.RoadSignalsMesh)
if road_signals_mesh.vertices:
    vert_idx = 0
    print(f"Road signal ID: {road_signals_mesh.get_road_signal_id(vert_idx)}")
    print(f"Signal interval: {road_signals_mesh.get_idx_interval_signal(vert_idx)}")
    print(f"Signal start indices: {road_signals_mesh.road_signal_start_indices}")

# Test routing graph
routing_graph = map.get_routing_graph()
assert isinstance(routing_graph, opendrive_bindings.RoutingGraph)
