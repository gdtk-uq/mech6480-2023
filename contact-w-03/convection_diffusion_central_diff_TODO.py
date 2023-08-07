import matplotlib.pyplot as plt
import numpy as np

def convection_diffusion_central_diff(num_cells, convective_flux, diffusive_conductance, boundary_left, boundary_right):
    """ Generate solution matrix for the convection-diffusion equation with FVM """
    a_W = # TODO: apply your discretisation
    a_E = # TODO: apply your discretisation
    a_P = # TODO: apply your discretisation

    # INTERNAL
    A = np.diag(np.repeat(-a_W, num_cells-1),-1) + \
        np.diag(np.repeat(a_P, num_cells),0) + \
        np.diag(np.repeat(-a_E, num_cells-1),1)
    b = np.zeros(num_cells)
    
    A[0,0] = # TODO: apply your discretisation
    A[-1,-1] = # TODO: apply your discretisation
    
    b[0] = # TODO: apply your discretisation
    b[-1] = # TODO: apply your discretisation
    return A, b

# SYSTEM PARAMETERS:
Gamma = 0.1             # kg/m.s      
u = 2.5                 # m/s
rho = 1.0               # kg/m3
length = 1              # m

# BOUNDARIES:
phi_0 = 1
phi_L = 0

# GRID GENERATION
num_cells = 50              #[-]
dx = length / (num_cells)  #[m]
x_locations = np.linspace(0.5*dx,(num_cells-0.5)*dx,num_cells)

# CONVECTIVE AND DIFFUSIVE TERMS
#   note: you may need to calculate these locally if rho, u, Gamma, or dx is not consistent in the domain.
F = rho * u
D = Gamma / dx

# SYSTEM OF EQUATIONS
A, b = convection_diffusion_central_diff(num_cells, F, D, phi_0, phi_L)
concentration = np.linalg.solve(A, b)

def analyticSolution(x):
    return phi_0 + (phi_L - phi_0) * (np.exp(rho*u*x/Gamma)-1) / (np.exp(rho*u*length/Gamma) -1)
x = np.linspace(0,length,100)
solution = analyticSolution(x)
plt.plot(x, solution, 'r--')
        
plt.plot(x_locations, concentration, 'b-o')
plt.xlabel('Distance along hallway (m)')
plt.ylabel('concentration')
plt.show()