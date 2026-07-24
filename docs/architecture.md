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
    blade.py
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
    Owns polar data for coefficients vs. alpha for specific Reynolds
    numbers and aerofoil geometries.
aerofoil.py
    Owns characteristic 2D aerofoil geometry, references polar
    class.
blade_element.py
    Represents a geometrically uniform, thin 3D segment of a rotor,
    owning radial length, and referencing the aerofoil class.
rotor.py
    A complete wing geometry owning how many radial segments it is
    composed of, their locations, twist, and referencing which
    blade elements they would use.
bem_solver.py
    A numerical solver that resolves force and energy for a rotor
    in a given environment.

# Assumptions
Single Reynolds number.
Linear interpolation between AoA datasets.

# Future Work
Multiple Reynolds numbers.
Tip loss.
Automatic power minimisation via selecting aerofoils.
