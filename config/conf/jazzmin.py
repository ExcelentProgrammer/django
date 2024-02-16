from typing import Any

JAZZMIN_SETTINGS: dict[str | Any, str | None | Any] = {
    "site_title": "Jscorp",
    "site_header": "Jscorp",
    "site_brand": "Jscorp",
    "site_logo": "/images/logo.png",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to the library",
    "copyright": "Acme Library Ltd",
    "search_model": ["auth.User"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Home", "url": "admin:index",
         "permissions": ["auth.view_user"]},
        {"name": "Support",
         "url": "https://github.com/farridav/django-jazzmin/issues",
         "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "usermenu_links": [
        {"name": "Support",
         "url": "https://github.com/farridav/django-jazzmin/issues",
         "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible",
                                    "auth.group": "vertical_tabs"},
}
