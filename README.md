# GradeX

Compile and grade large number of student submissions(in multiple languages) in a matter of seconds without the hassle of writing unit tests.

## Install
The project needs NumPy to work correctly.

If you use ```pip```, you can install it with:

```pip install numpy```

Or, if you use ```conda```, you can install it with:

```conda install numpy```

To install the project repo, run the following git command:

```git clone https://github.com/aditya-mahendru/friday.git```

## Usage

This project is a console application, and can be executed/compiled using ```python3```.

For basic execution, use:

```python3 main.py -i path/to/zip/containing/all/c/files -ti path/to/test/case/file```

The zip file should contain .c files in the format:

```Problemnumber_rollnumber.c```

eg: ```P1_1234.c```

### Test Case Writing

The project accepts a ```.json``` file containing:

- Test Input
- Expected Output
- Weightage

for each test case.

The ```.json``` is expected in the following format:

```
{
  "test_cases":
  [
    {
      "test_case": "Sample input 1(formatted)",
      "output": "Expected Output 1(formatted)",
      "marks": 10(Max Marks if test case passes)
    },
    {
      "test_case": "Sample input 2(formatted)",
      "output": "Expected Output 2(formatted)",
      "marks": 20(Max Marks if test case passes)
    }
  ]
}
```
### Mandatory Flags
|Flag|Use|
|---|---|
|```-i```|Specify path of zipfile containing C programs|
|```-ti```|Path to ```.json``` containing test I/O and Weigtage|


### Optional Flags

|Flag|Use|Default|
|---|---|---|
|```-o```|Specify output path| ../testResults.csv|
|```-r```|Record runtime and assign relative score|-|
|```-m```|Max value of bonus score|10|
|```-to```|Change timeout|60|
|```-cl```|Use Clang instead of GCC|-|
|```-pn```|Specify Problem Number|-|
|```-ww```|Remove all whitespaces from I/O|-|
|```-abs```|Char by char comparison b/w I/O|-|
