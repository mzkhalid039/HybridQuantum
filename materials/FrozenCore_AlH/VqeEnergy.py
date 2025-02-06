import os
import re
import matplotlib.pyplot as plt

# Function to extract the last energy value from the optimization log file
def extract_last_energy(log_file):
    energy = None
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            for line in lines[::-1]:  # Read lines in reverse order
                if "Iteration" in line and "Energy:" in line:
                    # Extract the energy value using a regular expression
                    match = re.search(r"Energy:\s*([-+]?[0-9]*\.?[0-9]+)", line)
                    if match:
                        energy = float(match.group(1))
                        break
    except Exception as e:
        print(f"Error reading {log_file}: {e}")
    return energy

# Function to search subfolders and collect energy values
def collect_energies(base_dir):
    energy_data = []
    for root, dirs, files in os.walk(base_dir):
        if "optimization_log.txt" in files:
            log_file_path = os.path.join(root, "optimization_log.txt")
            energy = extract_last_energy(log_file_path)
            if energy is not None:
                folder_name = os.path.basename(root)
                energy_data.append((folder_name, energy))
    return energy_data

# Function to save the energy data to a text file and plot it
def save_and_plot_energies(energy_data, output_txt, output_plot):
    # Save to text file
    with open(output_txt, 'w') as file:
        file.write("Folder\tEnergy\n")
        for folder, energy in sorted(energy_data):
            file.write(f"{folder}\t{energy}\n")
    
    # Plot the data
    folders, energies = zip(*sorted(energy_data))
    plt.figure(figsize=(10, 6))
    plt.plot(folders, energies, marker='o', linestyle='-', color='b')
    plt.xlabel("Folder")
    plt.ylabel("Energy")
    plt.title("Energy vs Folder")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_plot)
    plt.show()

# Main script
base_dir = "."  # Current directory
output_txt = "energy_summary.txt"
output_plot = "energy_vs_folder.png"

# Collect energy values from all subfolders
energy_data = collect_energies(base_dir)

# Save the data to a text file and plot it
save_and_plot_energies(energy_data, output_txt, output_plot)

print(f"Energy data saved to {output_txt}")
print(f"Energy plot saved as {output_plot}")

