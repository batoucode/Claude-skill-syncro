---
name: ui-ux-pro-max
description: UI/UX design intelligence for web and mobile. Searchable local database with 84 styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines, 104 icon entries, 16 GSAP motion presets, and 25 chart types across 22 stacks.
---

# UI/UX Pro Max - Design Intelligence

Searchable database of UI/UX design rules with priority-based recommendations: 84 styles, 192 color palettes, 74 font pairings, 192 product types with reasoning rules, 98 UX guidelines, 104 icon entries, 16 GSAP motion presets, and 25 chart types across 22 technology stacks.

## When to Apply

Use this Skill when the task involves **UI structure, visual design decisions, interaction patterns, or user experience quality control**: designing new pages, creating/refactoring UI components, choosing color/typography/spacing/layout systems, reviewing UI for UX/accessibility/consistency, implementing navigation/animation/responsive behavior, or improving perceived quality and usability.

Skip it for pure backend logic, API/database design, non-visual performance work, infrastructure/DevOps, or non-visual scripts — unless the task changes how something **looks, feels, moves, or is interacted with**.

## Rule Categories by Priority

*Follow priority 1→10 to decide which category to focus on first; use `--domain <Domain>` to query full details. The full rule text for every category lives in `references/quick-reference.md` — read it on demand rather than loading it every time.*

| Priority | Category            | Impact   | Domain                | Key Checks (Must Have)                                                |
| -------- | ------------------- | -------- | --------------------- | --------------------------------------------------------------------- |
| 1        | Accessibility       | CRITICAL | `ux`                  | Contrast 4.5:1, Alt text, Keyboard nav, Aria-labels                   |
| 2        | Touch & Interaction | CRITICAL | `ux`                  | Min size 44×44px, 8px+ spacing, Loading feedback                      |
| 3        | Performance         | HIGH     | `ux`                  | WebP/AVIF, Lazy loading, Reserve space (CLS < 0.1)                    |
| 4        | Style Selection     | HIGH     | `style`, `product`    | Match product type, Consistency, SVG icons (no emoji)                 |
| 5        | Layout & Responsive | HIGH     | `ux`                  | Mobile-first breakpoints, Viewport meta, No horizontal scroll         |
| 6        | Typography & Color  | MEDIUM   | `typography`, `color` | Base 16px, Line-height 1.5, Semantic color tokens                     |
| 7        | Animation           | MEDIUM   | `ux`, `gsap`          | Duration 150–300ms, Motion conveys meaning, Spatial continuity        |
| 8        | Forms & Feedback    | MEDIUM   | `ux`                  | Visible labels, Error near field, Helper text, Progressive disclosure |
| 9        | Navigation Patterns | HIGH     | `ux`                  | Predictable back, Bottom nav ≤5, Deep linking                         |
| 10       | Charts & Data       | LOW      | `chart`               | Legends, Tooltips, Accessible colors                                  |

## Running the Search Tool

The search script lives inside this skill's own directory, not the project directory. Always invoke it by its full path — do not assume a particular working directory:

```bash
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "<query>" --domain <domain>
```

If `python` is not found, try `python3`, then `py -3`. Requires Python 3.x, no external dependencies.

## Workflow

### Step 1: Analyze User Requirements

Extract from the user request:

- **Product type**: SaaS, e-commerce, portfolio, dashboard, entertainment, tool, productivity, or hybrid
- **Target audience & context**: age group, usage context (commute, leisure, work)
- **Style keywords**: playful, vibrant, minimal, dark mode, content-first, immersive, etc.
- **Stack**: detect from the project — React, Next.js, Vue, Svelte, Astro, SwiftUI, Flutter, Tailwind, Angular, Laravel, etc.

### Step 2: Generate Design System (REQUIRED for new pages/projects)

Always start with `--design-system` to get comprehensive recommendations:

```bash
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

### Step 3: Supplement with Detailed Searches (as needed)

```bash
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "<keyword>" --domain <domain> [-n <max_results>]
```

**Available domains**: `product`, `style`, `color`, `typography`, `chart`, `ux`, `landing`, `icons`, `gsap`, `react`, `nextjs`, etc.

### Step 4: Stack Guidelines

```bash
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "<keyword>" --stack <stack>
```

**Available stacks**: `react`, `nextjs`, `vue`, `svelte`, `astro`, `nuxtjs`, `angular`, `laravel`, `swiftui`, `react-native`, `flutter`, `jetpack-compose`, `html-tailwind`, `shadcn`, `threejs`, etc.

## Example Workflow

**User request:** "Make an AI search homepage." (Next.js detected)

```bash
# Step 2: design system
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "AI search tool modern minimal" --design-system -p "AI Search"

# Step 3: supplement
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "search loading animation" --domain ux

# Step 4: stack guidelines
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "suspense streaming bundle" --stack nextjs
```

Then synthesize the design system + detailed searches and implement.

## Tips for Better Results

- Use **multi-dimensional keywords** — combine product + industry + tone: `"entertainment social vibrant content-dense"`, not just `"app"`
- Try different phrasings for the same need
- Use `--design-system` first for full recommendations, then `--domain` to deep-dive
- Pass the detected stack explicitly for implementation-specific guidance

## Before Delivering App UI

Read pro-rules and run through its canonical Pre-Delivery Checklist. It covers icon/visual-element discipline, interaction feedback, light/dark contrast, safe-area layout, and accessibility — scoped to native/mobile app UI.

---

**Source**: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill  
**Version**: 1.0.0  
**Author**: nextlevelbuilder / batoucode (adapted)
