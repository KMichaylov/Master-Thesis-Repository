# Author & Supervisor
- **Author**: Kristiyan Michaylov
- **Supervisor**: Dr.-Ing. Jacob Krüger

# Master-Thesis-Repository
This repository contains the source code and datasets used for the experiments conducted as part of my Master's thesis, titled **Tracing Evolutionary Changes of APIs**.

The main objective of this research is to **analyse the reasons behind API changes and evaluate their impact on both the functionalities and the architectural design of the APIs.**

## Table of Contents

- [Research Questions](#research-questions)
- [Methodology](#methodology)
- [Project Structure](#project-structure-)
- [Setup and Installation RQ1](#setup-and-installation-rq1)
- [Setup and Installation RQ2](#setup-and-installation-rq2)
- [Link to thesis](#link-to-thesis)

## Research Questions
- RQ1 : To what extent can an automated machine learning technique analyse
and categorise the causes of changes in Java APIs?
- RQ2 : How do changes impact the architecture and functionalities of APIs?
- RQ2.1 : Are changes impacting the architecture and functionality represented
in the release log?
- RQ2.2 : How does the architecture of an API alter during evolution?
## Methodology
We studied the evolution of Java APIs (e.g., JUnit, Lombok, Log4J, Apache Commons IO) by analyzing release log messages and source code from the Maven Repository.
Machine learning models were used to classify change reasons, while empirical methods examined how functionality and architecture evolve over time.
This included software metrics evaluation, class diagram alternation throughout evolution, package structure analysis and mapping between release log messages and architecture and functionality.

## Project structure 
The structure of the current repository is organised as follows:
Master-Thesis-Repository/ \
├── notebooks/             &rarr; Jupyter notebooks (main experiments for RQ1) \
├── resources/             &rarr; Images, tables and other visuals \
├── rq2_resources          &rarr; Files related to experiments for RQ2 \
├──── arcana_json_files &rarr; JSON files generated by Arcana \
├──── class_diagrams    &rarr; Class diagrams from the JetBrains diagramming tool \
├── requirements.txt       &rarr; pip dependencies \
├── LICENSE                &rarr; Project license \
└── README.md 

## Setup and Installation RQ1
Here is an example for building and environment setup

1. Install virtualenv (if not already installed)
`pip install virtualenv`

2. Create a virtual environment
`python -m venv venv`

3. Activate the virtual environment

    * On macOS/Linux:
    `source venv/bin/activate`
    * On Windows:
    `venv\Scripts\activate`

4. Install and Upgrade pip (if not already done)
`pip install --upgrade pip`

5. Install project dependencies
`pip install -r requirements.txt`

6. Install Jupyter (if not already included)
`pip install notebook`

7. Run Jupyter Notebook
`jupyter notebook`

## Setup and Installation RQ2
To run the experiments related to RQ2, please refer to the following GitHub repositories:
* [arcana](https://github.com/rsatrioadi/arcana)
* [javapers](https://github.com/rsatrioadi/javapers)
* [bubbleTea 2.0](https://github.com/rsatrioadi/bubbletea-v2)

## Link to thesis
TODO, once available online
