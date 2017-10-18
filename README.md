# Elephant Carpaccio Exercise

## References

http://alistair.cockburn.us/Elephant+Carpaccio+exercise

## Instructions

1. Break into teams of 2-3 people, one workstation per team.
1. Preparation - Each team writes down on paper the 10-20 demo-able user stories
   ("slices") they will develop and possibly demo. Each should be doable in 3-8
   minutes. No slice is just mockup of UI, creation of a data table or data
   structure. All demos show real input & output (not test harness).
1. Discussion - Instructor/facilitator leads discussion of the slices, what is
   and isn't acceptable, solicits ways to slice finer.
1. Development - A fixed time-box of 40 minutes, five 8-minute development
   sprints, clock does not stop. At the end of each sprint, each team shows its
   product to another team.
1. Debrief

## Product

Accept 3 inputs from the user:
* How many items
* Price per item
* 2-letter state code

Output the total price. Give a discount based on the total price, add state tax
based on the state and the discounted price.

    | Order value | Discount rates |
    |-------------|----------------|
    | $1,000      |  3%            |
    | $5,000      |  5%            |
    | $7,000      |  7%            |
    | $10,000     | 10%            |
    | $50,000     | 15%            |

    | State | Tax rate |
    |-------|----------|
    | UT    | 6.85     |
    | NV    | 8.00     |
    | TX    | 6.25     |
    | AL    | 4.00     |
    | CA    | 8.25     |

## Example of result

The ece1.py and ece2.py are the deliverables of the first two sprints and the
ece3.py and ececlass.py are the deliverables of the third sprint. The third
sprint was mainly a refactoring sprint to create a class and to add test.py for
unit tests of the class. The development was not test driven. We tested the
deliveries manually in the first two sprints.
