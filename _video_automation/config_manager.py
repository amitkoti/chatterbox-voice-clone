"""
API Configuration Manager
Handles multiple API keys and configuration loading
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Optional


class APIConfig:
    """Manages API keys and configuration"""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path or self._default_config_path()
        self.google_accounts: List[Dict] = []
        self.fallback_apis: Dict = {}
        self.load_config()

    def _default_config_path(self) -> str:
        """Get default config file path"""
        script_dir = Path(__file__).parent
        return str(script_dir / "api_keys.json")

    def load_config(self):
        """Load API configuration from file or environment"""
        # Try loading from config file
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                    self.google_accounts = config.get('google_accounts', [])
                    self.fallback_apis = config.get('fallback', {})
                    print(f"[OK] Loaded config from: {self.config_path}")
                    print(f"  Google accounts: {len(self.google_accounts)}")
                    return
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")

        # Fallback to environment variables
        self._load_from_env()

    def _load_from_env(self):
        """Load API keys from environment variables"""
        env_keys = []

        # Look for GOOGLE_API_KEY_1, GOOGLE_API_KEY_2, etc.
        for i in range(1, 10):
            key = os.getenv(f'GOOGLE_API_KEY_{i}')
            if key:
                env_keys.append({
                    'name': f'Account {i} (from env)',
                    'api_key': key,
                    'daily_limit': 50
                })

        # Also check single GOOGLE_API_KEY
        single_key = os.getenv('GOOGLE_API_KEY')
        if single_key and not env_keys:
            env_keys.append({
                'name': 'Account 1 (from env)',
                'api_key': single_key,
                'daily_limit': 50
            })

        if env_keys:
            self.google_accounts = env_keys
            print(f"[OK] Loaded {len(env_keys)} API key(s) from environment variables")
        else:
            print("[!] No API keys found in config file or environment")
            print("    Please set up api_keys.json or environment variables")

    def add_cli_keys(self, keys_string: str):
        """Add API keys from command line parameter"""
        if not keys_string:
            return

        keys = [k.strip() for k in keys_string.split(',') if k.strip()]
        for i, key in enumerate(keys, 1):
            self.google_accounts.append({
                'name': f'Account {i} (CLI)',
                'api_key': key,
                'daily_limit': 50
            })

        print(f"[OK] Added {len(keys)} API key(s) from command line")

    def get_google_accounts(self) -> List[Dict]:
        """Get all configured Google API accounts"""
        return self.google_accounts

    def has_google_accounts(self) -> bool:
        """Check if any Google accounts are configured"""
        return len(self.google_accounts) > 0

    def get_fallback_api(self, service: str) -> Optional[str]:
        """Get fallback API key for service (dalle, stability, etc.)"""
        return self.fallback_apis.get(f'{service}_key')

    def create_example_config(self, output_path: Optional[str] = None):
        """Create example configuration file"""
        output_path = output_path or self.config_path

        example_config = {
            "google_accounts": [
                {
                    "name": "Account 1 (work)",
                    "api_key": "AIzaSy... (replace with your key)",
                    "daily_limit": 50,
                    "notes": "Primary account"
                },
                {
                    "name": "Account 2 (personal)",
                    "api_key": "AIzaSy... (replace with your key)",
                    "daily_limit": 50,
                    "notes": "Backup account"
                },
                {
                    "name": "Account 3 (backup)",
                    "api_key": "AIzaSy... (replace with your key)",
                    "daily_limit": 50,
                    "notes": "Emergency backup"
                }
            ],
            "fallback": {
                "dalle_key": "sk-... (optional OpenAI key)",
                "stability_key": "sk-... (optional Stability AI key)",
                "notes": "Fallback APIs if Google quota exhausted"
            }
        }

        with open(output_path, 'w') as f:
            json.dump(example_config, f, indent=2)

        print(f"[OK] Created example config: {output_path}")
        print(f"  Edit this file and add your API keys")

    def validate(self) -> bool:
        """Validate configuration"""
        if not self.has_google_accounts():
            print("[!] No Google API keys configured!")
            print("\nSetup options:")
            print("  1. Create config file:")
            print("     python -c \"from config_manager import APIConfig; APIConfig().create_example_config()\"")
            print("  2. Set environment variable:")
            print("     set GOOGLE_API_KEY=your_key_here")
            print("  3. Use --api-keys parameter:")
            print("     python slide_redesigner.py presentation.pptx --api-keys key1,key2")
            return False

        # Validate keys format (basic check)
        for account in self.google_accounts:
            if not account.get('api_key'):
                print(f"[!] Account '{account.get('name')}' has no API key")
                return False

        print(f"[OK] Configuration valid: {len(self.google_accounts)} account(s)")
        return True


def main():
    """Test configuration manager"""
    config = APIConfig()

    if not os.path.exists(config.config_path):
        print("No config file found. Creating example...")
        config.create_example_config()
    else:
        config.validate()
        print(f"\nConfigured accounts:")
        for i, account in enumerate(config.get_google_accounts(), 1):
            print(f"  {i}. {account['name']}")
            print(f"     Limit: {account.get('daily_limit', 50)} requests/day")


if __name__ == "__main__":
    main()
