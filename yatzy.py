def validate_rolls(func):
    def inner(rolls):
        """
            decorator to validate that rolls return 5 dice

            Args:
                rolls (int[]): dice rolls.

            Returns:
                func: callback function
        """
        if len(rolls) != 5:
            raise Exception("Please make sure you have 5 dice rolled")
        return func(rolls)
    return inner


def roll_numbers_count(rolls):
    """
        counts instance of numbers within the roll

        Example: 
            [1,1,2,3] -> {1:2, 2:1, 3:1}

        Args:
            rolls (int[]): dice rolls.

        Returns:
            {key: int}: count of each number rolled
    """
    rollDict = {}

    for roll in rolls:
        if roll in rollDict:
            rollDict[roll] += 1
        else:
            rollDict[roll] = 1

    return rollDict


class Yatzy:

    @staticmethod
    @validate_rolls
    def chance(rolls):
        """
            The player scores the sum of all dice, no matter what they read.

            Example:
                1,1,3,3,6 placed on "chance" scores 14 (1+1+3+3+6)
                4,5,5,6,1 placed on "chance" scores 21 (4+5+5+6+1)

            Args:
                rolls (int[]): dice rolls.

            Returns:
                int: sum of all dice
        """
        return sum(rolls)

    @staticmethod
    @validate_rolls
    def yatzy(rolls):
        """
            If all dice have the same number, the player scores 50 points.

            Example:
                1,1,1,1,1 placed on "yatzy" scores 50
                1,1,1,2,1 placed on "yatzy" scores 0

            Args:
                roll (int[]): dice rolls.

            Returns:
                int: point value of yatzy
        """
        rollCount = roll_numbers_count(rolls)

        for key in rollCount:
            if rollCount[key] == 5:
                return 50

        return 0

    @staticmethod
    def select_roll_count(rolls, chosenNumber):
        """
            The player scores the sum of the dice that reads one, two, three, four, five or six, respectively.

            Example:
                1,1,2,4,4 placed on "fours" scores 8 (4+4)
                2,3,2,5,1 placed on "twos" scores 4 (2+2)
                3,3,3,4,5 placed on "ones" scores 0

            Args:
                rolls (int[]): dice rolls.
                chosenNumber (int): chosen number by user.

            Returns:
                int: point value instances of chosen number
        """
        rollCount = roll_numbers_count(rolls)

        if chosenNumber in rollCount:
            return rollCount[chosenNumber] * chosenNumber

        return 0

    @staticmethod
    @validate_rolls
    def score_pair(rolls):
        """
            The player scores the sum of the two highest matching dice.

            Example:
                3,3,3,4,4 scores 8 (4+4)
                1,1,6,2,6 scores 12 (6+6)
                3,3,3,4,1 scores 6 (3+3)
                3,3,3,3,1 scores 6 (3+3)

            Args:
                rolls (int[]): dice rolls.

            Returns:
                int: point value of pair
        """
        rollCount = roll_numbers_count(rolls)
        pair = 0

        for key in rollCount.keys():
            if rollCount[key] == 2 and key > pair:
                pair = key

        return pair * 2

    @staticmethod
    @validate_rolls
    def two_pair(rolls):
        """
            If there are two pairs of dice with the same number, the player scores the sum of these dice.

            Examples:
                1,1,2,3,3 scores 8 (1+1+3+3)
                1,1,2,3,4 scores 0
                1,1,2,2,2 scores 6 (1+1+2+2)

            Args:
                rolls (int[]): dice rolls.

            Returns:
                int: point value of two pairs
        """

        rollCount = roll_numbers_count(rolls)
        pairList = []

        for key in rollCount.keys():
            if rollCount[key] >= 2:
                pairList.append(key)

        if len(pairList) == 2:
            return sum(pairList) * 2

        return 0

    @staticmethod
    @validate_rolls
    def three_of_a_kind(rolls):
        """
            If there are three dice with the same number, the player scores the sum of these dice.

            Examples:
                3,3,3,4,5 scores 9 (3+3+3)
                3,3,4,5,6 scores 0
                3,3,3,3,1 scores 9 (3+3+3)

            Args:
                rolls (int[]): dice rolls.

            Returns:
                int: point value of three of a kind
        """
        rollCount = roll_numbers_count(rolls)

        for key in rollCount.keys():
            if rollCount[key] >= 3:
                return key * 3

        return 0

    @staticmethod
    @validate_rolls
    def four_of_a_kind(rolls):
        """
            If there are four dice with the same number, the player scores the sum of these dice

            Examples:
                2,2,2,2,5 scores 8 (2+2+2+2)
                2,2,2,5,5 scores 0
                2,2,2,2,2 scores 8 (2+2+2+2)

            Args:
                rolls (int[]): dice rolls.

            Returns:
                int: point value of four of a kind
        """
        rollCount = roll_numbers_count(rolls)

        for key in rollCount.keys():
            if rollCount[key] >= 4:
                return key * 4

        return 0

    @staticmethod
    @validate_rolls
    def straights(rolls):
        """
            When placed on "small straight", four sequencial numbers. Or "large straight", five sequencial numbers.

            Examples:
                1,2,3,4,n scores 30.
                2,3,4,5,6 scores 40.

            Args:
                rolls (int[]): dice rolls.

            Returns:
                int: point value of four of smallStraight
        """
        sortedRolls = sorted(rolls)
        count = 0
        index = 1

        while len(sortedRolls) > index:
            if sortedRolls[index] - sortedRolls[index-1] == 1:
                count += 1

            index += 1

        if count == 4:
            # Large Straight
            return 40

        if count == 3:
            # Small Straight
            return 30

        return 0

    @staticmethod
    @validate_rolls
    def full_house(rolls):
        """
            If the rolls a full house.

            Examples:
                1,1,2,2,2 scores 25
                2,2,3,3,4 scores 0
                4,4,4,4,4 scores 0

            Args:
                rolls (int[]): dice rolls.

            Returns:
                int: point value of fullHouse
        """
        rollCount = roll_numbers_count(rolls)
        count = 0

        for key in rollCount.keys():
            roll = rollCount[key]
            if roll == 2 or roll == 3:
                count += roll

        if count == 5:
            return 25

        return 0
