"""Tests for the "extensions.api" classes and functions."""

# ======================================================================================================================
# Imports
# ======================================================================================================================
from pytest_flask_ligand import FlaskLigandTestHelpers


# ======================================================================================================================
# Test Suites
# ======================================================================================================================
class TestFlaskLigandTestHelpers(object):
    """Test cases the 'FlaskLigandTestHelpers' helpers class."""

    def test_helpers_fixture_import(self, pytester):
        """
        Verify that the 'helpers' fixture provides access to an instance of the 'FlaskLigandTestHelpers' class.
        """

        # create a temporary pytest test file
        pytester.makepyfile(
            """
            from pytest_flask_ligand import FlaskLigandTestHelpers

            def test_temp(helpers):
                assert isinstance(helpers, FlaskLigandTestHelpers)
            """
        )

        # run all tests with pytest
        result = pytester.runpytest("-ppytest_flask_ligand")

        # check that all tests passed
        result.assert_outcomes(passed=1)

    def test_is_sub_dict_happy_path(self, pytester):
        """
        Verify that the 'is_sub_dict' helper will correctly identify a dictionary is in fact a subset of another
        dictionary.
        """

        small_dict = {"one": 1, "two": 2}
        big_dict = {"one": 1, "two": 2, "three": 3}

        assert FlaskLigandTestHelpers.is_sub_dict(small_dict, big_dict)

    def test_is_sub_dict_order_mismatch(self, pytester):
        """
        Verify that the 'is_sub_dict' helper will correctly identify a dictionary is in fact a subset of another
        dictionary regardless of the order of items.
        """

        small_dict = {"two": 2, "one": 1}
        big_dict = {"one": 1, "three": 3, "two": 2}

        assert FlaskLigandTestHelpers.is_sub_dict(small_dict, big_dict)

    def test_is_sub_dict_same_dict(self, pytester):
        """
        Verify that the 'is_sub_dict' helper will correctly identify a dictionary is considered a sub-dict of itself.
        """

        same_dict = {"uno": 1, "dos": 2}

        assert FlaskLigandTestHelpers.is_sub_dict(same_dict, same_dict)

    def test_is_sub_dict_identical_items(self, pytester):
        """
        Verify that the 'is_sub_dict' helper will correctly identify a dictionary with the same exact items of another
        dictionary is considered a sub-dict.
        """

        first_dict = {"uno": 1, "dos": 2}
        second_dict = {"uno": 1, "dos": 2}

        assert FlaskLigandTestHelpers.is_sub_dict(first_dict, second_dict)


class TestNegativeFlaskLigandTestHelpers(object):
    """Negative test cases the 'FlaskLigandTestHelpers' helpers class."""

    def test_is_sub_dict_different_dicts(self, pytester):
        """
        Verify that the 'is_sub_dict' helper will reject comparisons of dictionary that have the same size,
        but different values.
        """

        first_dict = {"uno": 1, "dos": 2}
        second_dict = {"totally": "different", "dictionaries": "all together"}

        assert not FlaskLigandTestHelpers.is_sub_dict(first_dict, second_dict)

    def test_is_sub_dict_key_mismatch(self, pytester):
        """
        Verify that the 'is_sub_dict' helper will reject comparisons of dictionaries that have the same size,
        but different keys.
        """

        small_dict = {"uno": 1, "dos": 2}
        big_dict = {"one": 1, "two": 2}

        assert not FlaskLigandTestHelpers.is_sub_dict(small_dict, big_dict)

    def test_is_sub_dict_value_mismatch(self, pytester):
        """
        Verify that the 'is_sub_dict' helper will reject comparisons of dictionaries that have the same size,
        but different values.
        """

        small_dict = {"one": "uno", "two": "dos"}
        big_dict = {"one": 1, "two": 2}

        assert not FlaskLigandTestHelpers.is_sub_dict(small_dict, big_dict)
