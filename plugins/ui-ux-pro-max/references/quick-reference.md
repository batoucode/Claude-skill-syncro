# UI/UX Pro Max - Quick Reference Guide

## Priority Categories (1-10)

### 1. 🔴 CRITICAL: Accessibility
**Impact**: Legal compliance, inclusive design, core functionality

**Must-Haves:**
- **Contrast Ratio**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Alt Text**: Every image/icon must have descriptive alt text
- **Keyboard Navigation**: All functionality must work with Tab/Enter/Escape
- **ARIA Labels**: Form inputs, buttons, landmarks need proper labels
- **Focus Indicators**: Visible 2px+ outline on focused elements
- **No Color-Only Conveying**: Combine color with pattern, text, or icon

**Common Mistakes:**
- ❌ Using `<div>` for buttons instead of `<button>`
- ❌ Placeholder text instead of labels
- ❌ Removing default focus outlines
- ❌ Low contrast on gray text

**Tools**: axe DevTools, WAVE, Lighthouse, NVDA/JAWS

---

### 2. 🔴 CRITICAL: Touch & Interaction
**Impact**: Mobile usability, error prevention, user satisfaction

**Must-Haves:**
- **Minimum Size**: 44×44px for all touch targets
- **Spacing**: At least 8px gap between touch targets
- **Loading Feedback**: Show spinner/progress during async operations
- **Error Prevention**: Confirm before destructive actions (delete, logout)
- **Touch Feedback**: Visual feedback (highlight) on press
- **One-Hand Usability**: Mobile navigation reachable with thumb

**Common Mistakes:**
- ❌ Button size 30×30px (too small)
- ❌ Submit button directly next to Cancel button
- ❌ No loading indicator on slow API calls
- ❌ Confirmation only in alert() dialog

**Stack-Specific**:
- **React**: Use `onPointerDown/Up` for better touch feedback
- **iOS**: Account for safe areas (notch, home indicator)
- **Android**: Back button behavior differs from web

---

### 3. 🟠 HIGH: Performance
**Impact**: Page load, retention, SEO, user satisfaction

**Must-Haves:**
- **Image Format**: WebP/AVIF with PNG fallback
- **Lazy Loading**: Images below fold should load on scroll
- **CLS < 0.1**: Reserve space for dynamic content (skeletons)
- **LCP < 2.5s**: Largest paint under 2.5 seconds
- **FID < 100ms**: First input delay minimal
- **Code Splitting**: Load only what's needed per route

**Common Mistakes:**
- ❌ Serving full-size images on mobile
- ❌ Loading all fonts upfront
- ❌ No space reservation (layout shift)
- ❌ Unoptimized third-party scripts

**Tools**: Lighthouse, WebPageTest, Bundle Analyzer

---

### 4. 🟠 HIGH: Style Selection
**Impact**: Brand coherence, user expectations, professional appearance

**Must-Haves:**
- **Product Type Match**: SaaS style ≠ Entertainment style
- **Consistency**: Same component = same appearance everywhere
- **SVG Icons**: Never use emoji in professional apps
- **Theme Support**: Dark mode for modern apps
- **Accessibility**: Styles must support high-contrast mode

**8 Main Styles:**
1. **Minimal** (Figma, Stripe) → whitespace, 1-2 colors, clean typography
2. **Vibrant** (Duolingo, Slack) → bold colors, gradients, energetic
3. **Dark** (VS Code, Figma dark) → true black backgrounds, neon accents
4. **Playful** (Mailchimp, Basecamp) → rounded, emoji, friendly tone
5. **Professional** (LinkedIn, Microsoft) → corporate, trust-focused, serif
6. **Content-First** (Medium, Wikipedia) → typography-heavy, reading-focused
7. **Immersive** (Apple, Netflix) → hero images, full-screen, video-first
8. **Accessible** (Gov.uk, BBC) → high contrast, large text, clear hierarchy

---

### 5. 🟠 HIGH: Layout & Responsive
**Impact**: Mobile usability, device support, future-proof design

**Must-Haves:**
- **Mobile-First**: Design mobile first, enhance for desktop
- **Breakpoints**: 320px (mobile), 768px (tablet), 1024px (desktop), 1440px (large)
- **No Horizontal Scroll**: Ever. Not even in modals.
- **Viewport Meta**: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- **Flexible Layouts**: Flexbox/Grid, not fixed widths
- **Safe Areas**: Account for notches on iPhone 12+

**Common Mistakes:**
- ❌ Desktop-first approach
- ❌ Fixed width containers (width: 1200px always)
- ❌ Horizontal scroll on mobile
- ❌ No viewport meta tag

