# qc-osi-trace

This project implements the OSI Trace Checker for the ASAM Quality Checker project.

- [qc-osi-trace](#qc-osi-trace)
  - [Installation and usage](#installation-and-usage)
    - [Installation using pip](#installation-using-pip)
      - [To use as a library](#to-use-as-a-library)
      - [To use as an application](#to-use-as-an-application)
    - [Installation from source](#installation-from-source)
    - [Example output](#example-output)
  - [Tests](#tests)
    - [Execute tests](#execute-tests)
  - [Contributing](#contributing)

## Installation

qc-osi-trace can be installed using pip or from source.

### Installation using pip

qc-osi-trace can be installed using pip, so that it can be used as a library or as an application.

```bash
pip install qc-osi-trace@git+https://github.com/OpenSimulationInterface/qc-osi-trace@main
```

**Note**: To install from different sources, you can replace `@main` with
your desired target. For example, `develop` branch as `@develop`.

### Installation from source

```bash
pip install .
```

## Usage

### To use as a library

After installation, the usage is similar to the one expressed in the
[`main.py`](./qc_ositrace/main.py) script:

```Python3
from qc_ositrace.checks.deserialization import deserialization_checker
```

### To use as an application

```bash
qc_ositrace --help

usage: QC OSI Trace Checker [-h] [-d | -c CONFIG_PATH] [-i INPUT_FILE] [--osiTopic OSITOPIC] [--osiType OSITYPE]
                            [--osiVersion OSIVERSION] [--osiRulesFile OSIRULESFILE] [-r RESULT_FILE]
                            [--output_config OUTPUT_CONFIG]

ASAM QC checker bundle for checking the validity of OSI Trace (.osi/.mcap) files.

options:
  -h, --help            show this help message and exit
  -d, --default_config  Deprecated. Retained for backward compatibility. Default configuration is used whenever -c is
                        omitted.
  -c, --config_path CONFIG_PATH
  -i, --input_file INPUT_FILE
                        Path to the input OSI Trace file.
  --osiTopic OSITOPIC   Channel topic of a multi-trace OSI Trace file to select.
  --osiType OSITYPE     Type of the OSI Trace file (e.g., 'SensorView', 'SensorData').
  --osiVersion OSIVERSION
                        Expected version of the OSI Trace file (e.g., '3.7.0').
  --osiRulesFile OSIRULESFILE
                        Path to a custom OSI rules file.
  -r, --result_file RESULT_FILE
                        Path to the output result file.
  --output_config OUTPUT_CONFIG
                        Path to save the configuration after running the checks.
```

Example checking a simple SensorData trace file against version 3.7.0 rules using default configuration:

```bash
qc_ositrace -r results.xqar --osiType SensorData --osiVersion 3.7.0 -i 20210818T150542Z_sd_370_300_1523_example_sensordata_trace.osi
```

### Example output

- No issues found

```bash
$ qc_ositrace -c example_config/config.xml
2024-07-31 16:09:01,186 - Initializing checks
2024-07-31 16:09:01,187 - Executing deserialization checks
2024-07-31 16:09:01,188 - Executing deserialization.expected_type check
2024-07-31 16:09:01,188 - Executing deserialization.version_is_set check
2024-07-31 16:09:01,188 - Executing deserialization.expected_version check
2024-07-31 16:09:01,191 - Issues found - 0
2024-07-31 16:09:01,192 - Done
```

- Issues found

```bash
$ qc_ositrace -c example_config/config-errors.xml
2024-07-31 16:15:05,779 - Initializing checks
2024-07-31 16:15:05,780 - Executing deserialization checks
2024-07-31 16:15:05,781 - Executing deserialization.expected_type check
2024-07-31 16:15:05,781 - Executing deserialization.version_is_set check
2024-07-31 16:15:05,781 - Executing deserialization.expected_version check
2024-07-31 16:15:05,796 - Issues found - 547
2024-07-31 16:15:05,806 - Done
```

### Use with ASAM Quality Checker Framework

This checker bundle can be used stand-alone, or with the overall tooling provided by the [ASAM QC Framework](https://www.asam.net/standards/asam-quality-checker/).

For example, to view the checker bundle results obtained in the example above in a GUI with external viewer support:

```bash
ReportGUI results.xqar
```

The framework provides further tooling to merge results from multiple checker bundles, provide textual reports, or reports that fit into CI pipelines.
Please see its [documentation](https://github.com/asam-ev/qc-framework/blob/main/doc/manual/readme.md) for more information.

## Contributing

### Installation from source

For contributing, the project should be installed from source using [Poetry](https://python-poetry.org/), including the development requirements:

```bash
poetry install --with dev
```

You need to have pre-commit installed and install the hooks:

```
pre-commit install
```

After installing from source, the usage is the same as shown above.

It is also possible to execute the qc_ositrace application using Poetry:

```bash
poetry run qc_ositrace --help

usage: QC OSI Trace Checker [-h] [-d | -c CONFIG_PATH] [-i INPUT_FILE] [--osiTopic OSITOPIC] [--osiType OSITYPE]
                            [--osiVersion OSIVERSION] [--osiRulesFile OSIRULESFILE] [-r RESULT_FILE]
                            [--output_config OUTPUT_CONFIG]

ASAM QC checker bundle for checking the validity of OSI Trace (.osi/.mcap) files.

options:
  -h, --help            show this help message and exit
  -d, --default_config  Deprecated. Retained for backward compatibility. Default configuration is used whenever -c is
                        omitted.
  -c, --config_path CONFIG_PATH
  -i, --input_file INPUT_FILE
                        Path to the input OSI Trace file.
  --osiTopic OSITOPIC   Channel topic of a multi-trace OSI Trace file to select.
  --osiType OSITYPE     Type of the OSI Trace file (e.g., 'SensorView', 'SensorData').
  --osiVersion OSIVERSION
                        Expected version of the OSI Trace file (e.g., '3.7.0').
  --osiRulesFile OSIRULESFILE
                        Path to a custom OSI rules file.
  -r, --result_file RESULT_FILE
                        Path to the output result file.
  --output_config OUTPUT_CONFIG
                        Path to save the configuration after running the checks.
```

### Tests

Executing the tests:

```bash
poetry run pytest -vv
```

They should output something similar to:

```bash
================================================= test session starts =================================================
platform win32 -- Python 3.13.9, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\pmai\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\Local\pypoetry\Cache\virtualenvs\qc-osi-trace-aBsWsCJH-py3.13\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\pmai\src\qc-osi-trace
configfile: pyproject.toml
collected 28 items

tests/test_deserialization_checks.py::test_deserialization_version_is_set_examples[invalid-SensorView-547] PASSED [  3%]
tests/test_deserialization_checks.py::test_deserialization_version_is_set_examples[valid-SensorView-0] PASSED    [  7%]
tests/test_deserialization_checks.py::test_deserialization_expected_version[360-SensorView-3.5.0-547] PASSED     [ 10%]
tests/test_deserialization_checks.py::test_deserialization_expected_version[360-SensorView-3.6.0-0] PASSED       [ 14%]
tests/test_deserialization_checks.py::test_deserialization_mcap_topic[360-MySensorView-SensorView-3.5.0-547] PASSED [ 17%]
tests/test_deserialization_checks.py::test_deserialization_mcap_topic[360-MySensorView-SensorView-3.6.0-0] PASSED [ 21%]
tests/test_deserialization_checks.py::test_deserialization_mcap_topic[360-Foo-SensorView-3.6.0--1] PASSED        [ 25%]
tests/test_deserialization_checks.py::test_deserialization_single_topic[360-MySensorView-SensorView-3.5.0-547] PASSED [ 28%]
tests/test_deserialization_checks.py::test_deserialization_single_topic[360-MySensorView-SensorView-3.6.0-0] PASSED [ 32%]
tests/test_deserialization_checks.py::test_deserialization_single_topic[360-Foo-SensorView-3.5.0-547] PASSED     [ 35%]
tests/test_deserialization_checks.py::test_deserialization_single_topic[360-Foo-SensorView-3.6.0-0] PASSED       [ 39%]
tests/test_execution.py::test_nonexistent_input_file PASSED                                                      [ 42%]
tests/test_osirules_checks.py::test_osirules_version_is_set_examples[invalid-SensorView-547] PASSED              [ 46%]
tests/test_osirules_checks.py::test_osirules_version_is_set_examples[valid-SensorView-0] PASSED                  [ 50%]
tests/test_osirules_checks.py::test_osirules_expected_version[360-SensorView-3.5.0-547] PASSED                   [ 53%]
tests/test_osirules_checks.py::test_osirules_expected_version[360-SensorView-3.6.0-0] PASSED                     [ 57%]
tests/test_osirules_checks.py::test_osirules_automatic_rules[deserialization_version_is_set/deserialization_version_is_set_invalid.osi-SensorView-3.6.0-SensorView.version.is_set-0] PASSED [ 60%]
tests/test_osirules_checks.py::test_osirules_automatic_rules[deserialization_version_is_set/deserialization_version_is_set_invalid.osi-SensorView-3.7.0-SensorView.version.is_set-547] PASSED [ 64%]
tests/test_osirules_checks.py::test_osirules_automatic_rules[deserialization_expected_version/deserialization_expected_version_360.osi-SensorView-3.6.0-SensorView.mounting_position.is_set-0] PASSED [ 67%]
tests/test_osirules_checks.py::test_osirules_automatic_rules[deserialization_expected_version/deserialization_expected_version_360.osi-SensorView-3.7.0-SensorView.mounting_position.is_set-547] PASSED [ 71%]
tests/test_osirules_checks.py::test_osirules_automatic_rules[deserialization_expected_version/deserialization_expected_version_360.mcap-SensorView-3.6.0-SensorView.mounting_position.is_set-0] PASSED [ 75%]
tests/test_osirules_checks.py::test_osirules_automatic_rules[deserialization_expected_version/deserialization_expected_version_360.mcap-SensorView-3.7.0-SensorView.mounting_position.is_set-547] PASSED [ 78%]
tests/test_osirules_checks.py::test_osirules_custom_rules[deserialization_version_is_set/deserialization_version_is_set_invalid.osi-SensorView-3.6.0-SensorView.version.is_set-0] PASSED [ 82%]
tests/test_osirules_checks.py::test_osirules_custom_rules[deserialization_expected_version/deserialization_expected_version_360.osi-SensorView-3.6.0-GroundTruth.country_code.is_set-547] PASSED [ 85%]
tests/test_osirules_checks.py::test_osirules_custom_rules[deserialization_expected_version/deserialization_expected_version_360.osi-SensorView-3.6.0-GroundTruth.proj_string.is_set-547] PASSED [ 89%]
tests/test_osirules_checks.py::test_osirules_custom_rules[deserialization_expected_version/deserialization_expected_version_360.osi-SensorView-3.6.0-GroundTruth.map_reference.is_set-547] PASSED [ 92%]
tests/test_osirules_checks.py::test_osirules_custom_rules[deserialization_expected_version/deserialization_expected_version_360.osi-SensorView-3.6.0-GroundTruth.stationary_object.minimum_length_1-547] PASSED [ 96%]
tests/test_osirules_checks.py::test_osirules_custom_rules[deserialization_expected_version/deserialization_expected_version_360.osi-SensorView-3.6.0-GroundTruth.moving_object.maximum_length_1-547] PASSED [100%]

================================================= 28 passed in 17.21s =================================================
```

You can check more options for pytest at its [own documentation](https://docs.pytest.org/).
