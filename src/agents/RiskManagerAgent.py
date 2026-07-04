# src/agents/RiskManagerAgent.py
from src.utils.logger import setup_logger

logger = setup_logger("RiskManagerAgent")

class RiskManagerAgent:
    """Computes mathematical bet-sizing and checks scale/arbitrage rules"""
    
    def __init__(self, fractional_multiplier: float = 0.5):
        self.fractional_multiplier = fractional_multiplier # Half-Kelly for tail protection

    def calculate_allocation(self, win_probability: float, market_price: float) -> float:
        """
        Kelly Criterion Formula: f* = (b * p - q) / b
        Where:
        b = decimal net odds received on the wager (payout - stake)/stake
        p = probability of winning
        q = probability of losing (1 - p)
        """
        logger.info(f"Evaluating Risk Matrix: Win Prob={win_probability:.2f}, Contract implied price={market_price}")
        
        if market_price <= 0 or market_price >= 1:
            logger.warning("Invalid contract implied price bounds. Allocation halted safely.")
            return 0.0
            
        # Payout odds b based on contract acquisition cost
        # e.g., if contract costs $0.54, it pays out $1.00. Payout = 1/0.54 - 1
        b = (1.0 / market_price) - 1.0
        p = win_probability
        q = 1.0 - p
        
        if b <= 0:
            return 0.0
            
        kelly_f = (b * p - q) / b
        
        # Apply fractional constraints to manage leverage risk safely
        safe_allocation = max(0.0, kelly_f * self.fractional_multiplier)
        
        logger.info(f"Mathematical Optimal Allocation computed: {safe_allocation:.4f} (Raw Kelly: {kelly_f:.4f})")
        return round(safe_allocation, 4)