---
file_format: mystnb
kernelspec:
  name: python3
mystnb:
  number_source_lines: true
---

# Compilation of Quantum Circuits

In today's digital world, creating computer programs has become a crucial element of software development.
With the advent of high-level programming languages such as C++ or Python, the development process has become simpler and more efficient.
These languages enable developers to produce code that is more human-readable and understandable without having to worry about the underlying hardware's low-level features.
But before these programs can be executed on a computer, they must be translated into machine code that the computer can process.
This procedure is known as _compilation_, and it entails converting high-level code into a binary format that the computer's processor can directly execute.
By making it easier for more people to create computer programs, this has enabled the development of complex software applications that can run on many different platforms.

Just as in classical computing, the design of quantum circuits and the development of quantum algorithms are fundamental in the development of quantum computing applications.
Quantum circuits are analogous to classical functions or programs in that they are a sequence of quantum gates that perform specific operations on quantum bits or qubits.
Similarly to classical processors, quantum processors can only execute a certain set of native instructions, and they might further limit the qubits on which these operations might be applied.
Thus, any high-level quantum circuit (describing a quantum algorithm) must be _compiled_ into a representation that can be executed on the targeted device.
Most importantly, the resulting quantum circuit must only use gates that are native to the device on which it shall be executed.
If the device only has limited connectivity between its qubits, it must only apply gates to qubits that are connected on the device.
Naturally, the efficiency of this compilation process is critical because it can have a significant impact on the performance of the resulting quantum program.
Inefficient compilation can lead to longer execution times, higher error rates, and reduced accuracy in the final result.
Therefore, developing efficient compilation methods for quantum programs is essential to overcome the challenges of quantum computing and realize the potential of this technology.

In the following, we mainly focus on the _quantum circuit mapping_ task.
This is a crucial step in the compilation flow, as it directly affects the feasibility and performance of the quantum circuit on a given device.
It involves finding a way to map the qubits of a quantum circuit to the qubits of a quantum device, while respecting the limited connectivity constraints of the device and minimizing the overhead of additional gates.
In most cases, it is not possible to statically define a mapping of the circuit's qubits to the device's qubits such that all gates of the circuit conform to the connectivity limitations of the device.
Consequently, this mapping has to change dynamically throughout the circuit.
This can be accomplished by using _SWAP_ gates that allow the position of two logical qubits on the architecture to be interchanged.
However, since any additional gate increases the error probability and, hence, decreases the chances of success, it is vital to keep the number of additionally added gates as low as possible.
It has been shown that even this small part in the compilation flow is an NP-complete problem {cite:p}`boteaComplexityQuantumCircuit2018`.

The _MQT_ offers the quantum circuit mapping tool QMAP that allows one to generate circuits which satisfy all constraints given by the targeted architecture and, at the same time, keep the overhead in terms of additionally required quantum gates as low as possible.
More precisely, different approaches based on design automation techniques are provided, which are generic and can be easily configured for future architectures.
Among them is a general solution for arbitrary circuits based on informed-search algorithms {cite:p}`zulehnerEfficientMethodologyMapping2019,hillmichExploitingQuantumTeleportation2021` as well as a solution for obtaining mappings ensuring minimal overhead with respect to SWAP gate insertions {cite:p}`willeMappingQuantumCircuits2019,burgholzerLimitingSearchSpace2022`.
+++ {}

```{raw} latex
\vspace*{3em}
\begin{minipage}[t]{0.54\linewidth}
\textbf{MQT QMAP}\newline
\emph{Code:} \url{https://github.com/cda-tum/mqt-qmap}\newline
\emph{Python Package:} \url{https://pypi.org/p/mqt.qmap}\newline
\emph{Docs:} \url{https://mqt.readthedocs.io/projects/qmap}
\end{minipage}%
\hspace{1em}%
\begin{minipage}[t]{0.15\linewidth}
\raisebox{2mm -\dimexpr\depth}{%
\qrcode[height=1.75cm]{https://github.com/cda-tum/mqt-qmap}
}
\end{minipage}
\vspace*{3em}
```

````{only} html
::::{grid} 1
:::{grid-item-card} MQT QMAP
:text-align: center
```bash
(venv) $ pip install mqt.qmap
```
+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-qmap) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qmap/) | {fa}`fa-thin fa-book` {doc}` Documentation <qmap:index>`
:::
::::
````

```{raw} latex
\begin{example}
```

Assume we want to perform the computation from {numref}`fig-ghz-circuit` on a five-qubit IBM quantum computer described by the following coupling map:

```{code-cell} ipython3
:tags: [remove-cell]
%config InlineBackend.figure_formats = ['svg']

from qiskit import QuantumCircuit

circ = QuantumCircuit(3)
circ.h(2)
circ.cx(2, 1)
circ.cx(1, 0)
circ.measure_all()
```

```{code-cell} ipython3
from qiskit.providers.fake_provider import Fake5QV1

backend = Fake5QV1()
```

```{code-cell} ipython3
---
tags: [remove-input]
mystnb:
  figure:
    align: center
    caption: "Generic five-qubit IBM device."
    name: fig-device
---
from qiskit.visualization import plot_gate_map

plot_gate_map(backend)
```

Then, mapping the circuit to that device merely requires the following lines of Python:

```{code-cell} ipython3
from mqt.qmap import compile

circ_mapped, results = compile(circ, backend)
```

```{code-cell} ipython3
---
tags: [remove-input]
mystnb:
  figure:
    align: center
    caption: "Quantum circuit from {numref}`fig-ghz-circuit` mapped to the five-qubit device shown in {numref}`fig-device`."
    name: fig-ghz-circuit-mapped
---
circ_mapped.draw(output='mpl', style='iqp')
```

```{raw} latex
\end{example}
```

_MQT_ offers many more methods for various compilation tasks, such as Clifford circuit synthesis {cite:p}`pehamDepthoptimalSynthesisClifford2023, schneiderSATEncodingOptimal2023`, determining optimal sub-architectures {cite:p}`pehamOptimalSubarchitecturesQuantum2023`, compiler optimization {cite:p}`quetschlichCompilerOptimizationQuantum2023`, or compilation techniques for different architectures {cite:p}`schoenbergerUsingBooleanSatisfiability2024,schoenbergerCyclebasedShuttlingTrappedIon2024,schoenbergerShuttlingScalableTrappedIon2024,schmidHybridCircuitMapping2024,schmidComputationalCapabilitiesCompiler2024`.