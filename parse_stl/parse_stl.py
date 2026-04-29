from stl import mesh
import sys

#arg1 = sys.argv[0]

mesh = mesh.Mesh.from_file('stl_files/jett.stl')

# Access triangles (each triangle has 3 vertices, each vertex has X, Y, Z)
# The shape is (N, 3, 3) where N is the number of triangles
triangles = mesh.vectors

# for i, triangle in enumerate(triangles):
#     print(f"Triangle {i}:")
#     print(f"  Vertex 1: {triangle[0]}")
#     print(f"  Vertex 2: {triangle[1]}")
#     print(f"  Vertex 3: {triangle[2]}")

for i, triangle in enumerate(triangles):
    print("triangle")
    print(f"{triangle[0][0]} {triangle[0][1]} {triangle[0][2]} {triangle[1][0]} {triangle[1][1]} {triangle[1][2]} {triangle[2][0]} {triangle[2][1]} {triangle[2][2]}")

# Access normals for each triangle
normals = mesh.normals
