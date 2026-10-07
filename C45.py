def force_calculation(mass,acceleration):
    force = mass * acceleration
    return force
def main():
    mass = 40
    acceleration = 50
    print(f"Mass: {mass}")
    print(f"Acceleration: {acceleration}")
    print(f"Force: {force_calculation(mass,acceleration)}")
main()