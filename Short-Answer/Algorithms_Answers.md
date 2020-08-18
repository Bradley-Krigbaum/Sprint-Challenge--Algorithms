#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N)
    
    since it is only one loop I think its O(N). No matter what N is, the outcome will be linear.


b) O(N^2)

    since there are nested loops the time completity will increase. the value has to be interperted in both the inner and outer loops.


c) O( Log N )

    since this is a recursive function I would say this is logarithmic time complexity. 

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

```
=================================================================================================
```

get the number of floors in the building:

    index of highest floor = length( building - 1)

    index of lowest floor = 1

divide the building into two parts:

    find the middle of the building 
        middle of building = highest floor // 2

    high floors = middle of building and up

    low floors = middle of building and down

make a drop egg function:
    from the index of the floor your on:
        drop egg
            if egg breaks return index of floor
        

determine how high the eggs can break at:

    from lowest floor drop an egg off the building
        if egg breaks the highest floor an egg can fall is 1
    from middle floor drop an egg off the building
        if egg does not break move to floor two, floor three,... until the egg breaks
            return the floor the egg broke from
    from highest floor drop an egg off the building
        if egg does not break move to next floor... until the egg breaks
            return the floor the egg broke from

this should output a time complexity of O( N Log N) because you rerun the loops until the egg breaks. First N is the number of times you run the code, Log N is the outcome of using recursion.
