def calculate_energy(mass_kg):
    c = 300000000
    energy_joules = mass_kg * c*c
    return energy_joules

mass_kg = int(input("Enter mass in KG: "))
energy_joules = calculate_energy(mass_kg)

print("Equivalent energy in Joules: ",energy_joules)
