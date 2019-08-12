# pyTBSHACL
Python wrapper for TopBraid's SHACL validator.

PySHACL for RDFLib dooes not currently implement soome of the [advanced SHACL functionality](https://www.w3.org/TR/shacl-af/) 
which is available with [TopBraid's command line validator](https://github.com/TopQuadrant/shacl). `pyTBSHACL` 
implements a python wrapper for the TopBraid validator tool to help simplify integration with python projects 
needing that functionality. It is anticipated that this module will become redundant as adavanced capabilities 
are progeressively added to PySHACL.

## Status

Currently (2019-08-11) an initial draft implementation, tested on OS X only.


## Installation

1. Download and install the TopBraid SHACL validator, following guidance at:

  https://github.com/TopQuadrant/shacl
  
2. Set the `SHACLROOT` environment variable to the absolute path to the
`bin` folder of the TopBraid SHACL validator distribution.

3. Clone this repo, cd to the folder, then run: `pip install -e .`

## Example

Following are run from the `examples` folder.

Valid data:

```
$ shacl -d data_00a.ttl -s shape_00.ttl
stdout=
@prefix ex:    <http://example.org/> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

[ a       <http://www.w3.org/ns/shacl#ValidationReport> ;
  <http://www.w3.org/ns/shacl#conforms>
          true
] .

stderr=
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
```

Invalid data:

```
$ shacl -d data_00b.ttl -s shape_00.ttl
stdout=
@prefix ex:    <http://example.org/> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

[ a       <http://www.w3.org/ns/shacl#ValidationReport> ;
  <http://www.w3.org/ns/shacl#conforms>
          false ;
  <http://www.w3.org/ns/shacl#result>
          [ a       <http://www.w3.org/ns/shacl#ValidationResult> ;
            <http://www.w3.org/ns/shacl#focusNode>
                    ex:bob ;
            <http://www.w3.org/ns/shacl#resultMessage>
                    "Missing expected value ex:Mathematics" ;
            <http://www.w3.org/ns/shacl#resultPath>
                    ex:field ;
            <http://www.w3.org/ns/shacl#resultSeverity>
                    <http://www.w3.org/ns/shacl#Violation> ;
            <http://www.w3.org/ns/shacl#sourceConstraintComponent>
                    <http://www.w3.org/ns/shacl#HasValueConstraintComponent> ;
            <http://www.w3.org/ns/shacl#sourceShape>
                    []
          ]
] .

stderr=
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.

```
