# pyTBSHACL
Python wrapper for TopBraid's SHACL validator.

PySHACL for RDFLib dooes not currently implement soome of the [advanced SHACL functionality](https://www.w3.org/TR/shacl-af/) 
which is available with [TopBraid's command line validator](https://github.com/TopQuadrant/shacl). `pyTBSHACL` 
implements a python wrapper for the TopBraid validator tool to help simplify integration with python projects 
needing that functionality. It is anticipated that this module will become redundant as adavanced capabilities 
are progeressively added to PySHACL.

## Status

Currently (2019-08-11) an initial draft implementation.
