######################
# Antidepressants - health inequalities
######################

# --IMPORT STATEMENTS--
# Import/clone code building blocks from cohort extractor package

from cohortextractor import (
    StudyDefinition, 
    patients, 
    codelist,
    codelist_from_csv
    # combine_codelists, #not needed as not combining multiple code lists
    # filter_codes_by_category
)

# --DEFINE CODE LIST--
# Codelists are help within the codelist/ folder. 
# This section will import the lists from the codelists.py file

from codelists import *

# --STUDY POPULATION AND STUDY VARIABLES--
# Defines the study population of interest and variables to extract

    # --DEFINES DATA BEHAVIOUR--
study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2000-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    # --DEFINES STUDY POPULATION--
    population=patients.registered_with_one_practice_between(
        "2019-03-01", "today"
    ),

    # --DEFINES STUDY VARIABLES--
    
    ADprecovid = patients.with_these_medications(
            AD_codes,
            between ["2019-03-01", "2020-03-22"],
            return_last_date_in_period=TRUE, # to obtain latest date on AD preCOVID
            return_expectations={"earliest": "2019-03-01", "latest": "2020-03-22"},
            returning = "binary_flag"
            
    )
)
