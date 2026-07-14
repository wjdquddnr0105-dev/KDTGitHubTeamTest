import unittest

try:
    from smart_factory.app import app
except ModuleNotFoundError:
    from app import app


class StandaloneSmartFactoryAppTest(unittest.TestCase):
    def test_root_redirects_to_dashboard(self):
        with app.test_client() as client:
            response = client.get("/")

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.location.endswith("/smart-factory/dashboard"))

    def test_dashboard_renders_without_ai_iris_dependencies(self):
        with app.test_client() as client:
            response = client.get("/smart-factory/dashboard")

        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        for element_id in ("smart-factory-nav", "dashboard-kpis", "dashboard-status-summary", "dashboard-events"):
            self.assertIn(f'id="{element_id}"', html)
        self.assertNotIn("/predict", html)
        self.assertNotIn("/login", html)

    def test_dashboard_has_no_links_to_unavailable_pages(self):
        with app.test_client() as client:
            html = client.get("/smart-factory/dashboard").get_data(as_text=True)

        for path in ("/smart-factory/quality", "/smart-factory/equipment", "/smart-factory/reports"):
            self.assertNotIn(path, html)

    def test_standalone_static_assets_are_served(self):
        with app.test_client() as client:
            css = client.get("/static/css/smart_factory.css")
            javascript = client.get("/static/js/smart_factory.js")

        self.assertEqual(css.status_code, 200)
        self.assertIn("--bg", css.get_data(as_text=True))
        self.assertEqual(javascript.status_code, 200)
        self.assertIn("toggleSmartAssistant", javascript.get_data(as_text=True))
        css.close()
        javascript.close()


if __name__ == "__main__":
    unittest.main()
