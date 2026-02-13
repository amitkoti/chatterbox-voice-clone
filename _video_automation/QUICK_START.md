# Quick Start Guide
## Automated Slide Redesigner with Inventory System

---

## Setup (One-Time)

### 1. Install Dependencies
```bash
pip install python-pptx google-generativeai pillow
```

### 2. Configure API Keys

**Option A: Config File** (Recommended)
```bash
# Copy example config
copy api_keys.example.json api_keys.json

# Edit api_keys.json and add your Google AI Studio API keys
# Get keys from: https://aistudio.google.com/apikey
```

**Option B: Environment Variables**
```bash
set GOOGLE_API_KEY_1=your_first_key_here
set GOOGLE_API_KEY_2=your_second_key_here
set GOOGLE_API_KEY_3=your_third_key_here
```

**Option C: Command Line**
```bash
python slide_redesigner_v2.py presentation.pptx --generate --api-keys key1,key2,key3
```

---

## Basic Usage

### Quick Start (All-in-One)
```bash
python slide_redesigner_v2.py my_presentation.pptx --all
```

This runs all 3 stages:
1. Generate prompts
2. Generate images
3. Create redesigned presentation

---

## Production Workflow (Inventory Building)

### Stage 1: Build Prompt Inventory
Generate prompts for multiple presentations:

```bash
python slide_redesigner_v2.py deck1.pptx --plan-only
python slide_redesigner_v2.py deck2.pptx --plan-only
python slide_redesigner_v2.py deck3.pptx --plan-only
```

**Output:** Prompts saved to `_projects/[name]/image_prompts/`

**Review prompts:**
- Open `_projects/deck1/image_prompts/` folder
- Edit `.txt` files if needed
- Customize prompts for better results

---

### Stage 2: Build Image Inventory

**Option A: Auto-Generate (uses API)**
```bash
python slide_redesigner_v2.py deck1.pptx --generate
```

**Option B: Manual Generation (your choice of tools)**
1. Read prompt from `_projects/deck1/image_prompts/slide_01_title.txt`
2. Generate image using:
   - Google AI Studio (manual interface)
   - DALL-E
   - Midjourney
   - Any image tool
3. Save as `_projects/deck1/images/slide_01.png`
4. Repeat for important slides

**Option C: Hybrid (manual + auto)**
1. Manually create 5-10 key images
2. Run auto-generate for the rest:
   ```bash
   python slide_redesigner_v2.py deck1.pptx --generate
   ```
   (Skips slides with existing images)

**Multi-Account Power:**
```bash
# Uses all configured accounts automatically
# Account 1: 50 images
# Account 2: 50 images
# Account 3: 50 images
# Total: 150 images in one run!
```

---

### Stage 3: Build Slide Inventory
```bash
python slide_redesigner_v2.py deck1.pptx --create-slides
```

**Output:** `_projects/deck1/deck1_redesigned.pptx`

---

### Stage 4: Build Audio Inventory
```bash
python video_creator.py _projects/deck1/deck1_redesigned.pptx --audio-only
```

Run on multiple idle systems:
- **System A:** `deck1 --audio-only`
- **System B:** `deck2 --audio-only`
- **System C:** `deck3 --audio-only`

All complete in ~20 minutes (parallel)

---

### Stage 5: Build Video Inventory
```bash
python video_creator.py _projects/deck1/deck1_redesigned.pptx --use-existing-audio
```

Fast! Only 1-2 minutes per video.

---

## Inventory Management

### View Dashboard
```bash
python slide_redesigner_v2.py --inventory-status
```

**Shows:**
- All projects and their status
- Progress bars
- Next actions needed
- API quota status

**Example Output:**
```
╔══════════════════════════════════════════════════════╗
║        PRODUCTION INVENTORY DASHBOARD                ║
╚══════════════════════════════════════════════════════╝

📝 PROMPTS READY
┌──────────────────────────────────────────────────────┐
│ deck1
│   [████████████████████] 100%
│   Prompts: 18/18
│   → Next: Generate images
└──────────────────────────────────────────────────────┘

🎨 IMAGES READY
┌──────────────────────────────────────────────────────┐
│ deck2
│   [████████████████████] 100%
│   Prompts: 20/20 | Images: 20/20
│   → Next: Create slides
└──────────────────────────────────────────────────────┘

✅ VIDEOS COMPLETE
┌──────────────────────────────────────────────────────┐
│ deck3
│   [████████████████████] 100%
│   All stages complete!
└──────────────────────────────────────────────────────┘
```

