##antidepressants - health inequalities
from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.registered_with_one_practice_between(
        "2019-04-01", "today"
    ),

    agepostcovid=patients.age_as_of(
        "today",
        return_expectations={
            "rate": "universal",
            "int": {"distribution":"population_ages"},
        }
    ),

    ageprecovid=patients.age_as_of(
        "2020-02-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution":"population_ages"},
        }
    ),

    sex=patients.sex( 
    return_expectations={
        "rate": "universal",
        "category": {"ratios": {"M": 0.49, "F": 0.51}
        }
    ),

    ethnicity_by_16_grouping=patients.with_ethnicity_from_sus(
    returning="group_16",
    use_most_frequent_code=True,
    ),

    imd=patients.address_as_of(
    "2020-02-29",
    returning="index_of_multiple_deprivation",
    round_to_nearest=100,
    return_expectations={
        "rate": "universal",
        "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
    },
    ),

    region=patients.registered_practice_as_of(
    "2020-02-01",
    returning="nuts1_region_name",
    return_expectations={
        "rate": "universal",
        "category": {
            "ratios": {
                "North East": 0.1,
                "North West": 0.1,
                "Yorkshire and the Humber": 0.1,
                "East Midlands": 0.1,
                "West Midlands": 0.1,
                "East of England": 0.1,
                "London": 0.2,
                "South East": 0.2,
            },
        },
    },
    ),
)
