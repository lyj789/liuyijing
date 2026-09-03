# Homepage Template Adaptation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle the static homepage so it follows the `jianshuod` academic homepage template while preserving Yijing Liu's content and all existing sections.

**Architecture:** Keep the site as a single static HTML page with one stylesheet and inline interaction scripts. Replace the current sidebar navigation and publication row structure with the reference template's sidebar profile block, sticky top navigation, flatter section layout, and publication-first hierarchy.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, Python `unittest` for regression checks

---

### Task 1: Add Regression Coverage For Template Structure

**Files:**
- Create: `tests/test_homepage.py`
- Test: `tests/test_homepage.py`

- [ ] **Step 1: Write the failing test**

Write tests that assert the homepage uses:
- a reference-style `top-nav`
- a `News` section between `Biography` and `Publications`
- `profile-links` instead of icon-only social links
- `h3.pub-title > a` publication titles
- `PPT` labels for presentation links

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_homepage -v`
Expected: FAIL because the current page still uses the old section order and sidebar navigation.

- [ ] **Step 3: Write minimal implementation**

Update `index.html` and `css/custom.css` to satisfy the new structure.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_homepage -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_homepage.py index.html css/custom.css docs/superpowers/specs/2026-09-03-homepage-template-adaptation-design.md docs/superpowers/plans/2026-09-03-homepage-template-adaptation.md
git commit -m "feat: align homepage with reference academic template"
```

### Task 2: Replace Sidebar And Navigation Structure

**Files:**
- Modify: `index.html`
- Modify: `css/custom.css`
- Test: `tests/test_homepage.py`

- [ ] **Step 1: Write the failing test**

Extend or keep tests that require:
- no sidebar contents navigation block
- presence of top navigation links in the approved order
- reference-style profile links

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_homepage -v`
Expected: FAIL on navigation structure expectations.

- [ ] **Step 3: Write minimal implementation**

Port the sidebar and top navigation structure from the reference template and adapt labels to Yijing Liu's homepage sections.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_homepage -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add index.html css/custom.css tests/test_homepage.py
git commit -m "feat: adopt reference sidebar and top navigation"
```

### Task 3: Rebuild Publications And News Presentation

**Files:**
- Modify: `index.html`
- Modify: `css/custom.css`
- Test: `tests/test_homepage.py`

- [ ] **Step 1: Write the failing test**

Require:
- `news` section presence and order
- flattened publication rows with title-first structure
- `PPT` labels replacing `Presentation` where applicable

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_homepage -v`
Expected: FAIL until the publication markup and news section match the target layout.

- [ ] **Step 3: Write minimal implementation**

Add the `News` section and convert publication entries to the reference template's hierarchy.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_homepage -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add index.html css/custom.css tests/test_homepage.py
git commit -m "feat: restyle news and publications"
```

### Task 4: Manual Browser Verification

**Files:**
- Modify: `index.html`
- Modify: `css/custom.css`

- [ ] **Step 1: Run the page locally**

Run a simple local HTTP server from the project root and open the homepage in a browser.

- [ ] **Step 2: Verify desktop layout**

Check:
- sidebar spacing
- top navigation stickiness
- publication row readability
- long author list wrapping

- [ ] **Step 3: Verify mobile layout**

Check:
- sidebar collapses cleanly
- no overlap between navigation and sections
- item rows stack cleanly

- [ ] **Step 4: Fix any issues and re-run tests**

Run: `python3 -m unittest tests.test_homepage -v`
Expected: PASS after any responsive fixes.
