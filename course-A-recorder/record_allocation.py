import asyncio
import random
import os
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

# Ensure video storage target directory exists
os.makedirs("videos", exist_ok=True)

async def human_delay(min_sec=1.5, max_sec=3.0):
    """Introduces natural pacing to make video presentation watchable and authentic."""
    await asyncio.sleep(random.uniform(min_sec, max_sec))

async def main():
    async with Stealth().use_async(async_playwright()) as p:
        # Running in headless=True mode to guarantee stable context execution in GitHub Codespaces
        browser = await p.chromium.launch(headless=True, slow_mo=65)
        
        # Capture crisp 720p HD resolution 
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            record_video_dir="videos/",
            record_video_size={'width': 1280, 'height': 720}
        )
        
        page = await context.new_page()
        
        try:
            # -------------------------------------------------------------
            # PHASE 1: ADMIN AUTHENTICATION
            # -------------------------------------------------------------
            print("🎬 Step 1: Navigating to Course Allocation Portal...")
            await page.goto("https://ca-app-sandy.vercel.app/")
            await page.wait_for_load_state("networkidle")
            await human_delay(2.0, 3.5)

            print("⚙️ Logging in as System Administrator...")
            await page.locator('input[name="username"]').click()
            await page.locator('input[name="username"]').type("admin", delay=random.randint(70, 130))
            await human_delay(0.5, 1.0)
            
            await page.locator('input[name="password"]').click()
            await page.locator('input[name="password"]').type("😭😭😭", delay=random.randint(70, 130))
            await human_delay(0.8, 1.5)

            login_btn = page.locator('button:has-text("Sign In")').first
            await login_btn.hover()
            await login_btn.click()
            
            await page.wait_for_load_state("networkidle")
            print("Successfully entered Admin Dashboard View.")
            await human_delay(3.0, 4.5)

            # -------------------------------------------------------------
            # PHASE 2: CREATING A LECTURER
            # -------------------------------------------------------------
            print("👤 Transitioning to Lecturers Panel...")
            await page.locator('a:has-text("Lecturers")').first.click()
            await page.wait_for_load_state("networkidle")
            await human_delay(2.0, 3.0)

            print("➕ Launching Add Lecturer Modal...")
            await page.locator('button:has-text("+ Add Lecturer")').first.click()
            await human_delay(1.0, 1.8)

            print("✍️ Filling Lecturer credentials details...")
            await page.locator('input[name="lecturerId"]').type("LEC/777", delay=random.randint(70, 120))
            await page.locator('select[name="title"]').select_option("Dr")
            await page.locator('input[name="firstname"]').type("Charles", delay=random.randint(70, 120))
            await page.locator('input[name="surname"]').type("SMITH", delay=random.randint(70, 120))  # Force uppercase per instructions
            await page.locator('input[name="email"]').type("charles.smith@academy.edu", delay=random.randint(70, 120))
            await page.locator('input[name="department"]').type("Computer Science", delay=random.randint(70, 120))
            await page.locator('select[name="gender"]').select_option("Male")
            await human_delay(1.5, 2.5)

            print("💾 Saving newly created Lecturer context...")
            await page.locator('.modal-actions button:has-text("Add Lecturer")').click()
            await page.wait_for_load_state("networkidle")
            await human_delay(3.0, 4.0)

            # -------------------------------------------------------------
            # PHASE 3: CREATING A COURSE
            # -------------------------------------------------------------
            print("📚 Transitioning to Courses Panel...")
            await page.locator('a:has-text("Courses")').first.click()
            await page.wait_for_load_state("networkidle")
            await human_delay(2.0, 3.0)

            print("➕ Launching Add Course Modal...")
            await page.locator('button:has-text("+ Add Course")').first.click()
            await human_delay(1.0, 1.8)

            print("✍️ Registering course mapping rules...")
            await page.locator('input[name="courseCode"]').type("CSC301", delay=random.randint(70, 120))
            await page.locator('input[name="courseTitle"]').type("Advanced Data Structures", delay=random.randint(70, 120))
            await page.locator('select[name="semester"]').select_option("First")
            await page.locator('input[name="unit"]').type("4", delay=random.randint(70, 120))
            await human_delay(1.5, 2.5)

            print("💾 Saving Course structural definition...")
            await page.locator('.modal-actions button:has-text("Add Course")').click()
            await page.wait_for_load_state("networkidle")
            await human_delay(3.0, 4.0)

            # -------------------------------------------------------------
            # PHASE 4: COURSE ALLOCATION FLOW
            # -------------------------------------------------------------
            print("🗂 Transitioning to Allocations Management Panel...")
            await page.locator('a:has-text("Allocations")').first.click()
            await page.wait_for_load_state("networkidle")
            await human_delay(2.0, 3.0)

            print("➕ Launching Allocation Assignment Modal...")
            await page.locator('button:has-text("+ Allocate Course")').first.click()
            await human_delay(1.0, 1.8)

            print("⛓ Binding Lecturer instance to Course key template...")
            # Use value matching or labels depending on selection lists hydration attributes
            await page.locator('select[name="lecturerId"]').select_option(label="Dr Charles SMITH (LEC/777)")
            await page.locator('select[name="courseId"]').select_option(label="CSC301 — Advanced Data Structures")
            
            await page.locator('select[name="level"]').select_option("300")
            await page.locator('select[name="semester"]').select_option("First")
            await page.locator('select[name="classDate"]').select_option("Monday")
            await page.locator('input[name="classTime"]').type("10:00 AM", delay=random.randint(70, 120))
            await page.locator('input[name="academicSession"]').type("2026/2027", delay=random.randint(70, 120))
            await human_delay(2.0, 3.5)

            print("💾 Authorizing schedule record entry...")
            await page.locator('.modal-actions button:has-text("Allocate")').click()
            await page.wait_for_load_state("networkidle")
            await human_delay(4.0, 5.5)

            # -------------------------------------------------------------
            # PHASE 5: ADMIN SIGN OUT
            # -------------------------------------------------------------
            print("🚪 Signing out of Administration Profile session...")
            logout_btn = page.locator('button:has-text("Logout"), button:has-text("Sign Out"), a:has-text("Logout")').first
            if await logout_btn.is_visible():
                await logout_btn.click()
                await page.wait_for_load_state("networkidle")
                await human_delay(2.0, 3.0)
            else:
                # Secondary fall-back to explicitly clear session states via navigation route reset if button lacks simple text labels
                await page.goto("https://ca-app-sandy.vercel.app/")
                await page.wait_for_load_state("networkidle")

            # -------------------------------------------------------------
            # PHASE 6: LECTURER PORTAL VERIFICATION
            # -------------------------------------------------------------
            print("👤 Toggling view to Lecturer Access Module Tab...")
            await page.locator('button:has-text("Lecturer")').first.click()
            await human_delay(1.0, 2.0)

            print("🔑 Submitting newly assigned Lecturer token credentials...")
            await page.locator('input[name="lecturerId"]').type("LEC/777", delay=random.randint(70, 130))
            await page.locator('input[name="surname"]').type("SMITH", delay=random.randint(70, 130))
            await human_delay(1.0, 2.0)

            print("🔒 Entering Lecturer Portal space...")
            await page.locator('button:has-text("Sign In")').first.click()
            await page.wait_for_load_state("networkidle")
            
            print("📓 Presenting personalized Lecturer schedule layout dashboard...")
            # Explicitly wait to display allocated courses section container clearly on stream
            await human_delay(6.0, 8.0)

        except Exception as e:
            print(f"⚠️ App flow exception encountered during script execution: {e}")
            
        finally:
            # Safely compile frames and export compiled video target path asset
            video_path = await page.video.path()
            await context.close()
            await browser.close()
            print(f"\n🎉 Capture Complete! Walkthrough demonstration recording exported to: {video_path}")

if __name__ == "__main__":
    asyncio.run(main())
