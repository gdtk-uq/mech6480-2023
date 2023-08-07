from convection_diffusion_upwind_TODO import convection_diffusion_upwind
#from convection_diffusion_central_diff_TODO import convection_diffusion_central_diff
#from convection_diffusion_quick import convection_diffusion_quick

import numpy as np
import matplotlib.pyplot as plt

def my_solve(num_cells, F, D, phi_0, phi_L):
    A, b = convection_diffusion_upwind(num_cells, F, D, phi_0, phi_L)
    return np.linalg.solve(A, b)

def my_l2_norm(num_cells, x_location, concentration, function):
    #"""TODO: implement l2norm"""
    print("not yet implemented")
    return 

if __name__ == '__main__':
    # SYSTEM PARAMETERS:
    Gamma = 0.1             # kg/m.s      
    u = 0.1                 # m/s
    rho = 1.0               # kg/m3
    length = 1.              # m

    # BOUNDARIES:
    phi_0 = 1
    phi_L = 0
    def analytic_solution(x):
        return phi_0 + (phi_L - phi_0) * (np.exp(rho*u*x/Gamma)-1) / (np.exp(rho*u*length/Gamma) -1)

    fig, ax = plt.subplots(1)
    test_resolutions = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    l2 = np.zeros((len(test_resolutions)),dtype=float)

    for indx, num_cells in enumerate(test_resolutions):
        #"""TODO implement convergence study"""
        print("not yet implemented")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot([length/x for x in test_resolutions], [(0.4/y)**2 for y in test_resolutions],'k-')
    ax.plot([length/x for x in test_resolutions], [(0.4/y) for y in test_resolutions],'k--')
    plt.grid()
    plt.show()
