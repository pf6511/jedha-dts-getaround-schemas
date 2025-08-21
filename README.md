# jedha-dts-getaround-schemas

This module is a shared Python package that defines data models and validation schemas used across different compenents of the getaround ecosystem.

This repo is imported as git submodule into git repos that need it.

To add this package as a git submodule of another git repo

git submodule add https://github.com/your-username/jedha-dts-getaround-schemas.git getaround-schemas

git submodule update --init --recursive

git commit -m "Add getaround-schemas as submodule"

git push origin main


Then install it as a dependency into requirements.txt (for projects/app defined in a docker container)

-e ./getaround-schemas

* dockerfile supposed to install dependencies (pip install -r requirements.txt)

Then import the required models directly into python code as follows
    
    Example with RentalPricePredictInput

    from getaround_schemas.price_predict import RentalPricePredictInput