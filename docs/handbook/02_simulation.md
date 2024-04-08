---
file_format: mystnb
kernelspec:
  name: python3
mystnb:
  number_source_lines: true
---

# Classical Simulation of Quantum Circuits

Performing a quantum computation entails evolving an initial quantum state by applying a sequence of operations (also called gates) that is commonly described as a quantum circuit and measuring the resulting system.
Eventually, the goal should obviously be to do that on a real machine.
However, there are several important reasons for trying to simulate the corresponding computations on a classical machine, particularly in the early stages of the design:
As long as no suitable machines are available (e.g., in terms of scale, feasible computation depth, or accuracy), classical simulation of quantum circuits still allows one to explore and test quantum applications, even if only on a limited scale.
However, also with further progress in the capabilities of the hardware platforms, classical simulation will remain an essential part of the quantum computing design process, since it additionally allows access to _all_ amplitudes of a resulting quantum state in contrast to a real machine that only probabilistically returns measurement results.
Moreover, classical simulation provides means to study quantum error correction, as well as a baseline to estimate the advantage of quantum computers over classical computers.

The classical simulation of quantum circuits is commonly conducted by performing consecutive matrix-vector multiplication, which many simulators realize by storing a dense representation of the complete state vector in memory and evolving it correspondingly (see, e.g., {cite:p}`hanerPetabyteSimulation45Qubit2017,doiQuantumComputingSimulator2019,jonesQuESTHighPerformance2018,guerreschiIntelQuantumSimulator2020, wuFullstateQuantumCircuit2019`).
This approach quickly becomes intractable due to the exponential growth of the quantum state with respect to the number of qubits---quickly rendering such simulations infeasible even on supercomputer clusters.
Simulation methodologies based on decision diagrams {cite:p}`viamontesImprovingGatelevelSimulation2003,willeDecisionDiagramsQuantum2023,zulehnerAdvancedSimulationQuantum2019` are a promising complementary approach that frequently allows to reduce the required memory by exploiting redundancies in the simulated quantum state.

The _MQT_ offers the classical quantum circuit simulator _DDSIM_ that can be used to perform various quantum circuit simulation tasks based on using decision diagrams as a data structure.
This includes strong and weak simulation, approximation techniques, noise-aware simulation, hybrid Schrödinger-Feynman techniques, support for dynamic circuits, the computation of expectation values, and more {cite:p}`zulehnerAdvancedSimulationQuantum2019,zulehnerMatrixVectorVsMatrixMatrix2019,hillmichJustRealThing2020,hillmichAccurateNeededEfficient2020,hillmichConcurrencyDDbasedQuantum2020,hillmichApproximatingDecisionDiagrams2022,grurlConsideringDecoherenceErrors2020,grurlStochasticQuantumCircuit2021,grurlNoiseawareQuantumCircuit2023,burgholzerHybridSchrodingerFeynmanSimulation2021,burgholzerExploitingArbitraryPaths2022,burgholzerSimulationPathsQuantum2022,burgholzerEfficientConstructionFunctional2021`.

```{raw} latex
\vspace*{3.5em}
\begin{minipage}[t]{0.54\linewidth}
\textbf{MQT DDSIM}\newline
\emph{Code:} \url{https://github.com/cda-tum/mqt-ddsim}\newline
\emph{Python Package:} \url{https://pypi.org/p/mqt.ddsim}\newline
\emph{Docs:} \url{https://mqt.readthedocs.io/projects/ddsim}
\end{minipage}%
\hspace{1em}%
\begin{minipage}[t]{0.15\linewidth}
\raisebox{2mm -\dimexpr\depth}{%
\qrcode[height=1.75cm]{https://github.com/cda-tum/mqt-ddsim}
}
\end{minipage}
\vspace*{3.5em}
```

````{only} html
::::{grid} 1
:::{grid-item-card} MQT DDSIM
:text-align: center
```bash
(venv) $ pip install mqt.ddsim
```
+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-ddsim) | [{fab}`python` PyPI](https://pypi.org/project/mqt.ddsim/) | {fa}`fa-thin fa-book` {doc}` Documentation <ddsim:index>`
:::
::::
````

```{raw} latex
\begin{example}
```

```{code-cell} ipython3
:tags: [remove-cell]
%config InlineBackend.figure_formats = ['svg']
```

Consider the following circuit that generates a three-qubit GHZ state:

```{code-cell} ipython3
:tags: [remove-output]
from qiskit import QuantumCircuit

circ = QuantumCircuit(3)
circ.h(2)
circ.cx(2, 1)
circ.cx(1, 0)
circ.measure_all()
```

```{code-cell} ipython3
---
tags: [remove-input]
mystnb:
  figure:
    align: center
    caption: "Quantum circuit for generating a three-qubit GHZ state."
    name: fig-ghz-circuit
---
circ.draw(output="mpl", style="iqp")
```

Then the following listing demonstrates how to simulate this circuit using DDSIM as a backend for IBM Qiskit:

```{code-cell} ipython3
from mqt.ddsim import DDSIMProvider

provider = DDSIMProvider()
backend = provider.get_backend("qasm_simulator")
result = backend.run(circ, shots=10000).result()
result.get_counts()
```

```{raw} latex
\end{example}
```