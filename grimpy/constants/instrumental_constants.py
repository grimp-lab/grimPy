
# coding: utf-8

""" Global instrumental constants used for any instrument raw data processing are defined here and imported as needed.
    The constants are:
    =====================   ================================================================================
    Parameter               Description
    =====================   ================================================================================
    IRIS_VERSIONS            Dictionnary gathering IRIS version and their respective calibration constants
    =====================   ================================================================================
    **Usage example:**
        ::
            from grimpy.constants.instrumental_constants import IRIS_VERSIONS
"""

IRIS_VERSIONS = {
    'IRIS_1': 1.26,
    'IRIS_2': 1.205,
    'IRIS_3': 1.258
}
