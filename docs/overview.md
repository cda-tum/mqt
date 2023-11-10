# Overview of Tools

The following gives an overview of all repositories, ordered along the quantum software stack from high-level Applications to Physical Design.

- [Application](#application)
- [Simulation](#simulation)
- [Compilation](#compilation)
- [Verification](#verification)
- [Quantum Error Correction](#quantum-error-correction)
- [Data Structures and Core Methods](#data-structures-and-core-methods)
- [Physical Design](#physical-design)

---


## Application

::::{grid} 2
:::{grid-item-card} MQT Bench
:text-align: center
A Quantum Circuit Benchmark Suite

```bash
(venv) $ pip install mqt.bench
```

+++
[{fa}`fa-thin fa-desktop` Application](https://www.cda.cit.tum.de/mqtbench/) | [{fab}`github` GitHub](https://github.com/cda-tum/mqt-bench) | [{fab}`python` PyPI](https://pypi.org/project/mqt.bench/) | {fa}`fa-thin fa-book` {doc}` Documentation <bench:index>`
:::

:::{grid-item-card} MQT ProblemSolver
:text-align: center
A Tool for Solving Problems Using Quantum Computing

```bash
(venv) $ pip install mqt.problemsolver
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-problemsolver) | [{fab}`python` PyPI](https://pypi.org/project/mqt.problemsolver/)
:::

::::

## Simulation

::::{grid} 2
:::{grid-item-card} MQT DDSIM
:text-align: center
A Tool for Classical Quantum Circuit Simulation based on Decision Diagrams

```bash
(venv) $ pip install mqt.ddsim
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-ddsim) | [{fab}`python` PyPI](https://pypi.org/project/mqt.ddsim/) | {fa}`fa-thin fa-book` {doc}` Documentation <ddsim:index>` | [More ...](https://www.cda.cit.tum.de/research/quantum_simulation/)
:::
::::

## Compilation

::::{grid} 2
:::{grid-item-card} MQT Predictor
:text-align: center
A Tool for Determining Good Quantum Circuit Compilation Options

```bash
(venv) $ pip install mqt.predictor
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-predictor) | [{fab}`python` PyPI](https://pypi.org/project/mqt.predictor/) | {fa}`fa-thin fa-book` {doc}` Documentation <predictor:index>`
:::
:::{grid-item-card} MQT QMAP
:text-align: center
A Tool for Quantum Circuit Mapping

```bash
(venv) $ pip install mqt.qmap
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-qmap) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qmap/) | {fa}`fa-thin fa-book` {doc}` Documentation <qmap:index>` | [More ...](https://www.cda.cit.tum.de/research/ibm_qx_mapping/)
:::
:::{grid-item-card} MQT IonShuttler
:text-align: center
A Tool for Generating Shuttling Schedules for QCCD Architectures
+++
[{fab}`github` GitHub](https://github.com/cda-tum/ion-shuttler)
:::
:::{grid-item-card} MQT Qudits
:text-align: center
A Tool for Adaptive Compilation of Multi-Level Quantum Operations and Entangling Gates for High-Dimensional Quantum Systems
+++
[{fab}`github` GitHub](https://github/com/cda-tum/qudit-compilation) | [{fab}`github` GitHub](https://github/com/cda-tum/qudit-entanglement-compilation)
:::
:::{grid-item-card} MQT SyReC
:text-align: center
A Tool for the Synthesis of Reversible Circuits/Quantum Computing Oracles

```bash
(venv) $ pip install mqt.syrec
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-syrec) | [{fab}`python` PyPI](https://pypi.org/project/mqt.syrec/) | {fa}`fa-thin fa-book` {doc}` Documentation <syrec:index>`
:::
::::

## Verification

::::{grid} 2
:::{grid-item-card} MQT QCEC
:text-align: center
A Tool for Quantum Circuit Equivalence Checking

```bash
(venv) $ pip install mqt.qcec
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-qcec) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qcec/) | {fa}`fa-thin fa-book` {doc}` Documentation <qcec:index>` | [More ...](https://www.cda.cit.tum.de/research/quantum_verification/)
:::
::::

## Quantum Error Correction

::::{grid} 2
:::{grid-item-card} MQT QECC
:text-align: center
A Tool for Quantum Error Correcting Codes

```bash
(venv) $ pip install mqt.qecc
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-qecc) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qecc/) | {fa}`fa-thin fa-book` {doc}` Documentation <qecc:index>`
:::
::::

## Data Structures and Core Methods

::::{grid} 2
:::{grid-item-card} MQT Core
:text-align: center
The Backbone of the Munich Quantum Toolkit.

Quantum IR | DD Package | ZX Package

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-core) | {fa}`fa-thin fa-book` {doc}` Documentation <core:index>`
:::
:::{grid-item-card} MQT DDVis
:text-align: center
A Web-Application Visualizing Decision Diagrams for Quantum Computing
+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-ddvis) | [{fa}`fa-thin fa-desktop` Application](https://www.cda.cit.tum.de/app/ddvis/) | [More ...](https://www.cda.cit.tum.de/research/quantum_dd/)
:::
:::{grid-item-card} MQT LogicBlocks
:text-align: center
An Interface Library for SAT/SMT Abstractions
+++
[{fab}`github` GitHub](https://github.com/cda-tum/logicblocks)
:::
:::{grid-item-card} MQT QuSAT
:text-align: center
A Tool for Encoding Quantum Computing using Satisfiability Testing (SAT) Techniques

```bash
(venv) $ pip install mqt.qusat
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-qusat) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qusat/)
:::
::::

## Physical Design

::::{grid} 2
:::{grid-item-card} MQT DASQA
:text-align: center
A Tool for Designing Alternative Superconducting Quantum Architectures

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-dasqa)
:::
::::
