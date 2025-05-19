# Unit testing and test-driven development in Python

## Walkthrough 

This repo supports a presentation and workshop. The general flow of topics is as follows:

1. Testing vs. checking 
1. Test automation pyramid 
1. Writing unit tests for existing code 
1. Guiding new development and modifications from unit tests
1. Unit test suite as a safety net for refactoring
1. Mocking dependencies 
1. Property-based testing 
1. Mutation testing 
1. Exploratory testing 

## Running the examples 

Use a virtual environment to avoid conflicts with packages installed at the system level.

```shell
cd [project root]
source .venv/bin/activate 

[do stuff]

deactivate
```

### Run the unit tests 

```shell 
pytest tests
```

### Run the calculator with the console front-end 

```shell 
python3 src/rpn_console.py
```

### Run the calculator with the GUI front-end 

Might need to do this first:

```shell 
python3 -m pip install PyQt6
``` 

Run the app:


```shell 
python3 src/rpn_gui.py 
``` 

### Run the property-based tests 

```shell
python3 -m pip install hypothesis
``` 

Sample property-based test:

```shell 
pytest property_tests
```

### Run the mutation tests 

```shell
python3 -m pip install mutmut 
``` 

Run mutation tests

```shell
mutmut run

mutmut browse 

q
``` 




## Some resources

## Python packages used in this workshop 

- [pytest - unit testing library](https://docs.pytest.org/en/stable/)
- [hypothesis - property-based testing](https://hypothesis.readthedocs.io/en/latest/)
- [mutmut - Python mutation tester](https://mutmut.readthedocs.io/en/latest/index.html)
