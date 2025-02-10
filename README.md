# Hybrid Classical-Quantum Simulation Workflow

---

##  Overview
This repository provides a **Hybrid Classical-Quantum Workflow** for **molecular simulations**, leveraging both **classical and quantum computing tools**.

### 🔹 **Key Topics**
- **Hybrid Classical-Quantum Workflow** for molecular simulations.
- **Tools Used**: Qiskit, PySCF, Qiskit Nature, OpenFermion, ASE, VASP.
- **Applications**: Ground-state energy calculations, potential energy surfaces.

---

## 📦 Dependencies

The following Python libraries are required:

- [Qiskit](https://qiskit.org/)
- [Qiskit IBM Runtime](https://qiskit.org/documentation/partners/qiskit_ibm_runtime/)
- [OpenFermion](https://github.com/quantumlib/OpenFermion)
- [OpenFermion-PySCF](https://github.com/quantumlib/OpenFermion-PySCF)
- [Py3Dmol](https://github.com/3dmol/3Dmol.js)
- [SciPy](https://scipy.org/)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)

---

## 🔧 Installation

To set up your environment, install the required dependencies using:

```bash
pip install qiskit qiskit-ibm-runtime openfermion openfermionpyscf py3Dmol numpy scipy matplotlib

##  **Simulation Workflow**
The simulation follows these **key steps**:

1️⃣ **Build molecular geometry** (PySCF, ASE)  
2️⃣ **Optimize atomic and geometrical parameters** with **DFT** (VASP)  
3️⃣ **Perform Hartree-Fock calculations** (PySCF, Qiskit Nature)  
4️⃣ **Define active space** and map it to a **qubit Hamiltonian** (OpenFermion)  
5️⃣ **Solve using quantum algorithms**: VQE, QPE (Qiskit, Qiskit Nature)  
6️⃣ **Analyze results**: Potential energy surface, ground-state energy  

---

## **Workflow Flowchart**
![Workflow](https://github.com/user-attachments/assets/7b142974-1c2b-4fa3-ba0f-8a1402dd2818)



## References

1. **Qiskit Documentation** - [https://qiskit.org/documentation/](https://qiskit.org/documentation/)
2. **PySCF Documentation** - [https://pyscf.org/](https://pyscf.org/)
3. **Qiskit Nature** - [https://qiskit.org/ecosystem/nature/](https://qiskit.org/ecosystem/nature/)
4. **OpenFermion (Google Research)** - [https://github.com/quantumlib/OpenFermion](https://github.com/quantumlib/OpenFermion)
5. **Atomic Simulation Environment (ASE)** - [https://wiki.fysik.dtu.dk/ase/](https://wiki.fysik.dtu.dk/ase/)
6. **VASP (Vienna Ab-initio Simulation Package)** - [https://www.vasp.at/](https://www.vasp.at/)
7. **Variational Quantum Eigensolver (VQE) - Peruzzo et al., 2014** - [DOI: 10.1038/ncomms5213](https://doi.org/10.1038/ncomms5213)
8. **Bravyi-Kitaev Transformation - Bravyi & Kitaev, 2002** - [arXiv:quant-ph/0003137](https://arxiv.org/abs/quant-ph/0003137)
9. **Jordan-Wigner Transformation - Jordan & Wigner, 1928** - [https://doi.org/10.1007/BF01331938](https://doi.org/10.1007/BF01331938)
10. **Quantum Phase Estimation (QPE) - Kitaev, 1995** - [arXiv:quant-ph/9511026](https://arxiv.org/abs/quant-ph/9511026)
11. **Unitary Coupled Cluster (UCC) Ansatz for Quantum Chemistry - Romero et al., 2018** - [arXiv:1701.02691](https://arxiv.org/abs/1701.02691)
12. **Quantum Computational Chemistry - McArdle et al., 2020** - [DOI: 10.1103/RevModPhys.92.015003](https://doi.org/10.1103/RevModPhys.92.015003)
13. **Classical Electronic Structure Methods (Hartree-Fock, DFT, CASSCF, MP2)** - Szabo & Ostlund, *Modern Quantum Chemistry*, 1989.

---
