import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers returns 0."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a simple case with one streak."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_multiple_streaks_longest_first():
    """Test with multiple streaks where the longest is first."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2]) == 3

def test_multiple_streaks_longest_last():
    """Test with multiple streaks where the longest is last."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 4]) == 4

def test_streaks_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6]) == 3

def test_example_from_brief():
    """Test the primary example from the coding brief."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_long_list():
    """Test with a longer list and multiple streaks."""
    assert longest_positive_streak([1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0]) == 4

def test_zeros_and_negatives_mixed():
    """Test a mix of zeros and negative numbers as streak breakers."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6, 7, 8]) == 3

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-5]) == 0