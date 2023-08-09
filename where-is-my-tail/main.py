"""Is this my tail?

Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps 
the animals do not have the right tails. To help her, you must correct the broken 
function to make sure that the second argument (tail), is the same as the last 
letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be non empty strings, and normal letters.

source: https://www.codewars.com/kata/56f695399400f5d9ef000af5
"""


def is_tail(animal: str, tail: str) -> bool:
    """Says if tail matches animal

    Args:
        animal (str): an animal name
        tail (str): the last letter of animal

    Returns:
        bool: if tail matches animal or not
    """
    if animal[-1] == tail:
        return True
    return False


if __name__ == "__main__":
    assert is_tail("monkey", "y")
    assert not is_tail("fox", "m")