**CSS Grid Pattern:**
```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}
```

---

### 6. 🟡 MEDIUM: Typography & Color
**Impact**: Readability, accessibility, brand expression

**Must-Haves:**
- **Base Size**: 16px for body text (mobile) → 18px for desktop
- **Line Height**: 1.4-1.6 for body text (not 1.2)
- **Line Length**: 60-80 characters per line max
- **Semantic Colors**: Use tokens (primary, secondary, error) not hex values
- **Font Pairing**: 1-2 typefaces max (heading + body)
- **Hierarchy**: h1 > h2 > h3... (size + weight progression)

**Typographic Scale (8px base):**
| Element | Size | Weight | Height |
|---------|------|--------|--------|
| Display | 32-48px | 700 | 1.2 |
| Heading | 24-32px | 600 | 1.3 |
| Subhead | 18-20px | 600 | 1.4 |
| Body | 16px | 400 | 1.6 |
| Caption | 12px | 400 | 1.4 |
| Code | 13px | 500 | 1.4 |

**Color Token Pattern:**
```
--text-primary: #000000 (dark mode: #FFFFFF)
--text-secondary: #666666 (dark mode: #AAAAAA)
--bg-primary: #FFFFFF (dark mode: #1A1A1A)
--bg-secondary: #F5F5F5 (dark mode: #2A2A2A)
```

---

### 7. 🟡 MEDIUM: Animation
**Impact**: Perceived performance, delight factor, user flow

**Must-Haves:**
- **Duration**: 150-300ms for UI feedback (not 1000ms)
- **Easing**: ease-out for entrance, ease-in for exit
- **Purpose**: Motion must convey meaning (expand, move, highlight)
- **Spatial Continuity**: Animation should connect from/to actual positions
- **Prefers-Reduced-Motion**: Respect `prefers-reduced-motion` media query
- **Smooth**: Target 60fps (never drops below 30fps)

**Easing Functions:**
- `ease-out`: Quick start, slow end (UX feedback)
- `ease-in`: Slow start, quick end (dismissal)
- `cubic-bezier(0.34, 1.56, 0.64, 1)`: Spring bounce
- Never use `ease` (too bouncy, unpredictable)

**JavaScript Example (GSAP):**
```javascript
gsap.to(".element", {
  duration: 0.25,
  opacity: 1,
  y: 0,
  ease: "power2.out"
});
```

---

### 8. 🟡 MEDIUM: Forms & Feedback
**Impact**: Task completion, error recovery, user confidence

**Must-Haves:**
- **Visible Labels**: Not placeholders (placeholder disappears on focus)
- **Error Near Field**: Red outline + message below input
- **Helper Text**: Explain requirements ("At least 8 characters")
- **Progressive Disclosure**: Show optional fields only if needed
- **Validation Timing**: On blur (not on every keystroke)
- **Success Feedback**: Checkmark or confirmation message
- **Disabled State**: Clearly indicate why field is disabled

**Form Pattern:**
```html
<label for="email">Email Address</label>
<input 
  id="email" 
  type="email" 
  aria-describedby="email-hint"
  required
>
<span id="email-hint">We'll never share your email</span>
<span class="error" id="email-error"></span>
```

---

### 9. 🟠 HIGH: Navigation Patterns
**Impact**: Discoverability, user confidence, information architecture

**Must-Haves:**
- **Predictable Back**: Web back button = previous page, not menu close
- **Bottom Navigation**: Mobile max 5 items (5+ use tabs/drawer)
- **Deep Linking**: Every screen must have shareable URL
- **Breadcrumbs**: For hierarchical navigation (ecommerce, docs)
- **Search**: For >20 items, add search functionality
- **Consistent Position**: Header/footer same across all pages

**Mobile Navigation Strategies:**
1. **Bottom Tab Bar** (< 5 items) → Instagram, TikTok
2. **Hamburger Menu** (6+ items) → Twitter, Reddit
3. **Tab + Drawer Hybrid** (mix priority items + menu) → Airbnb
4. **Bottom Sheet** (content-heavy secondary nav) → Google Maps

---

### 10. 🔵 LOW: Charts & Data Visualization
**Impact**: Data comprehension, insights, storytelling

**Must-Haves:**
- **Legends**: Identify all colors/patterns
- **Tooltips**: Show exact values on hover
- **Accessible Colors**: Use colorblind-friendly palettes
- **Label Axes**: Always label x/y axes with units
- **Data Source**: Attribution for external data
- **Responsive**: Charts should reflow on mobile (switch to vertical bar from horizontal)

