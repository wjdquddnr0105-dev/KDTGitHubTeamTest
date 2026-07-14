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

    def test_dashboard_has_no_ai_iris_links(self):
        with app.test_client() as client:
            html = client.get("/smart-factory/dashboard").get_data(as_text=True)

        self.assertNotIn("/predict", html)
        self.assertNotIn("/login", html)

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

    def test_all_smart_factory_pages_render_with_shared_navigation(self):
        pages = {
            "/smart-factory/dashboard": "dashboard-kpis",
            "/smart-factory/quality": "production-line-map",
            "/smart-factory/equipment": "equipment-grid",
            "/smart-factory/reports": "report-filters",
        }

        with app.test_client() as client:
            for route, landmark in pages.items():
                response = client.get(route)
                self.assertEqual(response.status_code, 200, route)
                html = response.get_data(as_text=True)
                self.assertIn(f'id="{landmark}"', html)
                self.assertIn('id="smart-factory-nav"', html)

    def test_prototype_pages_load_their_page_scripts(self):
        expected_scripts = {
            "/smart-factory/quality": "smart_factory_quality.js",
            "/smart-factory/equipment": "smart_factory_equipment.js",
            "/smart-factory/reports": "smart_factory_reports.js",
        }

        with app.test_client() as client:
            for route, script_name in expected_scripts.items():
                html = client.get(route).get_data(as_text=True)
                script = client.get(f"/static/js/{script_name}")
                self.assertIn(script_name, html)
                self.assertEqual(script.status_code, 200)
                script.close()


if __name__ == "__main__":
    unittest.main()
