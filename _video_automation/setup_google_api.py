"""
Google API Setup Helper
Quick setup wizard for configuring Google Gemini API
"""

import json
from pathlib import Path
import sys

def create_api_config():
    """Interactive setup for Google API keys"""

    print("="*70)
    print("GOOGLE GEMINI API SETUP WIZARD")
    print("="*70)
    print()
    print("This wizard will help you configure Google Gemini API for image generation.")
    print()

    # Check if config already exists
    config_file = Path("api_keys.json")
    if config_file.exists():
        print("[!] api_keys.json already exists!")
        response = input("Overwrite? (yes/no): ").lower()
        if response != 'yes':
            print("Setup cancelled.")
            return
        print()

    accounts = []

    print("How many Google accounts do you have API keys for?")
    print("(Recommended: 3 accounts = 150 images/day)")
    print()

    while True:
        try:
            num_accounts = int(input("Number of accounts (1-10): "))
            if 1 <= num_accounts <= 10:
                break
            print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a valid number")

    print()
    print("-"*70)
    print()

    for i in range(num_accounts):
        print(f"ACCOUNT {i+1} of {num_accounts}")
        print("-"*70)

        # Account name
        name = input(f"Account name (e.g., 'Personal', 'Work'): ").strip()
        if not name:
            name = f"Account {i+1}"

        # API key
        while True:
            api_key = input("API key (starts with 'AIza'): ").strip()
            if api_key.startswith("AIza") and len(api_key) > 20:
                break
            print("[!] Invalid API key format. Should start with 'AIza' and be longer.")

        # Daily limit
        print("Daily limit (default: 50 for free tier)")
        limit_input = input("Daily limit [50]: ").strip()
        daily_limit = int(limit_input) if limit_input else 50

        # Enabled
        enabled = True

        accounts.append({
            "name": name,
            "api_key": api_key,
            "daily_limit": daily_limit,
            "enabled": enabled
        })

        print(f"[OK] {name} configured")
        print()

    # Create config
    config = {
        "google_accounts": accounts
    }

    # Save to file
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)

    print("="*70)
    print("[OK] Configuration saved to api_keys.json")
    print("="*70)
    print()
    print("Summary:")
    print(f"  Total accounts: {len(accounts)}")
    print(f"  Daily capacity: {sum(a['daily_limit'] for a in accounts)} images")
    print()
    print("Next steps:")
    print("  1. Test API: python test_google_api.py")
    print("  2. Generate images: python slide_redesigner_v2.py [file] --generate")
    print("  3. Full pipeline: python slide_redesigner_v2.py [file] --all")
    print()
    print("IMPORTANT: Add api_keys.json to .gitignore to keep keys private!")
    print()

def test_api_connection():
    """Test if Google API is accessible"""
    print("\nTesting Google API connection...")

    try:
        import google.generativeai as genai
        print("[OK] google-generativeai package installed")
    except ImportError:
        print("[!] Package not installed. Run: pip install google-generativeai")
        return False

    config_file = Path("api_keys.json")
    if not config_file.exists():
        print("[!] api_keys.json not found. Run setup first.")
        return False

    with open(config_file) as f:
        config = json.load(f)

    if not config.get('google_accounts'):
        print("[!] No accounts configured")
        return False

    account = config['google_accounts'][0]
    api_key = account['api_key']

    try:
        genai.configure(api_key=api_key)
        # Try to list models to verify connection
        models = genai.list_models()
        print(f"[OK] API connected successfully!")
        print(f"[OK] Account: {account['name']}")
        return True
    except Exception as e:
        print(f"[!] API connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_api_connection()
    else:
        create_api_config()
        print("\nWould you like to test the connection now? (yes/no): ", end='')
        if input().lower() == 'yes':
            test_api_connection()
