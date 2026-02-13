# Google Gemini API Setup Guide

## Step 1: Get API Keys

### Option A: Google AI Studio (Recommended - Free Tier)

1. **Visit:** https://aistudio.google.com/app/apikey
2. **Sign in** with your Google account
3. **Click:** "Create API Key"
4. **Select:** Your Google Cloud project (or create new)
5. **Copy** the API key (starts with `AIza...`)

**Free Tier Limits:**
- 50 requests per day per API key
- Perfect for testing and moderate use

### Option B: Google Cloud Console (Production)

1. **Visit:** https://console.cloud.google.com/
2. **Create/Select** a project
3. **Enable API:** "Generative Language API"
4. **Create credentials:** API Key
5. **Copy** the API key

## Step 2: Install Required Package

```bash
pip install google-generativeai
```

## Step 3: Configure API Keys

Create `api_keys.json` in `_video_automation/` folder:

```json
{
  "google_accounts": [
    {
      "name": "Account 1",
      "api_key": "AIza_YOUR_FIRST_API_KEY_HERE",
      "daily_limit": 50,
      "enabled": true
    },
    {
      "name": "Account 2",
      "api_key": "AIza_YOUR_SECOND_API_KEY_HERE",
      "daily_limit": 50,
      "enabled": true
    },
    {
      "name": "Account 3",
      "api_key": "AIza_YOUR_THIRD_API_KEY_HERE",
      "daily_limit": 50,
      "enabled": true
    }
  ]
}
```

**Multi-Account Benefits:**
- 3 accounts = 150 images/day
- Automatic failover if one account hits limit
- Production-ready capacity

## Step 4: Test API Connection

```bash
python -c "import google.generativeai as genai; genai.configure(api_key='YOUR_API_KEY'); print('API Connected!')"
```

## Step 5: Run Image Generation

### Test with Single Slide:
```bash
cd _video_automation
python slide_redesigner_v2.py your_presentation.pptx --plan-only
python slide_redesigner_v2.py your_presentation.pptx --generate --api-keys YOUR_API_KEY
```

### Full Pipeline:
```bash
python slide_redesigner_v2.py your_presentation.pptx --all --config api_keys.json --brand snowbrix
```

## Pricing & Limits

### Free Tier (Google AI Studio):
- **Cost:** $0
- **Limit:** 50 images/day per account
- **Best for:** Testing, personal projects, moderate use

### Paid Tier (Google Cloud):
- **Cost:** ~$0.04 per image (Imagen 3)
- **Limit:** No daily limit (pay per use)
- **Best for:** Production, high-volume

## Troubleshooting

### Error: "quota exceeded"
- **Solution:** System auto-switches to next account
- **Action:** Add more accounts or wait 24 hours

### Error: "API key not valid"
- **Check:** API key copied correctly (no spaces)
- **Verify:** API enabled in Google Cloud Console

### Error: "safety filter blocked"
- **Cause:** Content policy violation
- **Solution:** Adjust prompt to be less specific about people/brands

## File Structure

```
_video_automation/
├── api_keys.json              ← Your API keys (DO NOT commit to git!)
├── api_manager.py             ← Multi-account management
├── image_generator.py         ← Imagen API integration
├── prompt_generator.py        ← Snowbrix-themed prompts
└── slide_redesigner_v2.py     ← Main orchestration
```

## Security Best Practices

1. **Never commit** `api_keys.json` to git
2. **Add to .gitignore:** `api_keys.json`
3. **Rotate keys** periodically
4. **Use separate keys** for dev/prod

## Next Steps

After setup:
1. Generate prompts: `--plan-only`
2. Review prompts in `_projects/[name]/image_prompts/`
3. Generate images: `--generate`
4. Create slides: `--create-slides`
5. Or run all: `--all`

---

**Ready to generate beautiful Snowbrix-branded slides!** 🎨
