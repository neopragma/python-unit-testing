# Unit testing and test-driven development in Python

## Walkthrough 

This repo supports a presentation and workshop. Some notes about running the examples are provided below. This is not complete documentation for self-guided learning. The live session has the following general agenda:

1. (Talk) Testing vs. checking 
1. (Talk) Test automation pyramid 
1. (Code) Writing unit tests for existing code 
1. (Code) Guiding new development and modifications from unit tests
1. (Code) Unit test suite as a safety net for refactoring
1. (Code) Mocking dependencies, refactoring 
1. (Code) Property-based testing 
1. (Code) Mutation testing 
1. (Talk) Exploratory testing 

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

## Mocking dependencies, refactoring

The sample code calls a public API and uses the result to insert data into a local sqlite3 database. 

### Setup the database

If necessary, create the database. 

```shell
> cd [project root]/foodie
> sqlite3 data/food4thot 
sqlite> .databases 
``` 

Expect to see food4thot as the current (main) database, with read/write access enabled, like this:

```shell 
main: [local-absolute-path-to-project-root]/foodie/data/food4thot r/w
```

Enter .quit to exit the REPL. 

```shell 
sqlite> .quit 
``` 

To initialize the test database:

```shell 
cd [project-root]/foodie
sqlite3 food4thot < data/init_db.sql 
``` 

### Run the starter code for foodie 

```shell 
cd [project-root]/foodie/starter 

python3 food_run.py '0 44300 00012 4'
```

If the UPC code is no longer valid, look for another one here: https://www.upcitemdb.com/upc/44300000124. The sample code doesn't depend on any particular food item, provided the description matches the format used by the API, https://world.openfoodfacts.org/api/v0/product/.

Examine ```food_run.py```, ```foodie.py```, and ```food_storage.py``` and think about how you might isolate different parts of the code for automated checking ("testing"). You will have to do some refactoring to enable this. A sample solution is provided under ```foodie/solution```. 

### Create a "golden master" for Approval Testing

If you want to use the Approval Testing approach when refactoring the 'foodie' code, you can run this script:

```shell 
cd [project-root/foodie/starter/]
/run.sh > golden_master.txt 
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

- [ast - abstract syntax trees](https://docs.python.org/3/library/ast.html)
- [hypothesis - property-based testing](https://hypothesis.readthedocs.io/en/latest/)
- [mutmut - Python mutation tester](https://mutmut.readthedocs.io/en/latest/index.html)
- [pytest - unit testing library](https://docs.pytest.org/en/stable/)
- [requests - HTTP request and response](https://pypi.org/project/requests/)
- [sqlite3 - database](https://docs.python.org/3/library/sqlite3.html)