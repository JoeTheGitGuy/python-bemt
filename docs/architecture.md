# Python BEMT Model
A python implementation of a BEMT model with the purpose of learning
syntax, coding techniques, and architecture philosophy through a
hands-on appraoch. There will be a focus on maintainability through
clean but practical architecture, opposed to optimisation or fidelity.

# Design Goals
-Readable [PEP8]
-Documented
-Maintainable
-Modular
-Few dependencies

# Project Structure
main.py
src/
    load_polar.py
    polar.py
    aerofoil.py
    blade_element.py
    rotor.py
    bem_solver.py
tests/
data/
    xf-naca####-xx-Re-ncrit.csv
docs/
    architecture.md

# Architecture
load_polar.py
    Interfaces with data/* files to generate polar.py instances.
polar.py
    Represents an aerodynamic dataset.
    Owns polar data for coefficients vs. alpha for specific Reynolds
    numbers and aerofoil geometries.
    Owns (interface to ??) method for interpolating coefficients.
aerofoil.py
    Represents 2D aerofoil geometry
    Owns linking to relevant datasets via reference to Polar class.
    Owns interpolation between polar datasets.
blade_element.py
    Represents a geometrically uniform, thin 3D segment of a rotor.
    Owns radial length, position, twist.
    References the Aerofoil class for aerodynamic datasets.
rotor.py
    Represent complete wing geometry.
    Owns interface to bem_solver and multi-element interactions
    (eg. total lift, tip loss adjustment).
    References BladeElement class to consolidate a system of elements
    into a single object.
bem_solver.py
    A numerical solver that resolves force and energy for a rotor
    in a given environment.
config.txt (?)
    Owns initial conditions for environment.
main.py
    Owns interface between config, bem_solver, and rotor.

# Assumptions
Single Reynolds number.
Linear interpolation between AoA datasets.

# Future Work
Multiple Reynolds numbers.
Interpolations between Reynolds numbers.
Tip loss.
Automatic power minimisation via selecting aerofoils.
Transonic considerations?