**Chart Type Guide:**
| Goal | Chart Type | Tools |
|------|-----------|-------|
| Trend over time | Line chart | Recharts, Chart.js |
| Compare values | Bar chart | Recharts, Victory |
| Part of whole | Pie/Donut | Recharts (use sparingly) |
| Distribution | Histogram | Recharts, Observable |
| Relationships | Scatter | D3.js, Apache ECharts |
| Hierarchies | Treemap | D3.js |

**Recharts Example:**
```jsx
import { LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts';

<LineChart data={data}>
  <XAxis />
  <YAxis />
  <Tooltip formatter={(value) => `$${value}`} />
  <Line type="monotone" dataKey="revenue" stroke="#007AFF" />
</LineChart>
```

---

## Stack-Specific Guidelines

### React & Next.js
- Use `next/image` for image optimization (automatic WebP conversion)
- Leverage `next/font` for font optimization
- Code-split routes with `dynamic()` for performance
- Use `prefers-reduced-motion` in `useEffect` hooks
- Server Components for reducing JavaScript bundle

### Vue & Nuxt
- Use `v-cloak` to prevent flash of unstyled content
- Lazy-load components: `defineAsyncComponent()`
- Nuxt auto-imports: minimize explicit imports
- Use `<Suspense>` for loading states
- CSS Scoping: Always use scoped styles

### Svelte
- Reactive variables auto-track dependencies
- Use Svelte Transitions API (smooth animations)
- Stores for global state (simpler than React Context)
- Minimal bundle size (best performance)

### Tailwind CSS
- Use `@apply` sparingly (creates bloat)
- Component layer for reusable classes
- Dark mode: `class` strategy or `media` (auto-detect)
- Custom theme colors in `tailwind.config.js`
- Never hardcode colors (use theme tokens)

### Flutter & SwiftUI
- Use `SafeArea` widget to respect safe insets
- `MaterialApp` for Android, `CupertinoApp` for iOS
- Platform-specific navigation (bottom tab vs side drawer)
- Test on real devices (simulator is not enough)

---

## Pre-Delivery Checklist

- [ ] **Accessibility**: Run axe, test with keyboard, check contrast
- [ ] **Performance**: Lighthouse score > 90, images optimized
- [ ] **Mobile**: Test on real phones (not just browser DevTools)
- [ ] **Dark Mode**: All colors work in light + dark themes
- [ ] **Responsive**: No horizontal scroll on any breakpoint
- [ ] **Animations**: Smooth 60fps, respect prefers-reduced-motion
- [ ] **Forms**: Placeholders != labels, error messages clear
- [ ] **Loading States**: Spinners, skeletons, or progress indicators
- [ ] **Error States**: Show what went wrong + recovery path
- [ ] **Empty States**: Describe next steps when no content
- [ ] **Offline**: App shows graceful degradation (if applicable)
- [ ] **Navigation**: Back button works, deep links work
- [ ] **Touch**: All buttons 44×44px min with 8px spacing
- [ ] **Fonts**: System fonts for speed (or Google Fonts optimized)
- [ ] **Icons**: SVG, scalable, semantic alt text

---

## Common Design Debt & How to Fix

| Issue | Fix | Effort |
|-------|-----|--------|
| Low contrast text | Use contrast checker, update color tokens | 1 hour |
| Buttons too small | Add padding, increase hit area to 44px min | 30 min |
| No loading feedback | Add spinners/skeletons to async calls | 1 hour |
| Layout shift (CLS) | Reserve space for dynamic content | 2 hours |
| Mobile horizontal scroll | Fix max-width, use flexbox properly | 1-2 hours |
| Colors hardcoded | Extract to CSS custom properties | 3 hours |
| No dark mode | Add theme toggle, update all colors | 4 hours |
| Animations jank | Profile with DevTools, reduce complexity | 2-4 hours |

---

## Resources & Tools

### Testing
- **Accessibility**: axe DevTools, WAVE, Lighthouse, NVDA
- **Performance**: Lighthouse, WebPageTest, Chrome DevTools
- **Visual**: Figma, Storybook, Percy (visual regression)
- **Mobile**: BrowserStack, Sauce Labs, real device testing

### Design Systems
- **Figma Components**: Align design ↔ code
- **Storybook**: Document components, test interactions
- **Token Studio**: Sync design tokens across tools
- **Chromatic**: Visual regression testing

### Learning
- **Web.dev**: Google's performance + accessibility guide
- **MDN Web Docs**: Authoritative reference
- **A11y Project**: Accessibility resources
- **Nielsen Norman**: UX research articles

---

**Version**: 1.0.0  
**Last Updated**: 2026-07-26  
**Maintained By**: batoucode
