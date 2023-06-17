# The Munich Quantum Toolkit

<div style="float: right; margin-top:0em; margin-bottom:3em;">
    <a href="_static/flyers/mqt_flyer.pdf" title="Link to MQT flyer">
        <figure style="display: inline-block;">
            <img style="float: right;display: inline-block; max-height:12em; max-width:100%" src="_static/flyers/mqt_flyer.png" alt="MQT Overview Flyer"/>
            <figcaption style="text-align: center;">MQT Overview Flyer</figcaption>
        </figure>
    </a>
</div>

The Munich Quantum Toolkit (MQT) is a collection of design automation tools and software for quantum computing developed by the [Chair for Design Automation](https://www.cda.cit.tum.de/) at the [Technical University of Munich](https://www.tum.de/).
Our overarching objective is to provide solutions for design tasks across the entire quantum software stack.
This entails high-level support for end users in realizing their _Applications_ as well as efficient methods for the _Simulation_, _Compilation_, and _Verification_ of quantum circuits.
Reaching towards the hardware level, we also consider _Quantum Error Correction_ tools and _Physical Design_ considerations.
In all these tools we try to utilize _Data Structures and Core Methods_ facilitating the efficient handling of quantum computations.
For a comprehensive visual depiction of the MQT tools, we invite you to download our <a href="_static/flyers/mqt_flyer.pdf" title="Link to MQT flyer">MQT Flyer</a>.
All of the developed tools are available as open source and are hosted on [GitHub](https://github.com/cda-tum).

## Overview of Tools

The following gives an overview of all repositories, ordered along the quantum software stack from high-level Applications to Physical Design.

### Application

::::{grid} 2
:::{grid-item-card} MQT Bench
:text-align: center
A Quantum Circuit Benchmark Suite

```bash
(venv) $ pip install mqt.bench
```

+++
[{fa}`fa-thin fa-desktop` Application](https://www.cda.cit.tum.de/mqtbench/) | [{fab}`github` GitHub](https://github.com/cda-tum/MQTBench) | [{fab}`python` PyPI](https://pypi.org/project/mqt.bench/)
:::

:::{grid-item-card} MQT ProblemSolver
:text-align: center
A Tool for Solving Problems Using Quantum Computing

```bash
(venv) $ pip install mqt.problemsolver
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/MQTProblemSolver) | [{fab}`python` PyPI](https://pypi.org/project/mqt.problemsolver/)
:::

::::

### Simulation

::::{grid} 2
:::{grid-item-card} MQT DDSIM
:text-align: center
A Tool for Classical Quantum Circuit Simulation based on Decision Diagrams

```bash
(venv) $ pip install mqt.ddsim
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/ddsim) | [{fab}`python` PyPI](https://pypi.org/project/mqt.ddsim/) | {fa}`fa-thin fa-book` {doc}` Documentation <ddsim:index>` | [More ...](https://www.cda.cit.tum.de/research/quantum_simulation/)
:::
::::

### Compilation

::::{grid} 2
:::{grid-item-card} MQT Predictor
:text-align: center
A Tool for Determining Good Quantum Circuit Compilation Options

```bash
(venv) $ pip install mqt.predictor
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/MQTPredictor) | [{fab}`python` PyPI](https://pypi.org/project/mqt.predictor/)
:::
:::{grid-item-card} MQT QMAP
:text-align: center
A Tool for Quantum Circuit Mapping

```bash
(venv) $ pip install mqt.qmap
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/qmap) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qmap/) | {fa}`fa-thin fa-book` {doc}` Documentation <qmap:index>` | [More ...](https://www.cda.cit.tum.de/research/ibm_qx_mapping/)
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
[{fab}`github` GitHub](https://github.com/cda-tum/syrec) | [{fab}`python` PyPI](https://pypi.org/project/mqt.syrec/) | {fa}`fa-thin fa-book` {doc}` Documentation <syrec:index>`
:::
::::

### Verification

::::{grid} 2
:::{grid-item-card} MQT QCEC
:text-align: center
A Tool for Quantum Circuit Equivalence Checking

```bash
(venv) $ pip install mqt.qcec
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/qcec) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qcec/) | {fa}`fa-thin fa-book` {doc}` Documentation <qcec:index>` | [More ...](https://www.cda.cit.tum.de/research/quantum_verification/)
:::
::::

### Quantum Error Correction

::::{grid} 2
:::{grid-item-card} MQT QECC
:text-align: center
A Tool for Quantum Error Correcting Codes

```bash
(venv) $ pip install mqt.qecc
```

+++
[{fab}`github` GitHub](https://github.com/cda-tum/qecc) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qecc/) | {fa}`fa-thin fa-book` {doc}` Documentation <qecc:index>`
:::
::::

### Data Structures and Core Methods

::::{grid} 2
:::{grid-item-card} MQT Core
:text-align: center
The Backbone of the Munich Quantum Toolkit.

Quantum IR | DD Package | ZX Package

+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt.core) | {fa}`fa-thin fa-book` {doc}` Documentation <core:index>`
:::
:::{grid-item-card} MQT DDVis
:text-align: center
A Web-Application Visualizing Decision Diagrams for Quantum Computing
+++
[{fab}`github` GitHub](https://github.com/cda-tum/ddvis) | [{fa}`fa-thin fa-desktop` Application](https://www.cda.cit.tum.de/app/ddvis/) | [More ...](https://www.cda.cit.tum.de/research/quantum_dd/)
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
[{fab}`github` GitHub](https://github.com/cda-tum/qusat) | [{fab}`python` PyPI](https://pypi.org/project/mqt.qusat/)
:::
::::

## Stats

```{include} ../README.md
:start-after: <!-- SPHINX-START -->
```

:::{toctree}
:hidden:

MQT Core <https://mqt.readthedocs.io/projects/core/en/latest>
MQT DDSIM <https://mqt.readthedocs.io/projects/ddsim/en/latest>
MQT QMAP <https://mqt.readthedocs.io/projects/qmap/en/latest>
MQT QCEC <https://mqt.readthedocs.io/projects/qcec/en/latest>
MQT QECC <https://mqt.readthedocs.io/projects/qecc/en/latest>
MQT SyReC <https://mqt.readthedocs.io/projects/syrec/en/latest>

:::
