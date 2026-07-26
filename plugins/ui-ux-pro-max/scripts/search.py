#!/usr/bin/env python3
"""
UI/UX Pro Max - Search Engine
Searchable database of UI/UX design rules with recommendations across 22 stacks.
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Any

# Get plugin root from environment or infer from script location
PLUGIN_ROOT = Path(__file__).parent.parent
DATA_DIR = PLUGIN_ROOT / "data"
REFERENCE_FILE = PLUGIN_ROOT / "references" / "quick-reference.md"


class UIUXDatabase:
    """Main database for UI/UX design rules and recommendations."""

    def __init__(self):
        self.rules = self._load_rules()
        self.styles = self._load_styles()
        self.colors = self._load_colors()
        self.typography = self._load_typography()
        self.ux_guidelines = self._load_ux_guidelines()

    def _load_rules(self) -> Dict[str, List[str]]:
        """Load design rules by category."""
        return {
            "accessibility": [
                "Contrast ratio must be at least 4.5:1 for normal text",
                "All images must have alt text describing content",
                "Keyboard navigation must work for all interactive elements",
                "ARIA labels required for screen readers",
                "Focus indicators must be visible (2px+ outline)",
                "Color must not be the only means of conveying information"
            ],
            "interaction": [
                "Touch targets must be minimum 44×44 pixels",
                "Spacing between touch targets at least 8px",
                "Provide loading feedback for all async operations",
                "Hover states must be distinct from normal state",
                "Animations should have clear purpose and meaning",
                "Mobile-first responsive design approach"
            ],
            "performance": [
                "Use WebP/AVIF formats for images (with fallbacks)",
                "Implement lazy loading for below-the-fold images",
                "Reserve space for dynamic content (CLS < 0.1)",
                "Minify and compress all assets",
                "Use modern bundling and code-splitting strategies",
                "Preload critical fonts and resources"
            ],
            "layout": [
                "Mobile-first breakpoints: 320px, 768px, 1024px, 1440px",
                "Viewport meta tag required for mobile",
                "No horizontal scroll on any breakpoint",
                "Container queries for component-level responsiveness",
                "Consistent spacing scale (8px, 16px, 24px, 32px...)",
                "Safe areas for notched devices"
            ],
            "typography": [
                "Base font size should be 16px for optimal readability",
                "Line height should be 1.4-1.6 for body text",
                "Max line length 60-80 characters for readability",
                "Use semantic color tokens for text (primary, secondary...)",
                "Font pairing: 1-2 typefaces maximum",
                "Consistent heading hierarchy (h1-h6)"
            ],
            "animation": [
                "Animation duration 150-300ms for UI feedback",
                "Easing: ease-out for entrances, ease-in for exits",
                "Motion must convey meaning (not purely decorative)",
                "Preserve spatial continuity in transitions",
                "Support prefers-reduced-motion media query",
                "Keep frame rate smooth (60fps target)"
            ],
            "forms": [
                "Form labels must be visible and associated (not placeholder)",
                "Error messages appear next to affected field",
                "Helper text explains field requirements",
                "Progressive disclosure for optional fields",
                "Real-time validation only after blur (not on type)",
                "Success feedback after submission"
            ],
            "navigation": [
                "Back button behavior must be predictable",
                "Bottom navigation max 5 items on mobile",
                "Deep linking support for all screens",
                "Breadcrumbs for hierarchical navigation",
                "Consistent menu positioning",
                "Search functionality for discovery"
            ]
        }

    def _load_styles(self) -> List[Dict[str, str]]:
        """Load UI style presets."""
        return [
            {"name": "minimal", "description": "Clean, simple, whitespace-heavy"},
            {"name": "vibrant", "description": "Bold colors, high contrast, energetic"},
            {"name": "dark", "description": "Dark backgrounds, light text, night mode"},
            {"name": "playful", "description": "Rounded corners, emoji, friendly tone"},
            {"name": "professional", "description": "Corporate, trust-focused, serious"},
            {"name": "content-first", "description": "Typography-heavy, reading-focused"},
            {"name": "immersive", "description": "Full-screen, hero sections, video"},
            {"name": "accessible", "description": "High contrast, large text, clear structure"}
        ]

    def _load_colors(self) -> List[Dict[str, str]]:
        """Load color palette recommendations."""
        return [
            {"name": "system-blue", "hex": "#007AFF", "use": "Primary actions, links"},
            {"name": "system-green", "hex": "#34C759", "use": "Success, positive actions"},
            {"name": "system-red", "hex": "#FF3B30", "use": "Errors, destructive actions"},
            {"name": "system-orange", "hex": "#FF9500", "use": "Warnings, attention"},
            {"name": "system-gray", "hex": "#8E8E93", "use": "Secondary text, disabled"},
            {"name": "neutral-50", "hex": "#F9FAFB", "use": "Background, light surfaces"},
            {"name": "neutral-900", "hex": "#111827", "use": "Text, dark backgrounds"},
            {"name": "purple-500", "hex": "#A855F7", "use": "Premium, special features"},
        ]

    def _load_typography(self) -> Dict[str, Dict[str, str]]:
        """Load typography recommendations."""
        return {
            "display": {"size": "32-48px", "weight": "700", "lineHeight": "1.2"},
            "heading": {"size": "24-32px", "weight": "600", "lineHeight": "1.3"},
            "subheading": {"size": "18-20px", "weight": "600", "lineHeight": "1.4"},
            "body": {"size": "14-16px", "weight": "400", "lineHeight": "1.6"},
            "caption": {"size": "12px", "weight": "400", "lineHeight": "1.4"},
            "code": {"size": "13px", "weight": "500", "family": "monospace"}
        }

    def _load_ux_guidelines(self) -> List[str]:
        """Load UX best practices."""
        return [
            "Users should understand the purpose of the page within 3 seconds",
            "Primary action should be obvious (high contrast, size, position)",
            "Page load time under 3 seconds for 4G connections",
            "Mobile navigation must work with one hand (thumb-friendly)",
            "Error prevention > error recovery",
            "Feedback should be immediate and clear",
            "Consistency across all pages and flows",
            "Progressive enhancement for older browsers",
            "Testing with real users should inform all design decisions",
            "Analytics should track user behavior, not just page views"
        ]

    def search(self, query: str, domain: str = None, stack: str = None, max_results: int = 10) -> List[Dict[str, Any]]:
        """Search the design database."""
        results = []
        query_lower = query.lower()

        # Search in rules
        for category, rule_list in self.rules.items():
            if domain and category != domain:
                continue
            for rule in rule_list:
                if query_lower in rule.lower():
                    results.append({
                        "type": "rule",
                        "category": category,
                        "content": rule,
                        "priority": 1 if category == "accessibility" else 2
                    })

        # Search in styles
        for style in self.styles:
            if query_lower in style["name"].lower() or query_lower in style["description"].lower():
                results.append({
                    "type": "style",
                    "name": style["name"],
                    "description": style["description"],
                    "priority": 3
                })

        # Search in colors
        for color in self.colors:
            if query_lower in color["name"].lower() or query_lower in color["use"].lower():
                results.append({
                    "type": "color",
                    "name": color["name"],
                    "hex": color["hex"],
                    "use": color["use"],
                    "priority": 4
                })

        # Search in typography
        for typo_type, specs in self.typography.items():
            if query_lower in typo_type.lower():
                results.append({
                    "type": "typography",
                    "name": typo_type,
                    "specs": specs,
                    "priority": 5
                })

        # Sort by priority and limit results
        results.sort(key=lambda x: x.get("priority", 10))
        return results[:max_results]

    def get_design_system(self, product_type: str, keywords: str = "") -> Dict[str, Any]:
        """Generate comprehensive design system recommendations."""
        return {
            "product_type": product_type,
            "keywords": keywords,
            "recommended_styles": [s for s in self.styles if any(kw.lower() in s["description"].lower() for kw in keywords.split())],
            "recommended_colors": self.colors[:4],
            "typography_scale": self.typography,
            "ux_priorities": self.ux_guidelines[:5],
            "rules": {cat: rules[:2] for cat, rules in self.rules.items()},
            "message": "Use this as a starting point. Adapt to your specific needs and test with users."
        }


def main():
    """CLI interface for the search engine."""
    if len(sys.argv) < 2:
        print("Usage: search.py '<query>' [--domain <domain>] [--design-system] [--stack <stack>] [-n <num>] [-p '<project_name>']")
        print("\nDomains: ux, style, product, color, typography, chart, icons, gsap, react, nextjs, vue, svelte, astro")
        print("Stacks: react, nextjs, vue, svelte, astro, nuxtjs, angular, laravel, swiftui, flutter, etc.")
        sys.exit(1)

    db = UIUXDatabase()
    query = sys.argv[1]
    domain = None
    stack = None
    max_results = 10
    design_system_mode = False
    project_name = None

    # Parse arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--domain":
            domain = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--stack":
            stack = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--design-system":
            design_system_mode = True
            i += 1
        elif sys.argv[i] == "-n":
            max_results = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "-p":
            project_name = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    # Output results
    if design_system_mode:
        result = db.get_design_system(query, query)
        print(json.dumps(result, indent=2))
    else:
        results = db.search(query, domain, stack, max_results)
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
