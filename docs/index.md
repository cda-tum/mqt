```{only} html
<p align="center">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/mqt_light.png" width="80%">
   <img src="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/mqt_dark.png" width="80%">
 </picture>
 </p>
```

# The MQT Handbook

```{raw} latex
\begin{abstract}
```

Quantum computers are becoming a reality and numerous quantum computing applications with a near-term perspective (e.g., for finance, chemistry, machine learning, and optimization) and with a long-term perspective (e.g., for cryptography or unstructured search) are currently being investigated.
However, designing and realizing potential applications for these devices in a scalable fashion requires automated, efficient, and user-friendly software tools that cater to the needs of end users, engineers, and physicists at every level of the entire quantum software stack.
Many of the problems to be tackled in that regard are similar to design problems from the classical realm for which sophisticated design automation tools have been developed in the previous decades.

The _[Munich Quantum Toolkit (MQT)](https://mqt.readthedocs.io)_ is a collection of software tools for quantum computing developed by the [Chair for Design Automation](https://www.cda.cit.tum.de/) at the [Technical University of Munich](https://www.tum.de/) which explicitly utilizes this design automation expertise.
Our overarching objective is to provide solutions for design tasks across the entire quantum software stack.
This entails high-level support for end users in realizing their _applications_, efficient methods for the _classical simulation_, _compilation_, and _verification_ of quantum circuits, tools for _quantum error correction_, support for _physical design_, and more.
These methods are supported by corresponding _data structures_ (such as decision diagrams) and _core methods_ (such as SAT encodings/solvers).
All of the developed tools are available as open-source implementations and are hosted on [github.com/cda-tum](https://github.com/cda-tum).

````{only} latex
```{note}
A live version of this document is available at [mqt.readthedocs.io](https://mqt.readthedocs.io).
```
````

```{raw} latex
\end{abstract}

\sphinxtableofcontents
```

```{only} html
For a comprehensive visual depiction of the MQT tools, we invite you to download our <a href="_static/flyers/mqt_flyer.pdf" title="Link to MQT flyer">MQT Flyer</a>.

<div style="float: right; margin-top:0em; margin-bottom:3em;">
    <a href="_static/flyers/mqt_flyer.pdf" title="Link to MQT flyer">
        <figure style="display: inline-block;">
            <img style="float: right;display: inline-block; max-height:12em; max-width:100%" src="_static/flyers/mqt_flyer.png" alt="MQT Overview Flyer"/>
            <figcaption style="text-align: center;">MQT Overview Flyer</figcaption>
        </figure>
    </a>
</div>
```

```{toctree}
:caption: The MQT Handbook

handbook/01_intro
handbook/02_simulation
handbook/03_compilation
handbook/04_verification
handbook/05_benchmarking
handbook/06_implementations
handbook/07_conclusions
handbook/references
```

````{only} html
```{toctree}
:caption: Tool Overview and Statistics

overview
stats
```
````

```{toctree}
:hidden:
:caption: Tool Documentation

MQT Core <https://mqt.readthedocs.io/projects/core/en/latest>
MQT DDSIM <https://mqt.readthedocs.io/projects/ddsim/en/latest>
MQT QMAP <https://mqt.readthedocs.io/projects/qmap/en/latest>
MQT QCEC <https://mqt.readthedocs.io/projects/qcec/en/latest>
MQT QECC <https://mqt.readthedocs.io/projects/qecc/en/latest>
MQT Bench <https://mqt.readthedocs.io/projects/bench/en/latest>
MQT Predictor <https://mqt.readthedocs.io/projects/predictor/en/latest>
MQT SyReC <https://mqt.readthedocs.io/projects/syrec/en/latest>
```
