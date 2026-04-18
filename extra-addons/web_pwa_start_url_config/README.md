# PWA Start URL Config

This addon lets you configure the backend PWA `start_url` via `odoo.conf`.
Tested with Odoo 19.

## Install

- Add this addon to your `addons_path`.
- Install the module `web_pwa_start_url_config` in Apps.

## Configure

Add a `pwa_start_url` key to your `odoo.conf` and restart Odoo:

```
[options]
pwa_start_url = /odoo/sales?view_type=kanban
```

Notes:
- The value is forced to start with `/`.
- If the key is missing, Odoo's default `start_url` is used.
- Use the exact path + query you see in your browser URL for the desired landing page.
