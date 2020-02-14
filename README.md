## Brioche Factory TDD :pizza:

## Unit test

## Integration test
Test code from end to end. 

## TDD - Test driven dovelopment

It is what is say is.
you first write a test. 

then you code.

Code the minimum amount to pass. 

# # Basics of a test

Know inputs, and know outputs.
All you do is an assertion.

Then you have testing frameworks that helps you do this.

## Our factory know inputs and outputs

make a function that takes in 2 arguments. it should give dough with inputes egg, flour and eggs.

### make_bread
inputs:
- water
- flour
- eggs

outputs:
- dough


### bake 
input: 
dough

outputs:
brioche

##simple integration test - give better view on whats not working
### run factory
as a user, i want to be able to run ba factory function. Give it flour, water 
and eggs and recieve brioche. 
;)