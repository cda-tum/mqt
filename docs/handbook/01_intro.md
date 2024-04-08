# Introduction

Quantum computing has the potential to revolutionize many fields in the 21st century. Over the past decade, numerous quantum computers from multiple providers based on different qubit technologies have been made publicly available.
However, the best hardware is only as good as the software available to realize corresponding applications on it---a lesson learned from the past decades of research on designing and developing classical circuits and systems.
Thanks to the software tools and methods for _Electronic Design Automation (EDA)_, we can create classical systems with a staggering amount of transistors and complex functionalities that we often take for granted.
These methods allow designers to efficiently and automatically handle the intricacies of such systems and optimize their performance.
Compared to that, most existing software solutions for quantum computing are based on manual approaches.
This is not only susceptible to errors, inefficiency, and inconsistency but also leaves decades of research on design automation methods underutilized.

The _Munich Quantum Toolkit (MQT)_, which is developed by the [Chair for Design Automation](https://www.cda.cit.tum.de/) at the [Technical University of Munich](https://www.tum.de/), aims to leverage this latent potential by providing a collection of state-of-the-art design automation methods and software for quantum computing.
Our overarching objective is to provide solutions for design tasks across the entire quantum software stack.
This entails high-level support for end users in realizing their _Applications_ as well as efficient methods for the _Classical Simulation_, _Compilation_, and _Verification_ of quantum circuits.
Reaching towards the hardware level, we also consider tools for _Quantum Error Correction_ and _Physical Design_.
In all these tools, we try to utilize _Data Structures and Core Methods_ facilitating the efficient handling of quantum computations.
The proposed solutions demonstrate significant improvements in efficiency, scalability, and reliability and illustrate the immense benefits of leveraging knowledge and expertise in classical circuit and system design rather than starting from scratch.
All tools developed as part of the toolkit are made available as open-source packages on [github.com/cda-tum](https://github.com/cda-tum/).

In the following, we briefly summarize the main tools (covering classical simulation, compilation, and verification of quantum circuits as well as benchmarking). We particularly focus on how to use the tools, but additionally provide references/links that offer detailed descriptions of the underlying methods as well as summaries of corresponding case studies and evaluations demonstrating the performance.
