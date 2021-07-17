import pytest

from yatzy import Yatzy, roll_numbers_count

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_roll_numbers_count():
    count_five_ones = roll_numbers_count([1, 1, 1, 1, 1])
    assert {1: 5} == count_five_ones

    count_three_ones_and_two_threes = roll_numbers_count([1, 1, 1, 3, 3])
    assert {1: 3, 3: 2} == count_three_ones_and_two_threes

    count_two_ones_and_one_threes_and_one_six = roll_numbers_count([1, 1, 3, 3, 6])
    assert {1: 2, 3: 2, 6: 1} == count_two_ones_and_one_threes_and_one_six


def test_chance_scores_sum_of_all_dice():
    assert 15 == Yatzy.chance([2, 3, 4, 5, 1])
    assert 16 == Yatzy.chance([3, 3, 4, 5, 1])

    with pytest.raises(Exception):
        assert 16 == Yatzy.chance([3, 5, 1])


def test_yatzy_scores_50():
    assert 50 == Yatzy.yatzy([4, 4, 4, 4, 4])
    assert 50 == Yatzy.yatzy([6, 6, 6, 6, 6])
    assert 0 == Yatzy.yatzy([6, 6, 6, 6, 3])

    with pytest.raises(Exception):
        assert 50 == Yatzy.yatzy([4, 4, 4])


def test_select_roll_count_ones():
    assert 0 == Yatzy.select_roll_count([6, 2, 2, 4, 5], 1)
    assert 1 == Yatzy.select_roll_count([1, 2, 3, 4, 5], 1)
    assert 2 == Yatzy.select_roll_count([1, 2, 1, 4, 5], 1)
    assert 4 == Yatzy.select_roll_count([1, 2, 1, 1, 1], 1)

    with pytest.raises(Exception):
        assert 4 == Yatzy.select_roll_count([1, 1, 1], 1)


def test_select_roll_count_twos():
    assert 4 == Yatzy.select_roll_count([1, 2, 3, 2, 6], 2)
    assert 10 == Yatzy.select_roll_count([2, 2, 2, 2, 2], 2)

    with pytest.raises(Exception):
        assert 4 == Yatzy.select_roll_count([1, 1, 1], 2)


def test_select_roll_count_threes():
    assert 6 == Yatzy.select_roll_count([1, 2, 3, 2, 3], 3)
    assert 12 == Yatzy.select_roll_count([2, 3, 3, 3, 3], 3)

    with pytest.raises(Exception):
        assert 4 == Yatzy.select_roll_count([1, 1, 1], 3)


def test_select_roll_count_fours_test():
    assert 12 == Yatzy.select_roll_count([4, 4, 4, 5, 5], 4)
    assert 8 == Yatzy.select_roll_count([4, 4, 5, 5, 5], 4)
    assert 4 == Yatzy.select_roll_count([4, 5, 5, 5, 5], 4)

    with pytest.raises(Exception):
        assert 4 == Yatzy.select_roll_count([1, 1, 1], 4)


def test_select_roll_count_fives():
    assert 10 == Yatzy.select_roll_count([4, 4, 4, 5, 5], 5)
    assert 15 == Yatzy.select_roll_count([4, 4, 5, 5, 5], 5)
    assert 20 == Yatzy.select_roll_count([4, 5, 5, 5, 5], 5)

    with pytest.raises(Exception):
        assert 4 == Yatzy.select_roll_count([1, 1, 1], 5)


def test_select_roll_count_sixes_test():
    assert 0 == Yatzy.select_roll_count([4, 4, 4, 5, 5], 6)
    assert 6 == Yatzy.select_roll_count([4, 4, 6, 5, 5], 6)
    assert 18 == Yatzy.select_roll_count([6, 5, 6, 6, 5], 6)

    with pytest.raises(Exception):
        assert 4 == Yatzy.select_roll_count([1, 1, 1], 6)


def test_one_pair():
    assert 6 == Yatzy.score_pair([3, 4, 3, 5, 6])
    assert 10 == Yatzy.score_pair([5, 3, 3, 3, 5])
    assert 12 == Yatzy.score_pair([5, 3, 6, 6, 5])

    with pytest.raises(Exception):
        assert 4 == Yatzy.score_pair([1, 1, 1])


def test_two_Pair():
    assert 16 == Yatzy.two_pair([3, 3, 5, 4, 5])
    assert 18 == Yatzy.two_pair([3, 3, 6, 6, 6])
    assert 0 == Yatzy.two_pair([3, 3, 6, 5, 4])

    with pytest.raises(Exception):
        assert 4 == Yatzy.two_pair([1, 1, 1])


def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind([3, 3, 3, 4, 5])
    assert 15 == Yatzy.three_of_a_kind([5, 3, 5, 4, 5])
    assert 9 == Yatzy.three_of_a_kind([3, 3, 3, 3, 5])

    with pytest.raises(Exception):
        assert 4 == Yatzy.three_of_a_kind([1, 1, 1])


def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind([3, 3, 3, 3, 5])
    assert 20 == Yatzy.four_of_a_kind([5, 5, 5, 4, 5])
    assert 12 == Yatzy.four_of_a_kind([3, 3, 3, 3, 3])
    assert 0 == Yatzy.four_of_a_kind([3, 3, 3, 2, 1])

    with pytest.raises(Exception):
        assert 4 == Yatzy.four_of_a_kind([1, 1, 1])


def test_small_straight():
    assert 30 == Yatzy.straights([2, 5, 3, 4, 2])
    assert 30 == Yatzy.straights([1, 2, 3, 6, 5])
    assert 0 == Yatzy.straights([1, 2, 2, 4, 5])

    with pytest.raises(Exception):
        assert 4 == Yatzy.straights([1, 1, 1])


def test_large_straight():
    assert 40 == Yatzy.straights([6, 2, 3, 4, 5])
    assert 40 == Yatzy.straights([2, 3, 4, 5, 6])
    assert 0 == Yatzy.straights([1, 2, 2, 4, 5])

    with pytest.raises(Exception):
        assert 4 == Yatzy.straights([1, 1, 1])


def test_full_house():
    assert 25 == Yatzy.full_house([6, 2, 2, 2, 6])
    assert 0 == Yatzy.full_house([2, 3, 4, 5, 6])

    with pytest.raises(Exception):
        assert 4 == Yatzy.full_house([1, 1, 1])
