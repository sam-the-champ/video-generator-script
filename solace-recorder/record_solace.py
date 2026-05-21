import asyncio
import random
import os
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

# Create standard output directory for your recorded asset
os.makedirs("videos", exist_ok=True)

async def human_delay(min_sec=1.5, max_sec=3.5):
    """Introduces a realistic pause to match user thinking or reading speeds."""
    await asyncio.sleep(random.uniform(min_sec, max_sec))

async def main():
    # Use the updated v2.x Playwright Stealth async wrapper
    async with Stealth().use_async(async_playwright()) as p:
        # slow_mo paces browser actions seamlessly so the resulting video is smooth and clear
        browser = await p.chromium.launch(headless=True, slow_mo=60)
        
        # Capture clean 720p HD layout resolution
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            record_video_dir="videos/",
            record_video_size={'width': 1280, 'height': 720}
        )
        
        page = await context.new_page()
        
        try:
            print("🎬 Step 1: Opening Solace Landing Page...")
            await page.goto("https://slcai-sm9m.vercel.app/")
            await page.wait_for_load_state("networkidle")
            await human_delay(2.5, 4.0) # Let the landing screen settle on camera

            # --- SELECT MOOD BUTTON ---
            print("🎯 Clicking the 'Anxious' quick feeling button...")
            anxious_btn = page.locator('button:has-text("Anxious")').first
            await anxious_btn.hover()
            await human_delay(0.5, 1.0)
            await anxious_btn.click()
            await human_delay(1.0, 2.0)

            # --- TYPE IN THE MAIN JOURNAL TEXTAREA ---
            print("✍️ Appending human-like context to the journaling textarea...")
            journal_input = page.locator('textarea[placeholder*="Or tell me in your own words"]').first
            await journal_input.click()
            await human_delay(0.5, 1.0)
            
            # Additional conversational context to add to the quick button text
            sample_story = (
                " I have this massive deadline tomorrow, and I feel stuck. "
                "Every time I look at my task list, my chest gets tight."
            )
            # Type character-by-character at normal human pacing (80-140ms per key)
            await journal_input.type(sample_story, delay=random.randint(80, 140))
            await human_delay(2.0, 3.0)

            # --- SUBMIT FOR AI TRIAGE ---
            print("🧠 Submitting entry to trigger OpenRouter AI triage flow...")
            submit_btn = page.locator('button:has-text("Talk to Solace →")').first
            await submit_btn.hover()
            await human_delay(0.3, 0.7)
            await submit_btn.click()
            
            # Generous pause for OpenRouter API to fetch triage level, summary, and strategies
            print("Waiting for AI assessment panel to render completely...")
            await page.wait_for_load_state("networkidle")
            await human_delay(7.0, 9.0) # Gives video viewers time to read the AI summary

            # --- TRANSITION TO COMPANION CHAT ---
            print("💬 Advancing into the empathy companion chat view...")
            keep_talking_btn = page.locator('button:has-text("Keep talking →")').first
            await keep_talking_btn.hover()
            await human_delay(0.4, 0.8)
            await keep_talking_btn.click()
            await human_delay(2.0, 3.0)

            # --- CHAT INTERACTION ---
            print("💬 Typing a follow-up response inside the chat interface...")
            chat_input = page.locator('textarea[placeholder*="Type or speak"]').first
            await chat_input.click()
            await human_delay(0.5, 1.0)
            
            follow_up_msg = "Those strategies make a lot of sense. How can I start breaking down my milestone into tiny parts?"
            await chat_input.type(follow_up_msg, delay=random.randint(80, 130))
            await human_delay(1.5, 2.5)

            # Locates the circular button containing your arrow icon inside the chat container
            print("🚀 Dispatching message via the SVG action locator...")
            send_btn = page.locator('div[class*="chat"], footer, main').locator('button:has(svg)').last
            await send_btn.hover()
            await human_delay(0.2, 0.5)
            await send_btn.click()
            
            # Wait for conversational companion to generate its response parameters
            await page.wait_for_load_state("networkidle")
            await human_delay(7.0, 9.0) # Time to read the chat dialogue on stream

            # --- LOCAL JOURNAL VIEW ---
            print("📓 Transitioning views to display local storage journal metrics...")
            journal_toggle = page.locator('button:has-text("Journal")').first
            await journal_toggle.hover()
            await human_delay(0.6, 1.2)
            await journal_toggle.click()
            
            # Hold view on the journal entries lists so the dashboard saves cleanly
            await human_delay(4.0, 6.0)

        except Exception as e:
            print(f"⚠️ Operational warning encountered during playback: {e}")
            
        finally:
            # Safely finalize and export the video stream configuration
            video_path = await page.video.path()
            await context.close()
            await browser.close()
            print(f"\n🎉 Capture Complete! Your high-fidelity production video is saved here: {video_path}")

if __name__ == "__main__":
    asyncio.run(main())