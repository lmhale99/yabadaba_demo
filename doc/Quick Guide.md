# Quick Guide to yabadaba

## What is yabadaba?

The yabadaba package stands for "yay, a base database!"  What it does is offer an abstraction of database and database record interactions so that the end users who are generating and using data stored in a database can focus on the "data" over the "database infrastructure". 


## Built-in unit conversions

### Unit conversion methodology

For convenience, yabadaba contains a lightweight scheme for handling unit conversions.  The unit conversions are built-in to some of yabadaba's features but are entirely optional if you use an alternate scheme.

Unit conversions follow the principles of the numericalunits package, in that a set of compatible working units is defined relative to the basic independent SI units.  From this, then, nearly every other unit can be represented as a multiplication or division operation relative to those working units.  This allows for unit conversions to be handled in an extremely simple and lightweight manner:

- When values are defined, the units should be specified so that they can be converted into the pre-defined compatible working units.
- All calculations and evaluations are then performed in the working units.
- When it is time to report any computed values, specify the units that you want to get the values in.

This is a simple scheme that insures the math is compatible during the calculations without any calculation overhead.  

The caveats with this method are

- When converting between different units, there are no active checks performed as to if the units are for the same dimensions.  This means that it largely your responsibility to know what your calculations are doing to ensure valid unit conversions.  You can partially check that unit conversions are proper by running the same calculation multiple times with different working units and seeing if the values change.
- Any values that are assigned without units being specified are taken as either being unit-less or already in the compatible working units.  Ideally, any input/output values should explicitly define the associated units as the working units can be changed.
- This type of unit conversion only works for absolute units.  The main example where this could be an issue is temperature, as C and F are both *not* absolute units.  

### Unit conversion setup

Unit conversions are managed by the yabadaba.unitconvert object, which is an instance of the yabadaba.UnitConverter class.  At the base level of your package, import yabadaba.unitconvert.  Then, anywhere else in your code, import the unitconvert object from either yabadaba or your base level.  If your package and any other yabadaba-based packages all import the unitconvert object, then the working units and conversions will be compatible across all.

Do note, however, that different packages may define different preferred working units.  If you are importing multiple yabadaba-based packages and having the working units in specific values is important to you then you should manually specify the working units after all imports.

A final option is to initialize a new UnitConverter object for your project.  Doing so will isolate the unit conversion operations in your project from any others.  This, however, might lead to more issues than benefits when interfacing with other yabadaba-based projects as the the working units will differ between projects!

Once imported, you can set default working units for your package with unitconvert.reset_units().

### Performing unit conversions

The unitconvert object has a number of methods to assist with unit conversions.

Input operations read in values with specified units and convert them into compatible working units

- set_in_units() takes an int, float or numpy.array value and a string unit indicating what the given values are in.
- set_literal() takes a string value that contains both the number(s) and the units.
- value_unit() takes a dict containing 'value' and 'unit' fields (and optionally a 'shape' field for multidimensional arrays).
- error_unit() takes a dict containing 'error' and 'unit' fields (and optionally a 'shape' field for multidimensional arrays).

Output operations

- get_in_units() takes an int, float or numpy.array and a string unit indicating what units the value should be converted to.
- model() takes an int, float or numpy.array value and a string unit, and generates a dict with 'value', 'unit', (and 'shape') fields.  If an error value is also included, then it will be added to the resulting dict as well. 

