# Open-Source Implementations

All tools that have been developed as part of the _MQT_ are publicly available on [github.com/cda-tum](https://github.com/cda-tum}{github.com/cda-tum).
Many of these tools are powered by a state-of-the-art decision diagram package for quantum computing and a high-performance ZX-calculus library.
Together with a comprehensive intermediate representation for quantum computations these libraries form

```{raw} latex
\begin{minipage}[t]{0.54\linewidth}
\textbf{MQT Core}\newline
\emph{Code:} \url{https://github.com/cda-tum/mqt-core}\newline
\emph{Python Package:} \url{https://pypi.org/p/mqt.core}\newline
\emph{Documentation:} \url{https://mqt.readthedocs.io/projects/core}
\end{minipage}%
\hspace{1em}%
\begin{minipage}[t]{0.15\linewidth}
\raisebox{2mm -\dimexpr\depth}{%
\qrcode[height=1.75cm]{https://github.com/cda-tum/mqt-core}
}
\end{minipage}
```

````{only} html
::::{grid} 1
:::{grid-item-card} MQT Core
:text-align: center
```bash
(venv) $ pip install mqt.core
```
+++
[{fab}`github` GitHub](https://github.com/cda-tum/mqt-core) | [{fab}`python` PyPI](https://pypi.org/project/mqt.core/) | {fa}`fa-thin fa-book` {doc}` Documentation <core:index>`
:::
::::
````

All tools have been mainly implemented in C++, but strive to be as user-friendly as possible for the community.
Hence, push-button solutions are provided through Python bindings, pre-built Python wheels are available for all major platforms and Python versions, and all tools integrate natively with IBM's Qiskit.
All tools are actively maintained and well documented.