---

## Typical Day

### Morning: Add to Inventory
```bash
# Add 5 presentations to prompt inventory (2 minutes)
python slide_redesigner_v2.py pres1.pptx --plan-only
python slide_redesigner_v2.py pres2.pptx --plan-only
python slide_redesigner_v2.py pres3.pptx --plan-only
python slide_redesigner_v2.py pres4.pptx --plan-only
python slide_redesigner_v2.py pres5.pptx --plan-only
```

### Afternoon: Generate Images
```bash
# Review prompts (10 minutes)
# Edit any prompts that need tweaking

# Generate images for all (auto-detects pending work)
python slide_redesigner_v2.py pres1.pptx --generate
python slide_redesigner_v2.py pres2.pptx --generate
# ... uses 150 quota across 3 accounts
```

### Evening: Create Slides & Audio
```bash
# Create presentations (5 minutes total)
python slide_redesigner_v2.py pres1.pptx --create-slides
python slide_redesigner_v2.py pres2.pptx --create-slides

# Start audio generation on idle systems (overnight)
# System A: pres1 --audio-only
# System B: pres2 --audio-only
```

### Next Morning: Create Videos
```bash
# Assemble videos (5 minutes total)
python video_creator.py ...redesigned.pptx --use-existing-audio
python video_creator.py ...redesigned.pptx --use-existing-audio

# Upload to YouTube!
```

---

## Tips & Tricks

### Maximize Production

**Use All 3 Accounts:**
- 3 accounts × 50 requests/day = 150 images/day
- Can produce 5-10 complete presentations daily

**Review Prompts First:**
- Spend 10 minutes editing prompts
- Better prompts = better images
- Saves regeneration time

**Manual + Auto Mix:**
- Manually create 3-5 hero images (title, key concepts)
- Auto-generate the rest
- Best of both worlds

**Parallel Audio:**
- Use 3-5 idle systems for audio
- 5 systems = 5 presentations in 20 minutes
- vs. 100 minutes sequential

### Check Status Anytime
```bash
# See full inventory
python slide_redesigner_v2.py --inventory-status

# See API quota
python -c "from api_manager import *; from config_manager import *; c=APIConfig(); m=MultiAccountAPIManager(c.get_google_accounts()); print(m.get_status_summary())"
```

### Resume After Interruption
Everything is saved automatically:
- Prompts: Persistent files
- Images: Saved to disk
- API usage: Tracked in `.api_state.json`
- Inventory: Tracked in `inventory.json`

Just run the next stage command and it continues where you left off.

---

## Troubleshooting

### "No API keys configured"
**Fix:** Set up api_keys.json or environment variables

### "All API accounts exhausted"
**Fix:**
- Wait until tomorrow (quota resets)
- Or manually generate remaining images
- Or add more Google accounts

### "Images not found"
**Fix:** Run `--generate` before `--create-slides`

### "Prompts not found"
**Fix:** Run `--plan-only` first

### Check inventory status
```bash
python slide_redesigner_v2.py --inventory-status
```
Shows exactly what's ready and what's missing.

---

## File Structure

```
_projects/
└── my_presentation/
    ├── image_prompts/              # Stage 1 output
    │   ├── slide_01_title.txt
    │   ├── slide_02_comparison.txt
    │   └── ...
    │
    ├── images/                     # Stage 2 output
    │   ├── slide_01.png           # Auto or manual
    │   ├── slide_02.png
    │   └── ...
    │
    ├── my_presentation_redesigned.pptx  # Stage 3 output
    │
    └── output/                     # Stage 4-5 output
        ├── slide_01_audio.wav     # Audio files
        ├── slide_02_audio.wav
        └── final_video.mp4        # Final video
```

---

## Next Steps

1. **Set up API keys** (see Setup section)
2. **Try the quick start** with a test presentation
3. **Review the output** and adjust prompts
4. **Scale up** to your production workflow
5. **Check inventory** regularly to track progress

---

## Getting Help

- Check `--help` for any command
- View inventory status for current state
- Read error messages carefully
- Check that all stages completed in order

Happy automating! 🚀
