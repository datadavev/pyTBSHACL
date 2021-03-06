# pyTBSHACL
Python wrapper for TopQuadrant's TopBraid SHACL validator.

[PySHACL](https://github.com/RDFLib/pySHACL) for RDFLib 
[does not currently implement](https://github.com/RDFLib/pySHACL/blob/master/FEATURES.md) 
some of the [advanced SHACL functionality](https://www.w3.org/TR/shacl-af/) 
which is available with [TopBraid's command line validator](https://github.com/TopQuadrant/shacl). 
`pyTBSHACL` implements a python wrapper for the TopBraid validator tool 
to help simplify integration with python projects 
needing that functionality. It is anticipated that this module will 
become redundant as adavanced capabilities are progressively added to PySHACL.

## Status

Version 0.0.1 (2019-08-21):

Initial complete implementation. Shape files must be in turtle, data files
may be in any RDF format supported by RDFLib. Output in turtle, plain text,
or json. Tested on OS X only.


## Installation

1\. Download and install the TopBraid SHACL validator, following guidance at:
   
   https://github.com/TopQuadrant/shacl
  
  Optionally build the validator from source, see "Building the Validator 
  from Source" below.
  
2\. Set the `SHACLROOT` environment variable to the absolute path to the
`bin` folder of the TopBraid SHACL validator distribution.

3\. `pip install -U pyTBSHACL` or clone this repo, cd to the folder, 
then run: `pip install -e .`

## Example

Following are run from the `examples` folder.

Valid data:

```
$ shacl -d data_00a.ttl -s shape_00.ttl
@prefix ex:    <http://example.org/> .
@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

[ a            sh:ValidationReport ;
  sh:conforms  true
] .
```

Invalid data:

```
$ shacl -d data_00b.ttl -s shape_00.ttl
@prefix ex:    <http://example.org/> .
@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

[ a            sh:ValidationReport ;
  sh:conforms  false ;
  sh:result    [ a                             sh:ValidationResult ;
                 sh:focusNode                  ex:bob ;
                 sh:resultMessage              "Does not have value ex:Mathematics" ;
                 sh:resultPath                 ex:field ;
                 sh:resultSeverity             sh:Violation ;
                 sh:sourceConstraintComponent  sh:HasValueConstraintComponent ;
                 sh:sourceShape                []
               ]
] .
```

Invalid data with text output:

```
$ shacl -d data_00b.ttl -s shape_00.ttl -of text
Validation Report
Conforms: False
Results (1):
Results for focus node http://example.org/bob:
  Path: http://example.org/field
  Severity: Violation
  Constraint violation in HasValueConstraintComponent
  Message: Does not have value ex:Mathematics
  Source shape: ub2bL15C48
```



Valid Dataset with encoding in json-ld:

```
$ shacl -d data_01a.json -df json-ld  -s shape_01.ttl
@prefix :      <http://schema.org/> .
@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xml:   <http://www.w3.org/XML/1998/namespace> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

[ a            sh:ValidationReport ;
  sh:conforms  true
] .
```

Invalid Dataset encoding:

```
$ shacl -d data_01b.ttl -s shape_01.ttl
@prefix schema: <http://schema.org/> .
@prefix ex:    <http://example.org/> .
@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

[ a            sh:ValidationReport ;
  sh:conforms  false ;
  sh:result    [ a                             sh:ValidationResult ;
                 sh:focusNode                  ex:dataset2_encoding ;
                 sh:resultMessage              "A schema:contentUrl is required for the encoding property of a Dataset" ;
                 sh:resultPath                 schema:contentUrl ;
                 sh:resultSeverity             sh:Violation ;
                 sh:sourceConstraintComponent  sh:MinCountConstraintComponent ;
                 sh:sourceShape                <http://ns.dataone.org/schema/2019/08/SO/Dataset#contentUrlConstraint0>
               ] ;
  sh:result    [ a                             sh:ValidationResult ;
                 sh:focusNode                  ex:dataset2_encoding ;
                 sh:resultMessage              "Property needs to have at least 1 values, but found 0" ;
                 sh:resultPath                 schema:encodingFormat ;
                 sh:resultSeverity             sh:Violation ;
                 sh:sourceConstraintComponent  sh:MinCountConstraintComponent ;
                 sh:sourceShape                <http://ns.dataone.org/schema/2019/08/SO/Dataset#encodingFormatConstraint0>
               ] ;
  sh:result    [ a                             sh:ValidationResult ;
                 sh:focusNode                  []  ;
                 sh:resultMessage              "Property needs to have at least 1 values, but found 0" ;
                 sh:resultPath                 schema:encodingFormat ;
                 sh:resultSeverity             sh:Violation ;
                 sh:sourceConstraintComponent  sh:MinCountConstraintComponent ;
                 sh:sourceShape                <http://ns.dataone.org/schema/2019/08/SO/Dataset#encodingFormatConstraint0>
               ]
] .
```


## Building the Validator from Source

The most recent version of the TopBraid shacl validator can be built 
from source as follows:

1. Clone the repository:

```
git clone https://github.com/TopQuadrant/shacl
```

2. Build the package:

```
cd shacl
mvn clean package 
```

3. Deploy the built package. The package is a .zip file in the `target` 
folder named like ``. Unzip that file to the desired installation
location, e.g.:

```
cd ~/bin
unzip ~/git/shacl/target/shacl-1.x.y-SNAPSHOT-bin.zip
export SHACLROOT="~/git/shacl/target/shacl-1.x.y-SNAPSHOT/bin"
```