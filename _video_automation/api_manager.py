"""
Multi-Account API Manager
Handles API calls with automatic failover across multiple accounts
"""

import time
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import json
from pathlib import Path


@dataclass
class AccountStatus:
    """Track API account status"""
    name: str
    api_key: str
    daily_limit: int
    used_today: int = 0
    last_reset: datetime = field(default_factory=datetime.now)
    is_exhausted: bool = False
    last_error: Optional[str] = None

    def remaining(self) -> int:
        """Get remaining quota"""
        return max(0, self.daily_limit - self.used_today)

    def can_use(self) -> bool:
        """Check if account can be used"""
        # Check if it's a new day (quota reset)
        if (datetime.now() - self.last_reset).days >= 1:
            self.reset_daily_quota()

        return not self.is_exhausted and self.remaining() > 0

    def reset_daily_quota(self):
        """Reset daily quota"""
        self.used_today = 0
        self.is_exhausted = False
        self.last_reset = datetime.now()
        self.last_error = None

    def mark_used(self):
        """Mark one request as used"""
        self.used_today += 1
        if self.used_today >= self.daily_limit:
            self.is_exhausted = True

    def mark_exhausted(self, error_msg: str):
        """Mark account as exhausted"""
        self.is_exhausted = True
        self.last_error = error_msg

    def time_until_reset(self) -> str:
        """Get time until quota resets"""
        next_reset = self.last_reset + timedelta(days=1)
        delta = next_reset - datetime.now()

        hours = int(delta.total_seconds() // 3600)
        minutes = int((delta.total_seconds() % 3600) // 60)

        return f"{hours}h {minutes}m"


class MultiAccountAPIManager:
    """Manages multiple API accounts with automatic failover"""

    def __init__(self, accounts: List[Dict], state_file: Optional[str] = None):
        self.accounts: List[AccountStatus] = []
        self.current_account_index = 0
        self.state_file = state_file or str(Path(__file__).parent / ".api_state.json")

        # Initialize accounts
        for acc in accounts:
            self.accounts.append(AccountStatus(
                name=acc['name'],
                api_key=acc['api_key'],
                daily_limit=acc.get('daily_limit', 50)
            ))

        # Load previous state
        self.load_state()

    def load_state(self):
        """Load API usage state from file"""
        if not Path(self.state_file).exists():
            return

        try:
            with open(self.state_file, 'r') as f:
                state = json.load(f)

            for acc in self.accounts:
                if acc.name in state:
                    acc_state = state[acc.name]
                    acc.used_today = acc_state.get('used_today', 0)
                    last_reset_str = acc_state.get('last_reset')
                    if last_reset_str:
                        acc.last_reset = datetime.fromisoformat(last_reset_str)

                    # Check if it's a new day
                    if (datetime.now() - acc.last_reset).days >= 1:
                        acc.reset_daily_quota()

        except Exception as e:
            print(f"Warning: Could not load API state: {e}")

    def save_state(self):
        """Save API usage state to file"""
        try:
            state = {}
            for acc in self.accounts:
                state[acc.name] = {
                    'used_today': acc.used_today,
                    'last_reset': acc.last_reset.isoformat(),
                    'is_exhausted': acc.is_exhausted
                }

            with open(self.state_file, 'w') as f:
                json.dump(state, f, indent=2)

        except Exception as e:
            print(f"Warning: Could not save API state: {e}")

    def get_current_account(self) -> Optional[AccountStatus]:
        """Get current active account"""
        if not self.accounts:
            return None

        # Try to find next available account
        for _ in range(len(self.accounts)):
            acc = self.accounts[self.current_account_index]

            if acc.can_use():
                return acc

            # Try next account
            self.current_account_index = (self.current_account_index + 1) % len(self.accounts)

        # No accounts available
        return None

    def get_total_remaining_quota(self) -> int:
        """Get total remaining quota across all accounts"""
        return sum(acc.remaining() for acc in self.accounts)

    def mark_request_success(self):
        """Mark current request as successful"""
        acc = self.accounts[self.current_account_index]
        acc.mark_used()
        self.save_state()

    def mark_request_failed(self, error_msg: str, quota_exceeded: bool = False):
        """Mark current request as failed"""
        acc = self.accounts[self.current_account_index]

        if quota_exceeded:
            acc.mark_exhausted(error_msg)
            print(f"[\!]  {acc.name} quota exhausted")

            # Try next account
            self.current_account_index = (self.current_account_index + 1) % len(self.accounts)

            next_acc = self.get_current_account()
            if next_acc:
                print(f"   -> Switching to {next_acc.name} ({next_acc.remaining()} remaining)")
            else:
                print(f"   [X] All accounts exhausted!")

        self.save_state()

    def get_status_summary(self) -> str:
        """Get formatted status summary"""
        lines = []
        lines.append("API Quota Status:")
        lines.append("=" * 60)

        total_limit = sum(acc.daily_limit for acc in self.accounts)
        total_used = sum(acc.used_today for acc in self.accounts)
        total_remaining = sum(acc.remaining() for acc in self.accounts)

        for i, acc in enumerate(self.accounts, 1):
            status = "[OK]" if acc.can_use() else "[X]"
            bar_length = 20
            used_bars = int((acc.used_today / acc.daily_limit) * bar_length) if acc.daily_limit > 0 else 0
            bar = "#" * used_bars + "-" * (bar_length - used_bars)

            lines.append(f"{status} {acc.name}:")
            lines.append(f"   [{bar}] {acc.used_today}/{acc.daily_limit}")

            if acc.is_exhausted:
                lines.append(f"   Resets in: {acc.time_until_reset()}")

        lines.append("=" * 60)
        lines.append(f"Total: {total_used}/{total_limit} used, {total_remaining} remaining")

        if total_remaining == 0:
            earliest_reset = min(acc.time_until_reset() for acc in self.accounts)
            lines.append(f"All exhausted. Next reset in: {earliest_reset}")

        return "\n".join(lines)

    def check_capacity(self, required_requests: int) -> Dict[str, Any]:
        """Check if there's enough capacity for required requests"""
        total_remaining = self.get_total_remaining_quota()

        return {
            'sufficient': total_remaining >= required_requests,
            'available': total_remaining,
            'required': required_requests,
            'shortfall': max(0, required_requests - total_remaining)
        }

    def get_api_key(self) -> Optional[str]:
        """Get API key for current account"""
        acc = self.get_current_account()
        return acc.api_key if acc else None

    def has_capacity(self) -> bool:
        """Check if any account has capacity"""
        return any(acc.can_use() for acc in self.accounts)


def main():
    """Test API manager"""
    # Example accounts
    accounts = [
        {'name': 'Account 1', 'api_key': 'key1', 'daily_limit': 50},
        {'name': 'Account 2', 'api_key': 'key2', 'daily_limit': 50},
        {'name': 'Account 3', 'api_key': 'key3', 'daily_limit': 50},
    ]

    manager = MultiAccountAPIManager(accounts)
    print(manager.get_status_summary())

    print("\n--- Checking capacity for 100 requests ---")
    capacity = manager.check_capacity(100)
    print(f"Sufficient: {capacity['sufficient']}")
    print(f"Available: {capacity['available']}")
    print(f"Required: {capacity['required']}")


if __name__ == "__main__":
    main()
