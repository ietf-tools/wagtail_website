from django.test import TestCase
from wagtail.models import Page, Site

from ..home.factories import HomePageFactory
from ..home.models import HomePage
from .factories import FormPageFactory
from .models import FormPage


class FormPageTests(TestCase):
    def setUp(self):
        root = Page.get_first_root_node()
        self.home: HomePage = HomePageFactory(parent=root)  # type: ignore

        site = Site.objects.get()
        site.root_page = self.home
        site.save(update_fields=["root_page"])

        self.form_page: FormPage = FormPageFactory(
            parent=self.home,
        )  # type: ignore

    def test_form_page(self):
        response = self.client.get(path=self.form_page.url)
        self.assertEqual(response.status_code, 200)
        html = response.content.decode()

        self.assertIn(self.form_page.title, html)
        self.assertIn(self.form_page.intro, html)
