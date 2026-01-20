# Students API

Simple API built with Python and Flask.

## Requirements
- Python 3
- Flask

## Installation

```bash
pip install -r requirements.txt
````
## /Design Decisions

The Flask framework was chosen because it is simple, lightweight, and suitable for beginners learning how to build REST APIs.

The data storage was implemented using an in-memory list, since the goal of this project is to demonstrate the API functionality without the need for database configuration.

Input validation was added to ensure that the student grade is always between 0 and 10, maintaining data consistency.

The logic to find the first non-repeated letter in the student's name was implemented in a simple and readable way, making the code easier to understand and maintain.

The project structure was kept minimal to focus on clarity and ease of use, following good practices for introductory backend development.
