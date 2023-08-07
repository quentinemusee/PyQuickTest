# PyQuickTest
PyQuickTest is an experimental python testing framework designed to  deliver an easy-and-quick-to-start python testing mechanism.


# Getting started
PyQuickTest test kit is divided into few categories:


## Decorators
### @is_test
*Transform the decorated function into a test function for the framework.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():** *is not*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *a test*\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~~~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *is*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**  *a*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *test*

### @qpt_group
*Categorize the decorated function as belonging to the given groups and subgroups. Groups and subgroups should be given as arguments.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *has*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *no*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *test group*\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  *belong*\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_group("Group")** *to the*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  *group*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *"Group"*\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  *belong to the*\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_group("Group", "Subgroup")** &nbsp; *group "Group"*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *and the subgroup*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *"Subgroup"*

### @qpt_execnbr
*Order the decorated test function to be run a given number of times.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *runs*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():** &nbsp;&nbsp;&nbsp;&nbsp; *once*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*my_function*\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *runs*\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_execnbr(100)** &nbsp;&nbsp; *100*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():** &nbsp;&nbsp;&nbsp;&nbsp; *times*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *my_function*

### @qpt_parametrize
*Use the given parameters to the test function.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *will fail*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):** &nbsp;&nbsp;&nbsp;&nbsp; *because no*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *"arg" provided*\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *test*\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_parametrize(8)** *with*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):** *arg*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *= 8*\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *test with*\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_parametrize(8, 'a', [45.19])** &nbsp; *arg1 = 8*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg1, arg2, arg3):** *arg2 = 'a'*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *arg3 = [45.19]*


## Assertion functions                                            
### ok
*Validate the current test.*\
**example:**\
    **@is_test()**            |  *This*\
    **def my_function(arg):** |  *test*\
        **ok()**              | *passes*

### ko
*Unvalidate the current test with an optional error message.*\
**example:**\
    **@is_test()**                  | *This*\
    **def my_function(arg):**       | *test*\
        **ko("This test failed!")** | *fail*

### check
*Unvalidate the current test if the given boolean is False. An optional error message can be provided. If the given boolean is True, do nothing.*\
**example:**\
    **@is_test()**                                  |      *if the*\
    **def my_function(arg):**                       | *generated number*\
        **a = gen_int()**                           | *a is lower than*\
        **check(a > 0, "a isn't greater than 10")** |   *10, the tests*\
        **ok()**                                    |     *will fail.*

### ensure
*Validate or unvalidate the current test depending on the given boolean. An optional error message can be provided.*\
**example:**\
    **@is_test()**                                   |  *if the generated*\
    **def my_function(arg):**                        | *number a is lower*\
        **a = gen_int()**                            | *than 10, the tests*\
        **ensure(a > 0, "a isn't greater than 10")** |      *will fail*


## Generator functions                                               
### gen_none
*Generate None.*
### gen_bool
*Generate a random boolean.*
### gen_int
*Generate a random integer. Min and max can be provided.*
### gen_signed_int
*Generate a random signed integer. Min / max can be given.*
### gen_float
*Generate a random float.*
### gen_signed_float
*Generate a random signed float. Min and max can be given.*
### gen_ascii_lower_char
*Generate a random ascii lower char.*
### gen_ascii_upper_char
*Generate a random ascii upper char.*
### gen_ascii_char
*Generate a random ascii char.*
### gen_ascii_lower_string
*Generate a random ascii lower string.*
### gen_ascii_upper_string
*Generate a random ascii upper string.*
### gen_ascii_string
*Generate a random ascii string.*
### gen_callable
*Generate a random callable. The number of arguments can be specified with nbr_args, as well as the generator function for the returned value with gen_return. If raised_exception = True, then the callable will raise an exception.*
### gen_generator
*Generate a random iterator. The iterator length can be provided, as well as the elements generator function with the gen_element argument.*
### gen_list
*Generate a random list. The list length can be provided, as well as the elements generator function with the the gen_element argument.*
### gen_dict
*Generate a random dict. The dict length can be provided, as well as the keys generator function with the the gen_keys argument, and the element generator function with the gen_element argument.*
### gen_random_value
*Generate a random value from any single value generator decorated with the "is_gen_value" flag attribute.*
### gen_random_iterable
*Generate a random iterable from any iterable generator decorated with the "is_gen_iterable" flag attribute.*
### gen_random
*Generate a random data from any generator decorated with the "is_gen" flag attribute.*


## Testing functions
### test_one
*Run a single test function. A few optional arguments can be provided, but if this function is directly used alone, only passing the test function as a parameter is certainly enough.*\
**example:**\
    **test_one(my_function)** | *This will run the test function my_function.*\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    **test_one(**        |     *This will run the test*\
        **my_function,** |  *function my_function with a*\
        **prefix="==>"** |      *printed prefix "==>"*\
    **)**                | *before the test result output.*\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    **test_one(**        |     *This will run the test*\
        **my_function,** |  *function my_function with an*\
        **prefix="==>"** |  *indentation of 4 spaced and a*\
        **indent=4**     |      *printed prefix "==>"*\
    **)**                | *before the test result output.*

### test_group                                                 
*Run a group of test functions. If you want to run a subgroup, pass every group and subgroup as a parameter. If no context is provided, it will be obtained by importing the caller file. If a filename is provided, the context will be retrieved from this file.*\
**example:**\
    **test_group("G")** | *This will run very test function from group "G".*\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    **test_group(**    |   *This will run every*\
        **"G",**       |    *test function from*\
        **"Subgroup"** |  *the group "G" and the*\
    **)**              |   *subgroup "Subgroup".*\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    **test_group(**             |  *This will run every*\
        **"G",**                |   *test function from*\
        **"SG",**               |   *the group "G", the*\
        **"SSG",**              | *subgroup "SG" and the*\
        **filename="tests.py"** | *subgroup "SGG" from the*\
    **)**                       |     *"test.py" file.*

### test_all                                                     
*Run every test functions. If no context is provided, it will be obtained by importing the caller file. If a filename is provided, the context will be retrieved from this file.*\
**example:**\
    **test_all()** | *This will every test function from caller file context.*\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    **test_all(**               | *This will run every*\
        **filename="tests.py"** | *test function from*\
    **)**                       | *the "test.py" file.*


# Installation
TBA