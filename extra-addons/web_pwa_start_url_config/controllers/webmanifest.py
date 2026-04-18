# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import tools
from odoo.addons.web.controllers.webmanifest import WebManifest


class WebManifestStartUrl(WebManifest):

    def _get_webmanifest(self):
        manifest = super()._get_webmanifest()
        start_url = tools.config.get("pwa_start_url")
        if start_url:
            manifest['start_url'] = f"/{start_url.lstrip('/')}"
        return manifest
