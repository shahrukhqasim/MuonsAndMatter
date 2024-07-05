import numpy as np
import matplotlib.pyplot as plt
from muon_slabs import add, simulate_muon, initialize, collect

# Add function test
print(add(1,2))

# Initialize muon simulation
initialize(5, 4, 4, 4)

# Simulate muon
simulate_muon(100, 100, 100, 1, 0, 0, 0)

# Collect data
data = collect()
print(data)

# Extract x, y, z coordinates
x = data['x']
y = data['y']
z = data['z']

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, s=0.3)

# Set labels
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')
ax.set_title('3D Scatter Plot of Muon Simulation Data')

# Show plot
plt.show()
