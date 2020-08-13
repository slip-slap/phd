import numpy as np

FIBER_VOLUME_FRACTION_GLASS_EPOXY = 0.45
FIBER_VOLUME_FRACTION_BORON_EPOXY = 0.50
FIBER_VOLUME_FRACTION_GRAPHITE_EPOXY = 0.70
FIBER_SPECIFIC_GRAVITY_GRAPHITE = 1.8
FIBER_SPECIFIC_GRAVITY_GLASS    = 2.5
MATRIC_SPECIFIC_GRAVITY_EPOXY = 1.2
#### mm
LAMINATE_LENGTH = 100
LAMINATE_WIDTH = 20


density_of_water = 3.6127*0.01


def get_lamina_mass(volume,material):
    fiber = material.split('_')[0]
    matrice = material.split('_')[1]
    if(fiber == "glass"):
        fiber_volume_fraction = FIBER_VOLUME_FRACTION_GLASS_EPOXY
        fiber_specific_gravity = FIBER_SPECIFIC_GRAVITY_GLASS
    if(fiber == "graphite"):
        fiber_volume_fraction = FIBER_VOLUME_FRACTION_GRAPHITE_EPOXY
        fiber_specific_gravity = FIBER_SPECIFIC_GRAVITY_GRAPHITE
    if(fiber == "boron"):
        fiber_volume_fraction = FIBER_VOLUME_FRACTION_BORON_EPOXY

    if(matrice == 'epoxy'):
        matric_specific_gravity = MATRIC_SPECIFIC_GRAVITY_EPOXY

    
    density = fiber_specific_gravity * fiber_volume_fraction + \
            matric_specific_gravity *  (1 -  fiber_volume_fraction)
    return volume * density/1000

def get_laminate_mass(height,material):
    mass = 0
    for i in range(len(height)):
        volume = LAMINATE_WIDTH * LAMINATE_LENGTH * height[i]*100
        lamina_mass = get_lamina_mass(volume,material[i])
        mass = mass + lamina_mass
    return mass


def get_lamina_cost(volume,material):
    pass



if __name__ == "__main__":
    #volume = 4*100*20*0.5
    #mass = get_lamina_mass(volume,'glass_epoxy')
    #mass = get_lamina_mass(volume,'graphite_epoxy')
    #mass = get_lamina_mass(volume,'glass_epoxy')
    mass = get_laminate_mass([0.005]*4,["graphite_epoxy"]*4)
    print(mass)
    mass = get_laminate_mass([0.005]*4,["glass_epoxy"]*4)
    print(mass)