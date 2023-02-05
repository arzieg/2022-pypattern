"""Test use of the meteogram module."""

# youtube: https://www.youtube.com/watch?v=LX2ksGYXJ80
# Repo
# https://github.com/dopplershift/testing-with-python

from meteogram import meteogram
import datetime
from numpy.testing import assert_almost_equal, assert_array_almost_equal
import numpy as np
from unittest.mock import patch
import pytest
from pathlib import Path


# Beispiel für fixture
# Man sollte Downloads von Webseiten vermeiden, wenn die Technik nicht funktioniert oder aber
# die Datengrundlage sich wieder ändert, sind die Tests wieder anzupassen.
# Besser: Verwenden von lokalen Daten. Hierzu wird ein fixture verwendet.
#  from pathlib import Path
# dann eine Funktion schreiben, die die Daten zur Verfügung stellt. Diese Funktion wird dann
# weiter unten in Tests verwendet (def test_plotting_meteogram_defaults(load_example_asos)
@pytest.fixture()
def load_example_asos():
    """
    Fixture to load example data
    :return:
    """
    example_data_path = Path(__file__).resolve().parent / 'staticdata'
    data_path = example_data_path / 'AMS_example_data.csv'
    return meteogram.download_asos_data(data_path)


#
# Example starter test
#
def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup - none necessary


#
# Instructor led introductory examples
#
def test_title_case():
    # setup
    in_string = 'this is a test string'
    desired_result = 'This Is A Test String'

    # excercise
    actual_result = in_string.title()

    # verify
    assert actual_result == desired_result

    # cleanup - none


#
# Instructor led examples of numerical comparison
#

#
# Exercise 1
#
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    """
    # setup
    start = datetime.datetime(2018, 1, 5, 1)
    end = datetime.datetime(2018, 1, 9, 1)
    station = 'FSD'

    # excersise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # verify
    # hier geht man zweistufig vor.
    # 1. truth_url = ' ' -> aus dem Fehler dann die Url kopieren, im Browser probieren
    #                       und dann einfügen in Schritt zwei
    # 2. truth_url = '

    truth_url = 'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes'
    assert result_url == truth_url

    # cleanup


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # setup
    start = datetime.datetime(2018, 10, 11, 1)
    end = datetime.datetime(2018, 10, 16, 1)
    station = 'FSD'

    # excersise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # verify
    # hier geht man zweistufig vor.
    # 1. truth_url = ' ' -> aus dem Fehler dann die Url kopieren, im Browser probieren
    #                       und dann einfügen in Schritt zwei
    # 2. truth_url = '

    truth_url = 'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2018&month1=10&day1=11&hour1=01&minute1=00&year2=2018&month2=10&day2=16&hour2=01&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes'
    assert result_url == truth_url

    # cleanup


#
# Exercise 1 - Stop Here
#
def test_does_three_equal_three():
    assert 3 == 3


# Floating Points sind kritisch!!
def test_floating_substraction():
    # setup
    desired = 0.293

    # excercise
    actual = 1 - 0.707

    # verify
    # assert actual == desired   <- dieser Test problematisch, da floating point

    # ein möglicher Ansatz, aber auch nicht so elegant
    # assert abs(actual-desired) < 0.00001 # Toleranzwert eintragen

    # numpy hat noch assert methoden! Dies sollte man dann verwenden
    assert_almost_equal(actual, desired)


#
# Exercise 2 - Add calculation tests here
#
def test_wind_components_north():
    # setup
    speed = 10
    direction = 0

    # excercise
    u, v = meteogram.wind_components(speed, direction)

    # verify
    true_u = 0
    true_v = -10
    assert_almost_equal(u, true_u)
    assert_almost_equal(v, true_v)


def test_wind_components_northeast():
    # setup
    speed = 10
    direction = 45

    # excercise
    u, v = meteogram.wind_components(speed, direction)

    # verify
    true_u = -7.0710  # 5 * np.sqrt(2)
    true_v = -7.0710
    assert_almost_equal(u, true_u, 4)
    assert_almost_equal(v, true_v, 4)


#
# Exercise 2 - Stop Here
#
def test_wind_components():
    # Beispiel für ein Assert mit einem Array

    # setup
    speed = np.array([10, 10, 10, 0])
    direction = np.array([0, 45, 360, 45])

    # excersise
    u, v = meteogram.wind_components(speed, direction)

    # verify
    true_u = np.array([0, -7.0710, 0, 0])
    true_v = np.array([-10, -7.0710, -10, 0])

    assert_array_almost_equal(u, true_u, 3)
    assert_array_almost_equal(v, true_v, 3)

    # cleanup - none


#
# Instructor led mock example
#

# diese funktion überschreibt die current_utc_time für das Testen, damit immer ein bestimmtes
# Datum zurückgegeben wird.
# Hierzu ist einzufügen
# from unittest.mock import patch
def mocked_current_utc_time():
    """
    Mock out utc time function for testing with defaults
    :return:
    """

    return datetime.datetime(2018, 3, 26, 12)


# Test, dass der mock funktioniert ;-)
# Patch: ersetze original funktion durch gepatchte funktion
#        zum zeigen, kann man die Zeile @patch auskommentieren und einen pytest absetzen
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_that_mock_works():
    """
    Test if we really know how to use a mock
    :return:
    """
    # setup - none

    # excersise

    result = meteogram.current_utc_time()

    # verify
    truth = datetime.datetime(2018, 3, 26, 12)
    assert result == truth

    # cleanup - node


#
# Exercise 3
#
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_defaults():
    # setup - none
    # excersise
    url = meteogram.build_asos_request_url('MLI')

    # verify
    truth = 'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=25&hour1=12&minute1=00&year2=2018&month2=03&day2=26&hour2=12&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes'
    assert url == truth

    # cleanup - none


def test_current_utc_time():
    # setup - none

    # excersise
    result = meteogram.current_utc_time()

    # verify
    truth = datetime.datetime.utcnow()
    # Ansatz funktioniert nicht, da microseconds sich ändern
    # assert result == truth
    # ein Ansatz, aber nicht der richtige.es kann auch einmal Sekunden sein, wenn microseconds überschritten wird
    assert result.replace(microsecond=0) == truth.replace(microsecond=0)

    # ein besserer Ansatz: Zeitdifferenz nehmen, und einen gewissen "Spielraum" akzeptieren


#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#
# Imagevergleich / Imagetest
# import pytest
# ausserdem musste noch die setup.cfg editiert werden:
#   [tool:pytest]
#   markers = mpl_image_compare
#
# danach einmal mit folgenen Aufruf ausführen
# pytest -k test_plotting_meteogram_defaults --mpl-generate-path=tests/baseline
# -> eine Grafik wird in tests/baseline gespeichert
# pytest -k meteogram --mpl
# -> der eigentlich Testaufruf
@pytest.mark.mpl_image_compare(remove_test=True)
def test_plotting_meteogram_defaults(load_example_asos):
    # setup
    # url = meteogram.build_asos_request_url('AMW',
    #                                       start_date=datetime.datetime(2018,3,26),
    #                                       end_date = datetime.datetime(2018,3,27))
    # df = meteogram.download_asos_data(url)

    # excersise
    # fig, _, _, _ = meteogram.plot_meteogram(df)
    fig, _, _, _ = meteogram.plot_meteogram(load_example_asos)
    # verify

    # cleanup - none

    return fig

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
