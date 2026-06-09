import asyncio
import random
import os
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

# Ensure output directory for recorded demo assets exists
os.makedirs("videos", exist_ok=True)

async def human_delay(min_sec=1.5, max_sec=3.0):
    """Introduces natural pacing delays so the compiled video matches true human playback speed."""
    await asyncio.sleep(random.uniform(min_sec, max_sec))

async def main():
    async with Stealth().use_async(async_playwright()) as p:
        # Run in headless mode to guarantee zero window server crashes inside cloud runtimes/Codespaces
        browser = await p.chromium.launch(headless=True, slow_mo=60)
        
        # Capture a clean 720p HD frame aspect ratio layout
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            record_video_dir="videos/",
            record_video_size={'width': 1280, 'height': 720}
        )
        
        page = await context.new_page()
        
        try:
            # -------------------------------------------------------------
            # PHASE 1: INITIALIZE SEQUENCE & TITLE SCREEN
            # -------------------------------------------------------------
            print("🎬 Step 1: Navigating to Turing Game Portal...")
            # Automatically matching your new Vercel deployment endpoint
            await page.goto("https://turing-game-three.vercel.app/")
            await page.wait_for_load_state("networkidle")
            await human_delay(2.5, 4.0)

            print("🟢 Initiating Sequence... Handshaking game engine core...")
            start_btn = page.locator('button.start-btn, button:has-text("INITIATE SEQUENCE")').first
            await start_btn.hover()
            await human_delay(0.5, 1.0)
            await start_btn.click()
            await human_delay(2.0, 3.0)

            # -------------------------------------------------------------
            # PHASE 2: SOLVING CAESAR CIPHERS (CHAPTERS 1-3)
            # -------------------------------------------------------------
            # PUZZLE 1 (Shift 3)
            print("🧩 Chapter 1: Decoding Cipher Shift 3...")
            p1_input = page.locator('input.terminal-input, #decode-input').first
            await p1_input.click()
            # Text transformation to uppercase is handled by the UI automatically
            await p1_input.type("WHERE IS THE BOMB, THERE IS THE MIND.", delay=random.randint(60, 110))
            await human_delay(1.0, 2.0)
            await p1_input.press("Enter")
            await human_delay(2.5, 3.5)

            # PUZZLE 2 (Shift 7)
            print("🧩 Chapter 2: Decoding Cipher Shift 7...")
            p2_input = page.locator('input.terminal-input, #decode-input').first
            await p2_input.click()
            await p2_input.type("THE MACHINE CHALLENGES YOU. PROBE IT BEAUTIFULLY.", delay=random.randint(60, 110))
            await human_delay(1.0, 2.0)
            await p2_input.press("Enter")
            await human_delay(2.5, 3.5)

            # PUZZLE 3 (Shift 13 / ROT13)
            print("🧩 Chapter 3: Decoding Cipher Shift 13...")
            p3_input = page.locator('input.terminal-input, #decode-input').first
            await p3_input.click()
            await p3_input.type("I LOVED THE UNBORN WORLD BECAUSE IT WAS BEAUTIFUL.", delay=random.randint(60, 110))
            await human_delay(1.0, 2.0)
            await p3_input.press("Enter")
            # Extra buffer time for the screen view engine to morph into the Chapter 4 Inverted Test layout
            await human_delay(3.5, 5.0)

            # -------------------------------------------------------------
            # PHASE 3: INVERTED TURING TEST CHAT (CHAPTER 4)
            # -------------------------------------------------------------
            print("🤖 Chapter 4: Entering Inverted Turing Test Space...")
            
            # Crafting 2 distinct, highly existential human strings targeting your score logic:
            # Requires personal pronouns ("I"), emotional words ("grief", "dream"), and imperfections ("hmm", "well")
            human_responses = [
                "Honestly... I feel a profound sense of grief sometimes when I dream about what is lost. Hmm, do you?",
                "Well, perhaps my mistakes are what define me. I don't know, pain and love aren't equations to resolve."
            ]

            for turn_idx, response_text in enumerate(human_responses):
                print(f"💬 Conversing with Machine Intelligence — Turn {turn_idx + 1}/5...")
                
                # Dynamic hook targeting your chat layout inputs
                chat_field = page.locator('input.chat-input, #chat-input').first
                await chat_field.wait_for(state="visible", timeout=10000)
                await chat_field.click()
                await human_delay(0.5, 1.2)
                
                # Type response with natural variations mimicking reflection
                await chat_field.type(response_text, delay=random.randint(70, 120))
                await human_delay(1.0, 2.0)
                
                # Dispatch response via the transmit button locator string hooks
                send_btn = page.locator('button.chat-send, #chat-send').first
                await send_btn.hover()
                await send_btn.click()
                
                print("Waiting for Claude API context processing handshake...")
                # Allow ample time for the Anthropic endpoint to hydrate message arrays on screen
                await page.wait_for_load_state("networkidle")
                await human_delay(6.5, 8.5)

            # -------------------------------------------------------------
            # PHASE 4: END EVALUATION & VERDICT CAPTURE
            # -------------------------------------------------------------
            print("📊 Tracking system metrics transition to verdict view container...")
            # Matches your target tracking rule: #screen-end.active 
            end_screen = page.locator('#screen-end.active, #screen-end')
            await end_screen.wait_for(state="visible", timeout=45000)
            
            # Generous camera breather at the end screen so viewers can read final stats and philosophical quote
            print("🎉 Displaying Ending Verdict Screen successfully.")
            await human_delay(8.0, 10.0)

        except Exception as e:
            print(f"⚠️ Operation sequence halted due to an interaction anomaly: {e}")
            
        finally:
            # Finalize stream frames matrix and save the video container
            video_path = await page.video.path()
            await context.close()
            await browser.close()
            print(f"\n🎉 Capture Complete! High-fidelity video walkthrough saved to: {video_path}")

if __name__ == "__main__":
    asyncio.run(main())
