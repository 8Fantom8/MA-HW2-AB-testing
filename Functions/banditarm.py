import numpy as np

class BanditArm:
    def __init__(self, p: float):
        self.p = p  # True probability of winning
        self.p_estimate = 0.0  # Estimated probability of winning
        self.N = 0  # Number of times this arm has been pulled

    def __repr__(self) -> str:
        return f'BanditArm(p={self.p:.2f}, p_estimate={self.p_estimate:.2f}, N={self.N})'

    def pull(self) -> float:
        """Simulate pulling the arm by returning a reward sampled from a Bernoulli distribution."""
        return 1 if np.random.random() < self.p else 0

    def update(self, reward: float) -> None:
        """Update the estimate of p based on the reward received."""
        self.N += 1
        self.p_estimate = ((self.N - 1) * self.p_estimate + reward) / self.N


