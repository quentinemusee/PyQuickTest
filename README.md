# PyQuickTest
PyQuickTest is an experimental python testing framework designed to  deliver an easy-and-quick-to-start python testing mechanism.


# Getting started
PyQuickTest test kit is divided into few categories:


## Decorators
### @is_test
*Transform the decorated function into a test function for the framework.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" is not a test.*\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" is a test.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**

### @qpt_group
*Categorize the decorated function as belonging to the given groups and subgroups. Groups and subgroups should be given as arguments.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" has no test group.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**\
    ~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" belong to the test group "Group".*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_group("Group")**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**\
    ~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" belong to the test group "Group" and subgroup "Subgroup".*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_group("Group", "Subgroup")**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**

### @qpt_execnbr
*Order the decorated test function to be run a given number of times.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" is run once.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" is run 100 times.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_execnbr(100)**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function():**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**

### @qpt_parametrize
*Use the given parameters to the test function.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" will fail once tested because no arg is provided.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" will will be run with arg = 8.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_parametrize(8)**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*"my_function" will will be run with arg1 = 8, arg2 = 'a' and arg3 = [45.19].*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**@qpt_parametrize(8, 'a', [45.19])**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg1, arg2, arg3):**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**


## Assertion functions                                            
### ok
*Validate the current test.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*The test "my_function" will pass.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**

### ko
*Unvalidate the current test with an optional error message.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*The test "my_function" will fail.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ko("This test failed!")**

### check
*Unvalidate the current test if the given boolean is False. An optional error message can be provided. If the given boolean is True, do nothing.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*The test "my_function" will fail if the generated number 'a' is lower than 10.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**a = gen_int()**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**check(a > 10, "a isn't greater than 10")**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ok()**

### ensure
*Validate or unvalidate the current test depending on the given boolean. An optional error message can be provided.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*The test "my_function" will pass if the generated number 'a' if greater than 10, and fail otherwise.*\
&nbsp;&nbsp;&nbsp;&nbsp;**@is_test()**\
&nbsp;&nbsp;&nbsp;&nbsp;**def my_function(arg):**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**a = gen_int()**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ensure(a > 10, "a isn't greater than 10")**


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
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test "my_function".*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_one(my_function)**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test "my_function" with a printed prefix "==>" before the test result output.*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_one(**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**my_function,**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**prefix="==>"**\
&nbsp;&nbsp;&nbsp;&nbsp;**)**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test "my_function" with an indentation of 4 spaces and a printed prefix "==>" before the test result output.*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_one(**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**my_function,**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**prefix="==>"**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**indent=4**\
&nbsp;&nbsp;&nbsp;&nbsp;**)**

### test_group                                                 
*Run a group of test functions. If you want to run a subgroup, pass every group and subgroup as a parameter. If no context is provided, it will be obtained by importing the caller file. If a filename is provided, the context will be retrieved from this file.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test functions from group "G".*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_group("G")**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test functions from group "G" and subgroup "Subgroup".*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_group(**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**"G",**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**"Subgroup"**\
&nbsp;&nbsp;&nbsp;&nbsp;**)**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test functions from group "G", subgroup "SG" and sub-subgroup "SSG".*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_group(**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**"G",**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**"SG",**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**"SSG",**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**filename="tests.py"**\
&nbsp;&nbsp;&nbsp;&nbsp;**)**

### test_all                                                     
*Run every test functions. If no context is provided, it will be obtained by importing the caller file. If a filename is provided, the context will be retrieved from this file.*\
**example:**\
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test functions from caller file context.*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_all()**\
&nbsp;&nbsp;&nbsp;&nbsp;~~~~~~\
&nbsp;&nbsp;&nbsp;&nbsp;*Run the test functions from file "test.py".*\
&nbsp;&nbsp;&nbsp;&nbsp;**test_all(**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**filename="tests.py"**\
&nbsp;&nbsp;&nbsp;&nbsp;**)**


# Installation
TBA