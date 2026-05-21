# Solace Automated Walkthrough Recorder

An automated, human-like browser recording engine built with Python and Playwright. This system interacts dynamically with the Solace Web App, executes a comprehensive user journey (mood assessment, AI triage, interactive chat, and local data storage validation), and records the session into a clean, high-fidelity demo video.

## How it Works Under the Hood

The execution sequence is entirely deterministic yet mimics authentic human interactions to capture an organic-looking application demonstration:

```
[Launch Headless Chromium] ──> [Apply Browser Fingerprint Masking]
              │
              ▼
[Click "Anxious" Button] ──> [Type Scenario Context (Delayed Keystrokes)]
              │
              ▼
[Trigger OpenRouter Triage Flow] ──> [Read Assessment (7-9s Camera Breather)]
              │
              ▼
[Transition to Companion Chat] ──> [Send Follow-up Dialogue via SVG Locator]
              │
              ▼
[Toggle "Journal" History View] ──> [Finalize & Compile Output Video File]
```

## Technical Features

**Native Screen Capture**  
Utilizes Playwright's system-level context recording layer to output high-fidelity layout sessions directly to standard `.webm` media files.

**Keystroke & Velocity Emulation**  
Injects arbitrary, randomized delays (80ms - 140ms) between separate character keystrokes to break machine-like uniform typing patterns.

**Stealth Engine Integration**  
Leverages Object-Oriented browser context hooks to spoof navigator properties, preventing automated bot mitigation filters from flagging or blocking the connection.

**Network-Idle Syncing**  
Dynamically hooks into browser transport streams (networkidle) to pause actions until framework asynchronous hydration routines and OpenRouter API endpoints resolve.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Linux Core UI Packages (if running inside cloud containers or environments like GitHub Codespaces)

### 1. Installation Setup

Navigate to your workspace directory and install the orchestration engine dependencies along with the core browser binaries:

```bash
# Create and move to workspace
mkdir solace-recorder && cd solace-recorder

# Install modern automation core and stealth abstractions
pip install playwright playwright-stealth

# Provision isolated testing web browser bundles
playwright install chromium
```

> [!IMPORTANT]  
> If you are deploying or running this engine inside an unheaded cloud runtime environment (like GitHub Codespaces or Docker containers), you must provision the missing host operating system graphical libraries before running:
> 
> ```bash
> sudo playwright install-deps
> ```

### 2. File Architecture

Ensure your automation folder mirrors this modular layout:

```
solace-recorder/
├── record_solace.py    # Main automation script execution logic
└── videos/             # Automatically generated runtime output directory
    └── *.webm          # Compiled demonstration video recordings
```

## Configuration & Customization

If the core layout or structural workflow of the primary application changes, use the following code locations inside `record_solace.py` to adapt the engine:

### Adjusting Target Selectors

The interaction layer hooks directly into text layers and structural HTML components:

- **Landing Grid**: `page.locator('button:has-text("Anxious")')` - targeted text strings can be modified to evaluate other emotion components ("Sad", "Angry", "Stressed").

- **Main Form Field**: Matches on fuzzy placeholder constraints: `textarea[placeholder*="Or tell me in your own words"]`.

- **Icon-Only Elements**: Elements containing no accessible text layers (like the chat dispatch action button) are targeted using relative DOM structure indexing matching: `locator('button:has(svg)').last`.

### Adjusting Video Cadence

To control visual retention lengths for production reviews or presentation decks, modify the pacing wrappers:

Increase the `sleep` constants inside `human_delay(7.0, 9.0)` right after data submissions to give target audiences more time to read AI-generated summary panels on screen.

## Execution Manual

Run the automation module from the root directory of your workspace terminal:

```bash
python record_solace.py
```

### Expected Output Logs

```
🎬 Step 1: Opening Solace Landing Page...
🎯 Clicking the 'Anxious' quick feeling button...
✍️ Appending human-like context to the journaling textarea...
🧠 Submitting entry to trigger OpenRouter AI triage flow...
Waiting for AI assessment panel to render completely...
💬 Advancing into the empathy companion chat view...
💬 Typing a follow-up response inside the chat interface...
🚀 Dispatching message via the SVG action locator...
📓 Transitioning views to display local storage journal metrics...

🎉 Capture Complete! Your high-fidelity production video is saved here: videos/xxxx.webm
```

## Project Structure

This repository contains the automated recording system for creating high-quality demo videos of the Solace application workflow. The system handles:

- ✅ Authentication and browser initialization
- ✅ User journey simulation with realistic timings
- ✅ AI triage flow integration
- ✅ Video capture and compilation
- ✅ Local storage validation

## License

See LICENSE file for details.

## Support

For issues or questions about the recorder, please refer to the documentation above or check the `record_solace.py` source code for implementation details.