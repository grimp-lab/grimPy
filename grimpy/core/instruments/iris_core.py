# coding: utf-8

'''
This module implements core functions for processing raw IRIS measures (in Volts) to SSA (in m :sup:`2`.m :sup:`-3`).
'''

import numpy as np
from grimpy.constants.instrumental_constants import IRIS_VERSIONS
from grimpy.constants.physical_constants import DENSITY_OF_ICE, IM_REFRACTION, RAYONNEMENT_I


def calibration_polynom_fit(spectralon, calibration_values):
    """
    Computes a cubic calibration polynomial function from the calibration measured voltages and the spectralon values
    :param spectralon: percentage of reflectance of the spectralon used for calibration
    :type spectralon: numpy array of floats. For example, reflectance are logged as 80 for 80% in the spreadsheet
    :param calibration_values: voltage measured by IRIS
    :param calibration_values: numpy array of floats
    """

    polynom = np.polyfit(calibration_values, spectralon, deg=3)

    return polynom


def voltage_to_reflectance(voltage, polynom):
    """
    Computes reflectance based on a voltage measurement and the cubic polynomial calibration function
    :param voltage: voltage (Volt) measured by IRIS
    :type voltage: float
    :param polynom: calibration polynom computed for the considered IRIS measurements session
    :type polynom: numpy polyfit object
    """

    reflectance = polynom[0] * volt**3 + polynom[1] * volt**2 + polynom[2] * volt + polynom[3]

    return np.around(reflectance, 2)


def reflectance_to_ssa(reflectance, version):
    """
        Computes SSA based on a reflectance computation and the IRIS version used calibration constant
        :param reflectance: reflectance value computed by voltage_to_reflectance
        :type reflectance: float
        :param version: IRIS version number used for the measurement session
        :type version: int
    """

    ssa = 4 * np.pi * IM_REFRACTION / RAYONNEMENT_I * 6 / DENSITY_OF_ICE * (K_0 * B / np.log(reflectance / 100)) ** 2


    return np.around(ssa,2)

def ssa_to_optical_radius(ssa):
    """
        Computes optical radius (mm) based on ssa value computated by reflectance_to_ssa
        :param reflectance: SSA value in m :sup:`2`.m :sup:`-3`
        :type reflectance: float
    """

    optical_radius = (3.0 / (DENSITY_OF_ICE * ssa)) * 10**3

    return optical_radius
