import numpy as np


def trigonomeric_identity(angle: float) -> float:
    """Calculates trig identity

    param:
    angle: angle in radians

    return: trigonometric one
    """

    print("Running trigonometric_identity()")
    return np.cos(angle) ** 2 + np.sin(angle) ** 2


if __name__ == "__main__":
    print("Running directyly from module2.py")  
    print(trigonomeric_identity(42))
else:
    print("You have imported me")