
***CURRY SELECTOR***

Author @ Patrick Collins
V.1:25 July 2021
V.2:29 July 2021
Python 3 
Attempted solution to KitchenOS Engineer - Code
Challenge: The Curry Wholesaler problem

***V.2 Update:
V.2 now successfully solves all sample input and successfully selected ~ 10 test inputs created using input generator.

Run input generator:
From 'test' dir, run 'python inpgen.py'
It will output an input file to /sample_inputs/ and a file to /sample_inputs/test/ This test fall is parsed to be visually easier to manually trace inputs to determine if app output - curry selection - is correct. So far, so good.

Run CurrySelector:
From main dir, run 'python app.py </pathTo/sample/inputs/>'

No change to unit tests as I decided it would be more interesting and more useful to create the class to create test inputs.

This work is very brute force. I'm sure there's a better, more terse way to do this. I would love to get feedback and see a proper solution regardless of the outcome of my hiring candidacy.

Thanks!

Kind regards,

Patrick Collins

*******************
V.1 Release:
This seemed really simple, but the logic was much trickier to apply programatically...

This is an update: App doesn't function correctly for all inputs. I tried to add some looping logic as a second pass to compare codified customer preferences
against the tentative menu, which worked in some cases, not in others (including runaway loops). To get this right, I would have to take it apart and start over
and unfortunately I cannot afford the time. I commented out the looping section (docstring instead of individual #s), and I left commented out the procedural script to run with some debugging that's also commented out. 

Test case can be run (to simplify this, I just have all necessary files in same dir) by running python -m unittest testcase.py. I included shebangs for linux (and hopefully macOS?).

To run the application directly, remove docstring """'s from #procedural section and run: python app.py from the app directory followed by the path to an input text file

Questions and Assumptions:
*While clearly stated that no customer will want more than 1 meat curry, there is no definition for total number of Meat curries.
I played with the idea of only allowing one, but in the instance of multiple customers each wanting a different type of meat with no veg options,
this doesn't work. It should be possible for all of N options to be meat if you have many carnivorous customers.
* This was a 'brute force' effort - this could probably be more elegant and less lines of code. It seems to work, and works in all the scenarios I tried.
* App has been vetted in pep8 and pylint to meet typical conventions
* long nested if statements are generally bad, and mine are a little repetetive - better application of DRY would be preferable; given more time (I tried to stick to roughly the 3 hours suggested) this would be cleaner, less repetetive code.

I assume that a not perfectly functioning exercise is probably a no-go for going forward in the hiring process, and I get that. I would love to get feedback on what I have done, and learn what a correct approach would have been. I assume this could be done in 10 or 20 LoC...


Thanks for the opportunity. The exercise was fun to work on, I learned (and re-learned) a number of useful python tricks; I just wish I'd managed a better solution.

Kind regards,

Patrick Collins
pjcollins@gmail.com