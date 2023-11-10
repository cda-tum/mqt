<p align="center">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/mqt_light.png" width="80%">
   <img src="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/mqt_dark.png" width="80%">
 </picture>
 </p>

# The Munich Quantum Toolkit (MQT)

The Munich Quantum Toolkit (MQT) is a collection of design automation tools and software for quantum computing developed by the [Chair for Design Automation](https://www.cda.cit.tum.de/) at the [Technical University of Munich](https://www.tum.de/).

<p align="center">
  <a href="https://mqt.readthedocs.io/en/latest/">
  <img width=50% src="https://img.shields.io/badge/documentation-blue?style=for-the-badge&logo=read%20the%20docs" alt="Documentation" />
  </a>
</p>

<!-- SPHINX-START -->

## GitHub Information

| Projekt                              |                                     latest version |                                            forks |                                            stars |
| ------------------------------------ | -------------------------------------------------: | -----------------------------------------------: | -----------------------------------------------: |
| `mqt-ddsim`                          |                          ![gh.mqt.ddsim.release][] |                          ![gh.mqt.ddsim.forks][] |                          ![gh.mqt.ddsim.stars][] |
| `mqt-qmap`                           |                           ![gh.mqt.qmap.release][] |                           ![gh.mqt.qmap.forks][] |                           ![gh.mqt.qmap.stars][] |
| `mqt-qcec`                           |                           ![gh.mqt.qcec.release][] |                           ![gh.mqt.qcec.forks][] |                           ![gh.mqt.qcec.stars][] |
| `mqt-qecc`                           |                           ![gh.mqt.qecc.release][] |                           ![gh.mqt.qecc.forks][] |                           ![gh.mqt.qecc.stars][] |
| `mqt-bench`                          |                          ![gh.mqt.bench.release][] |                          ![gh.mqt.bench.forks][] |                          ![gh.mqt.bench.stars][] |
| `mqt-predictor`                      |                      ![gh.mqt.predictor.release][] |                      ![gh.mqt.predictor.forks][] |                      ![gh.mqt.predictor.stars][] |
| `mqt-core`                           |                           ![gh.mqt.core.release][] |                           ![gh.mqt.core.forks][] |                           ![gh.mqt.core.stars][] |
| `mqt-problemsolver`                  |                  ![gh.mqt.problemsolver.release][] |                  ![gh.mqt.problemsolver.forks][] |                  ![gh.mqt.problemsolver.stars][] |
| `mqt-syrec`                          |                          ![gh.mqt.syrec.release][] |                          ![gh.mqt.syrec.forks][] |                          ![gh.mqt.syrec.stars][] |
| `mqt-ddvis`                          |                          ![gh.mqt.ddvis.release][] |                          ![gh.mqt.ddvis.forks][] |                          ![gh.mqt.ddvis.stars][] |
| `mqt-qusat`                          |                          ![gh.mqt.qusat.release][] |                          ![gh.mqt.qusat.forks][] |                          ![gh.mqt.qusat.stars][] |
| `mqt-qudit-compilation`              |              ![gh.mqt.qudit-compilation.release][] |              ![gh.mqt.qudit-compilation.forks][] |              ![gh.mqt.qudit-compilation.stars][] |
| `mqt-dasqa`                          |                          ![gh.mqt.dasqa.release][] |                          ![gh.mqt.dasqa.forks][] |                          ![gh.mqt.dasqa.stars][] |
| `mqt-logicblocks`                    |                    ![gh.mqt.logicblocks.release][] |                    ![gh.mqt.logicblocks.forks][] |                    ![gh.mqt.logicblocks.stars][] |
| `mqt-qudit-entanglement-compilation` | ![gh.mqt.qudit-entanglement-compilation.release][] | ![gh.mqt.qudit-entanglement-compilation.forks][] | ![gh.mqt.qudit-entanglement-compilation.stars][] |
| `mqt-ionshuttler`                    |                    ![gh.mqt.ionshuttler.release][] |                    ![gh.mqt.ionshuttler.forks][] |                    ![gh.mqt.ionshuttler.stars][] |

[gh.mqt.ddsim.release]: https://img.shields.io/github/v/release/cda-tum/mqt-ddsim?label=%20&style=flat-square
[gh.mqt.ddsim.forks]: https://img.shields.io/github/forks/cda-tum/mqt-ddsim?label=%20&style=flat-square
[gh.mqt.ddsim.stars]: https://img.shields.io/github/stars/cda-tum/mqt-ddsim?label=%20&style=flat-square
[gh.mqt.qmap.release]: https://img.shields.io/github/v/release/cda-tum/mqt-qmap?label=%20&style=flat-square
[gh.mqt.qmap.forks]: https://img.shields.io/github/forks/cda-tum/mqt-qmap?label=%20&style=flat-square
[gh.mqt.qmap.stars]: https://img.shields.io/github/stars/cda-tum/mqt-qmap?label=%20&style=flat-square
[gh.mqt.qcec.release]: https://img.shields.io/github/v/release/cda-tum/mqt-qcec?label=%20&style=flat-square
[gh.mqt.qcec.forks]: https://img.shields.io/github/forks/cda-tum/mqt-qcec?label=%20&style=flat-square
[gh.mqt.qcec.stars]: https://img.shields.io/github/stars/cda-tum/mqt-qcec?label=%20&style=flat-square
[gh.mqt.core.release]: https://img.shields.io/github/v/release/cda-tum/mqt-core?label=%20&style=flat-square
[gh.mqt.core.forks]: https://img.shields.io/github/forks/cda-tum/mqt-core?label=%20&style=flat-square
[gh.mqt.core.stars]: https://img.shields.io/github/stars/cda-tum/mqt-core?label=%20&style=flat-square
[gh.mqt.bench.release]: https://img.shields.io/github/v/release/cda-tum/mqt-bench?label=%20&style=flat-square
[gh.mqt.bench.forks]: https://img.shields.io/github/forks/cda-tum/mqt-bench?label=%20&style=flat-square
[gh.mqt.bench.stars]: https://img.shields.io/github/stars/cda-tum/mqt-bench?label=%20&style=flat-square
[gh.mqt.predictor.release]: https://img.shields.io/github/v/release/cda-tum/mqt-predictor?label=%20&style=flat-square
[gh.mqt.predictor.forks]: https://img.shields.io/github/forks/cda-tum/mqt-predictor?label=%20&style=flat-square
[gh.mqt.predictor.stars]: https://img.shields.io/github/stars/cda-tum/mqt-predictor?label=%20&style=flat-square
[gh.mqt.qecc.release]: https://img.shields.io/github/v/release/cda-tum/mqt-qecc?label=%20&style=flat-square
[gh.mqt.qecc.forks]: https://img.shields.io/github/forks/cda-tum/mqt-qecc?label=%20&style=flat-square
[gh.mqt.qecc.stars]: https://img.shields.io/github/stars/cda-tum/mqt-qecc?label=%20&style=flat-square
[gh.mqt.syrec.release]: https://img.shields.io/github/v/release/cda-tum/mqt-syrec?label=%20&style=flat-square
[gh.mqt.syrec.forks]: https://img.shields.io/github/forks/cda-tum/mqt-syrec?label=%20&style=flat-square
[gh.mqt.syrec.stars]: https://img.shields.io/github/stars/cda-tum/mqt-syrec?label=%20&style=flat-square
[gh.mqt.ddvis.release]: https://img.shields.io/github/v/release/cda-tum/mqt-ddvis?label=%20&style=flat-square
[gh.mqt.ddvis.forks]: https://img.shields.io/github/forks/cda-tum/mqt-ddvis?label=%20&style=flat-square
[gh.mqt.ddvis.stars]: https://img.shields.io/github/stars/cda-tum/mqt-ddvis?label=%20&style=flat-square
[gh.mqt.problemsolver.release]: https://img.shields.io/github/v/release/cda-tum/mqt-problemsolver?label=%20&style=flat-square
[gh.mqt.problemsolver.forks]: https://img.shields.io/github/forks/cda-tum/mqt-problemsolver?label=%20&style=flat-square
[gh.mqt.problemsolver.stars]: https://img.shields.io/github/stars/cda-tum/mqt-problemsolver?label=%20&style=flat-square
[gh.mqt.qusat.release]: https://img.shields.io/github/v/release/cda-tum/mqt-qusat?label=%20&style=flat-square
[gh.mqt.qusat.forks]: https://img.shields.io/github/forks/cda-tum/mqt-qusat?label=%20&style=flat-square
[gh.mqt.qusat.stars]: https://img.shields.io/github/stars/cda-tum/mqt-qusat?label=%20&style=flat-square
[gh.mqt.logicblocks.release]: https://img.shields.io/github/v/release/cda-tum/logicblocks?label=%20&style=flat-square
[gh.mqt.logicblocks.forks]: https://img.shields.io/github/forks/cda-tum/logicblocks?label=%20&style=flat-square
[gh.mqt.logicblocks.stars]: https://img.shields.io/github/stars/cda-tum/logicblocks?label=%20&style=flat-square
[gh.mqt.ionshuttler.release]: https://img.shields.io/github/v/release/cda-tum/ion-shuttler?label=%20&style=flat-square
[gh.mqt.ionshuttler.forks]: https://img.shields.io/github/forks/cda-tum/ion-shuttler?label=%20&style=flat-square
[gh.mqt.ionshuttler.stars]: https://img.shields.io/github/stars/cda-tum/ion-shuttler?label=%20&style=flat-square
[gh.mqt.qudit-compilation.release]: https://img.shields.io/github/v/release/cda-tum/qudit-compilation?label=%20&style=flat-square
[gh.mqt.qudit-compilation.forks]: https://img.shields.io/github/forks/cda-tum/qudit-compilation?label=%20&style=flat-square
[gh.mqt.qudit-compilation.stars]: https://img.shields.io/github/stars/cda-tum/qudit-compilation?label=%20&style=flat-square
[gh.mqt.qudit-entanglement-compilation.release]: https://img.shields.io/github/v/release/cda-tum/qudit-entanglement-compilation?label=%20&style=flat-square
[gh.mqt.qudit-entanglement-compilation.forks]: https://img.shields.io/github/forks/cda-tum/qudit-entanglement-compilation?label=%20&style=flat-square
[gh.mqt.qudit-entanglement-compilation.stars]: https://img.shields.io/github/stars/cda-tum/qudit-entanglement-compilation?label=%20&style=flat-square
[gh.mqt.dasqa.release]: https://img.shields.io/github/v/release/cda-tum/mqt-dasqa?label=%20&style=flat-square
[gh.mqt.dasqa.forks]: https://img.shields.io/github/forks/cda-tum/mqt-dasqa?label=%20&style=flat-square
[gh.mqt.dasqa.stars]: https://img.shields.io/github/stars/cda-tum/mqt-dasqa?label=%20&style=flat-square

## PyPI Downloads

| Projekt                                             |                      latest version |                             weekly |                             monthly |                                                                          total |
| --------------------------------------------------- | ----------------------------------: | ---------------------------------: | ----------------------------------: | -----------------------------------------------------------------------------: |
| [`mqt.qcec`][pypi.mqt.qcec.stats]                   |          ![pypi.mqt.qcec.version][] |          ![pypi.mqt.qcec.weekly][] |          ![pypi.mqt.qcec.monthly][] |                   [![pypi.mqt.qcec.total]](https://pepy.tech/project/mqt.qcec) |
| [`mqt.qmap`][pypi.mqt.qmap.stats]                   |          ![pypi.mqt.qmap.version][] |          ![pypi.mqt.qmap.weekly][] |          ![pypi.mqt.qmap.monthly][] |                   [![pypi.mqt.qmap.total]](https://pepy.tech/project/mqt.qmap) |
| [`mqt.ddsim`][pypi.mqt.ddsim.stats]                 |         ![pypi.mqt.ddsim.version][] |         ![pypi.mqt.ddsim.weekly][] |         ![pypi.mqt.ddsim.monthly][] |                 [![pypi.mqt.ddsim.total]](https://pepy.tech/project/mqt.ddsim) |
| [`mqt.syrec`][pypi.mqt.syrec.stats]                 |         ![pypi.mqt.syrec.version][] |         ![pypi.mqt.syrec.weekly][] |         ![pypi.mqt.syrec.monthly][] |                 [![pypi.mqt.syrec.total]](https://pepy.tech/project/mqt.syrec) |
| [`mqt.qusat`][pypi.mqt.qusat.stats]                 |         ![pypi.mqt.qusat.version][] |         ![pypi.mqt.qusat.weekly][] |         ![pypi.mqt.qusat.monthly][] |                 [![pypi.mqt.qusat.total]](https://pepy.tech/project/mqt.qusat) |
| [`mqt.qecc`][pypi.mqt.qecc.stats]                   |          ![pypi.mqt.qecc.version][] |          ![pypi.mqt.qecc.weekly][] |          ![pypi.mqt.qecc.monthly][] |                   [![pypi.mqt.qecc.total]](https://pepy.tech/project/mqt.qecc) |
| [`mqt.core`][pypi.mqt.core.stats]                   |          ![pypi.mqt.core.version][] |          ![pypi.mqt.core.weekly][] |          ![pypi.mqt.core.monthly][] |                   [![pypi.mqt.core.total]](https://pepy.tech/project/mqt.core) |
| [`mqt.bench`][pypi.mqt.bench.stats]                 |         ![pypi.mqt.bench.version][] |         ![pypi.mqt.bench.weekly][] |         ![pypi.mqt.bench.monthly][] |                 [![pypi.mqt.bench.total]](https://pepy.tech/project/mqt.bench) |
| [`mqt.predictor`][pypi.mqt.predictor.stats]         |     ![pypi.mqt.predictor.version][] |     ![pypi.mqt.predictor.weekly][] |     ![pypi.mqt.predictor.monthly][] |         [![pypi.mqt.predictor.total]](https://pepy.tech/project/mqt.predictor) |
| [`mqt.problemsolver`][pypi.mqt.problemsolver.stats] | ![pypi.mqt.problemsolver.version][] | ![pypi.mqt.problemsolver.weekly][] | ![pypi.mqt.problemsolver.monthly][] | [![pypi.mqt.problemsolver.total]](https://pepy.tech/project/mqt.problemsolver) |

[pypi.mqt.ddsim.stats]: https://pypistats.org/packages/mqt-ddsim
[pypi.mqt.ddsim.version]: https://img.shields.io/pypi/v/mqt.ddsim?label=%20&style=flat-square
[pypi.mqt.ddsim.weekly]: https://img.shields.io/pypi/dw/mqt.ddsim?label=%20&style=flat-square
[pypi.mqt.ddsim.monthly]: https://img.shields.io/pypi/dm/mqt.ddsim?label=%20&style=flat-square
[pypi.mqt.ddsim.total]: https://static.pepy.tech/personalized-badge/mqt-ddsim?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.qmap.stats]: https://pypistats.org/packages/mqt-qmap
[pypi.mqt.qmap.version]: https://img.shields.io/pypi/v/mqt.qmap?label=%20&style=flat-square
[pypi.mqt.qmap.weekly]: https://img.shields.io/pypi/dw/mqt.qmap?label=%20&style=flat-square
[pypi.mqt.qmap.monthly]: https://img.shields.io/pypi/dm/mqt.qmap?label=%20&style=flat-square
[pypi.mqt.qmap.total]: https://static.pepy.tech/personalized-badge/mqt-qmap?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.qcec.stats]: https://pypistats.org/packages/mqt-qcec
[pypi.mqt.qcec.version]: https://img.shields.io/pypi/v/mqt.qcec?label=%20&style=flat-square
[pypi.mqt.qcec.weekly]: https://img.shields.io/pypi/dw/mqt.qcec?label=%20&style=flat-square
[pypi.mqt.qcec.monthly]: https://img.shields.io/pypi/dm/mqt.qcec?label=%20&style=flat-square
[pypi.mqt.qcec.total]: https://static.pepy.tech/personalized-badge/mqt-qcec?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.core.stats]: https://pypistats.org/packages/mqt-core
[pypi.mqt.core.version]: https://img.shields.io/pypi/v/mqt.core?label=%20&style=flat-square
[pypi.mqt.core.weekly]: https://img.shields.io/pypi/dw/mqt.core?label=%20&style=flat-square
[pypi.mqt.core.monthly]: https://img.shields.io/pypi/dm/mqt.core?label=%20&style=flat-square
[pypi.mqt.core.total]: https://static.pepy.tech/personalized-badge/mqt-core?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.qecc.stats]: https://pypistats.org/packages/mqt-qecc
[pypi.mqt.qecc.version]: https://img.shields.io/pypi/v/mqt.qecc?label=%20&style=flat-square
[pypi.mqt.qecc.weekly]: https://img.shields.io/pypi/dw/mqt.qecc?label=%20&style=flat-square
[pypi.mqt.qecc.monthly]: https://img.shields.io/pypi/dm/mqt.qecc?label=%20&style=flat-square
[pypi.mqt.qecc.total]: https://static.pepy.tech/personalized-badge/mqt-qecc?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.bench.stats]: https://pypistats.org/packages/mqt-bench
[pypi.mqt.bench.version]: https://img.shields.io/pypi/v/mqt.bench?label=%20&style=flat-square
[pypi.mqt.bench.weekly]: https://img.shields.io/pypi/dw/mqt.bench?label=%20&style=flat-square
[pypi.mqt.bench.monthly]: https://img.shields.io/pypi/dm/mqt.bench?label=%20&style=flat-square
[pypi.mqt.bench.total]: https://static.pepy.tech/personalized-badge/mqt-bench?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.predictor.stats]: https://pypistats.org/packages/mqt-predictor
[pypi.mqt.predictor.version]: https://img.shields.io/pypi/v/mqt.predictor?label=%20&style=flat-square
[pypi.mqt.predictor.weekly]: https://img.shields.io/pypi/dw/mqt.predictor?label=%20&style=flat-square
[pypi.mqt.predictor.monthly]: https://img.shields.io/pypi/dm/mqt.predictor?label=%20&style=flat-square
[pypi.mqt.predictor.total]: https://static.pepy.tech/personalized-badge/mqt-predictor?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.problemsolver.stats]: https://pypistats.org/packages/mqt-problemsolver
[pypi.mqt.problemsolver.version]: https://img.shields.io/pypi/v/mqt.problemsolver?label=%20&style=flat-square
[pypi.mqt.problemsolver.weekly]: https://img.shields.io/pypi/dw/mqt.problemsolver?label=%20&style=flat-square
[pypi.mqt.problemsolver.monthly]: https://img.shields.io/pypi/dm/mqt.problemsolver?label=%20&style=flat-square
[pypi.mqt.problemsolver.total]: https://static.pepy.tech/personalized-badge/mqt-problemsolver?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.syrec.stats]: https://pypistats.org/packages/mqt-syrec
[pypi.mqt.syrec.version]: https://img.shields.io/pypi/v/mqt.syrec?label=%20&style=flat-square
[pypi.mqt.syrec.weekly]: https://img.shields.io/pypi/dw/mqt.syrec?label=%20&style=flat-square
[pypi.mqt.syrec.monthly]: https://img.shields.io/pypi/dm/mqt.syrec?label=%20&style=flat-square
[pypi.mqt.syrec.total]: https://static.pepy.tech/personalized-badge/mqt-syrec?period=total&units=international_system&left_color=orange&right_color=orange&left_text=
[pypi.mqt.qusat.stats]: https://pypistats.org/packages/mqt-qusat
[pypi.mqt.qusat.version]: https://img.shields.io/pypi/v/mqt.qusat?label=%20&style=flat-square
[pypi.mqt.qusat.weekly]: https://img.shields.io/pypi/dw/mqt.qusat?label=%20&style=flat-square
[pypi.mqt.qusat.monthly]: https://img.shields.io/pypi/dm/mqt.qusat?label=%20&style=flat-square
[pypi.mqt.qusat.total]: https://static.pepy.tech/personalized-badge/mqt-qusat?period=total&units=international_system&left_color=orange&right_color=orange&left_text=

<!-- SPHINX-END -->

---

## Acknowledgements

The Munich Quantum Toolkit has been supported by the European
Research Council (ERC) under the European Union's Horizon 2020 research and innovation program (grant agreement
No. 101001318), the Bavarian State Ministry for Science and Arts through the Distinguished Professorship Program, as well as the
Munich Quantum Valley, which is supported by the Bavarian state government with funds from the Hightech Agenda Bayern Plus.

<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cda-tum/mqt-core/main/docs/_static/tum_dark.svg" width="28%">
<img src="https://raw.githubusercontent.com/cda-tum/mqt-core/main/docs/_static/tum_light.svg" width="28%">
</picture>
<picture>
<img src="https://raw.githubusercontent.com/cda-tum/mqt-core/main/docs/_static/logo-bavaria.svg" width="16%">
</picture>
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cda-tum/mqt-core/main/docs/_static/erc_dark.svg" width="24%">
<img src="https://raw.githubusercontent.com/cda-tum/mqt-core/main/docs/_static/erc_light.svg" width="24%">
</picture>
<picture>
<img src="https://raw.githubusercontent.com/cda-tum/mqt-core/main/docs/_static/logo-mqv.svg" width="28%">
</picture>
</p>
