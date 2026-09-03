import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class HomepageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.section_ids = []
        self.top_nav_hrefs = []
        self.in_top_nav = False
        self.top_nav_depth = 0
        self.in_pub_title = False
        self.pub_title_anchor_count = 0
        self.profile_links_count = 0
        self.sidebar_nav_count = 0
        self.link_texts = []
        self._capture_link_text = False
        self._current_link_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        class_names = set(attrs.get("class", "").split())
        if tag == "section" and "id" in attrs:
            self.section_ids.append(attrs["id"])
        if tag == "nav" and "top-nav" in class_names:
            self.in_top_nav = True
            self.top_nav_depth = 1
        elif self.in_top_nav and tag not in {"br", "img", "meta", "link", "input"}:
            self.top_nav_depth += 1
        if tag == "nav" and "sidebar-nav" in class_names:
            self.sidebar_nav_count += 1
        if tag == "div" and "profile-links" in class_names:
            self.profile_links_count += 1
        if tag == "h3" and "pub-title" in class_names:
            self.in_pub_title = True
        if self.in_pub_title and tag == "a":
            self.pub_title_anchor_count += 1
        if tag == "a":
            if self.in_top_nav and "href" in attrs:
                self.top_nav_hrefs.append(attrs["href"])
            self._capture_link_text = True
            self._current_link_parts = []

    def handle_endtag(self, tag):
        if tag == "h3" and self.in_pub_title:
            self.in_pub_title = False
        if tag == "a" and self._capture_link_text:
            text = " ".join(part.strip() for part in self._current_link_parts if part.strip())
            if text:
                self.link_texts.append(text)
            self._capture_link_text = False
            self._current_link_parts = []
        if self.in_top_nav and tag not in {"br", "img", "meta", "link", "input"}:
            self.top_nav_depth -= 1
            if self.top_nav_depth == 0:
                self.in_top_nav = False

    def handle_data(self, data):
        if self._capture_link_text:
            self._current_link_parts.append(data)


class HomepageTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index_text = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.css_text = (ROOT / "css" / "custom.css").read_text(encoding="utf-8")
        cls.parser = HomepageParser()
        cls.parser.feed(cls.index_text)

    def test_section_order_matches_reference_adaptation(self):
        self.assertEqual(
            self.parser.section_ids,
            [
                "biography",
                "news",
                "publications",
                "education",
                "awards",
                "services",
                "presentations",
                "teaching",
                "misc",
            ],
        )

    def test_top_navigation_is_present_instead_of_sidebar_contents_nav(self):
        self.assertEqual(
            self.parser.top_nav_hrefs,
            [
                "#biography",
                "#news",
                "#publications",
                "#education",
                "#awards",
                "#services",
                "#presentations",
                "#teaching",
                "#misc",
            ],
        )
        self.assertEqual(self.parser.sidebar_nav_count, 0)

    def test_profile_links_block_replaces_icon_only_social_links(self):
        self.assertGreaterEqual(self.parser.profile_links_count, 1)
        self.assertIn(".profile-links", self.css_text)

    def test_publication_titles_use_reference_title_first_markup(self):
        self.assertGreaterEqual(self.parser.pub_title_anchor_count, 6)

    def test_presentation_links_use_ppt_label(self):
        self.assertIn("PPT", self.parser.link_texts)
        self.assertNotIn("Presentation", self.parser.link_texts)


if __name__ == "__main__":
    unittest.main()
