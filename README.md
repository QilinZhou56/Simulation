# Simulation Repository

## Overview

This repository contains a collection of simulation codes for various scenarios and purposes. The simulations range from voting procedures and wait times in restaurants to treemap visualizations. These codes are intended to aid in learning and study, providing practical examples of simulation in different contexts.

## Contents
- `customer.py`, `queue.py`: A simulation of customer wait times based on queue data structure, with Poisson arrivals, deterministic service time, and one service, useful for understanding queue management and service efficiency.
  
  ### Features
  - **Arrivals**: follow a Markov process (M)
  - **Service Time**: the time to service each customer is deterministic (D)
  - **Number of Servers**: there is only one server (1)

- `Gerrymandering.py`: a Python application designed to simulate the division of a grid into electoral districts. It demonstrates key principles like equal population, contiguity, and compactness in district creation. The program uses the Tkinter library for graphical representation and allows users to visualize how different numbers of districts can be mapped on a grid. 

  ### Features
  - **Grid Division**: Divides a grid into a specified number of districts.
  - **Random Color Assignment**: Assigns colors (light red and light blue) to each cell in the grid randomly, representing different political affiliations.
  - **District Visualization**: Clearly delineates district boundaries with black lines.
  - **Adherence to Principles**: Follows the principles of equal population, contiguity, and compactness in district creation.


