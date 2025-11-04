from qc_baselib import StatusType
from qc_baselib.result import Result

import test_setup


def test_nonexistent_input_file(monkeypatch) -> None:
    """Test that non-existent input file results in error status for all checkers"""
    target_file_path = "path/to/nonexistent/file.osi"
    target_type = "SensorView"

    test_setup.create_test_config(target_file_path, target_type)
    test_setup.launch_main(monkeypatch)

    # Load result and verify error status
    result = Result()
    result.load_from_file(test_setup.REPORT_FILE_PATH)

    checker_bundles = result.get_checker_bundle_results()
    assert len(checker_bundles) > 0, "No checker bundles found in result"

    for bundle in checker_bundles:
        checkers = bundle.checkers
        assert len(checkers) > 0, f"No checkers found in bundle {bundle}"
        for checker in checkers:
            assert checker.status == StatusType.ERROR

    test_setup.cleanup_files()
