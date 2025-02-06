import os
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import EfficientSU2
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.providers.fake_provider import Fake20QV1
from qiskit.primitives import StatevectorEstimator as Estimator
from qiskit.primitives import StatevectorSampler as Sampler
from scipy.optimize import minimize
import time
import numpy as np
import matplotlib.pyplot as plt 

# Create a log file path
log_file = 'optimization_log.txt'

# Function to log iteration information to a file
def log_to_file(message):
    with open(log_file, 'a') as log:
        log.write(f"{message}\n")


# Function to read the Hamiltonian from a file
def read_hamiltonian(file_path):
    with open(file_path, 'r') as file:
        hamiltonian = file.read()
    return hamiltonian

# Function to parse the Hamiltonian string and convert it to SparsePauliOp format
def parse_hamiltonian(hamiltonian_string):
    # Remove any newline characters and split the string by " +\n" to get individual terms
    terms = hamiltonian_string.strip().split(" +\n")
    pauli_list = []
    max_qubit_index = 0  # To detect the number of qubits

    for term in terms:
        # Extract the coefficient and operator string
        coeff_part, ops_part = term.split(" [")
        
        # Convert to complex (handling complex parts) and remove imaginary part
        coeff = complex(coeff_part.strip().split("+")[0].strip('()')).real
        
        # Extract the Pauli operators and qubit indices (e.g., 'X0', 'Z1')
        ops = ops_part.strip(']')
        
        # Process the Pauli operators and check the qubit indices
        if ops != "":
            for op in ops.split():
                qubit_index = int(op[1:])  # The qubit index (after the Pauli letter)
                if qubit_index > max_qubit_index:
                    max_qubit_index = qubit_index
        
        pauli_list.append((ops, coeff))

    # The number of qubits is determined by the largest qubit index plus one
    num_qubits = max_qubit_index + 1

    # Build the full Pauli strings for each term
    pauli_terms = []
    for ops, coeff in pauli_list:
        pauli_string = ['I'] * num_qubits  # Initialize as identity for all qubits
        if ops != "":
            for op in ops.split():
                pauli_type = op[0]  # The Pauli operator (X, Y, Z)
                qubit_index = int(op[1:])  # The qubit index
                pauli_string[qubit_index] = pauli_type
        
        # Join the Pauli string to form "ZZII", "XXYY", etc.
        pauli_string = ''.join(pauli_string)
        pauli_terms.append((pauli_string, coeff))

    return pauli_terms, num_qubits

# Define the directory where the file is stored
input_dir = '.'
bk_ham_file_path = os.path.join(input_dir, 'bravyi_kitaev.txt')

# Read the Bravyi-Kitaev Hamiltonian from the file
bk_hamiltonian_str = read_hamiltonian(bk_ham_file_path)

# Parse the Bravyi-Kitaev Hamiltonian and detect the number of qubits
pauli_terms, num_qubits = parse_hamiltonian(bk_hamiltonian_str)

# Create the SparsePauliOp from the parsed Pauli terms
hamiltonian = SparsePauliOp.from_list(pauli_terms)

# Output the number of qubits and the Hamiltonian
sparse_ham_file = os.path.join(input_dir, 'sparse_hamiltonian.txt')
with open(sparse_ham_file, 'w') as f:
    f.write(str(hamiltonian))

print(f"Sparse Hamiltonian written to {sparse_ham_file}")

# Change entanglement strategy to 'linear' or 'circular'
ansatz = EfficientSU2(hamiltonian.num_qubits, entanglement='linear')  # Linear entanglement
ansatz.decompose().draw("mpl", style="iqp")

num_params = ansatz.num_parameters


# Run the sampler job locally using Fake20QV1
backend = Fake20QV1()
pm = generate_preset_pass_manager(backend=backend, optimization_level=3)

# Transpile the ansatz for the backend
ansatz_isa = pm.run(ansatz)

hamiltonian_isa = hamiltonian.apply_layout(layout=ansatz_isa.layout)

def cost_func_vqe(params, ansatz, hamiltonian, sampler):
    """Return estimate of energy from estimator

    Parameters:
        params (ndarray): Array of ansatz parameters
        ansatz (QuantumCircuit): Parameterized ansatz circuit
        hamiltonian (SparsePauliOp): Operator representation of Hamiltonian
        estimator (EstimatorV2): Estimator primitive instance
        cost_history_dict: Dictionary for storing intermediate results

    Returns:
        float: Energy estimate
    """
    pub = (ansatz, [hamiltonian], [params])
    result = sampler.run(pubs=[pub]).result()
    energy = result[0].data.evs[0]
    
    # Log iteration data to file
    log_to_file(f"Iteration {cost_history_dict['iters']} | Energy: {energy}")


    cost_history_dict["iters"] += 1
    cost_history_dict["prev_vector"] = params
    cost_history_dict["cost_history"].append(energy)
    print(f"Iters. done: {cost_history_dict['iters']} [Current cost: {energy}]")

    return energy

cost_history_dict = {
    "prev_vector": None,
    "iters": 0,
    "cost_history": [],
}

x0 = 2 * np.pi * np.random.random(num_params)


estimator = Estimator()
sampler = Sampler()

# SciPy minimizer routine


# Start the optimization and log the start time
start_time = time.time()
log_to_file(f"Optimization started at {time.ctime(start_time)}")


res = minimize(cost_func_vqe, x0, args=(ansatz_isa, hamiltonian_isa, estimator), method="L-BFGS-B", options={'maxiter': 100, 'disp': True})

# End the optimization and log the end time
end_time = time.time()
execution_time = end_time - start_time
log_to_file(f"Optimization finished at {time.ctime(end_time)}")
log_to_file(f"Total execution time: {execution_time} seconds")


# Plot the cost history
fig, ax = plt.subplots()
ax.plot(range(cost_history_dict["iters"]), cost_history_dict["cost_history"])
ax.set_xlabel("Iterations")
ax.set_ylabel("Cost")

# Save the plot as an image
output_image_file = "cost_history_plot.png"
plt.savefig(output_image_file)

# Log the completion of the image generation
log_to_file(f"Cost history plot saved as {output_image_file}")

print(f"Plot saved as {output_image_file}")

