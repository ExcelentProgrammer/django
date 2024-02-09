import json

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()


def getScript(url: object) -> str:
    ext: str = str(url).split(".")[-1]

    if settings.DEBUG:
        url = f"http://localhost:5173/{url}"
    else:
        url: str = static(url)

    if ext == "css":
        script: str = "<link rel='stylesheet' type='text/css' href='{}'>".format(url)
    else:
        script: str = "<script type='text/javascript' src='{}'></script>".format(url)
    return script


@register.simple_tag
def vite_load():
    try:
        fd = open(f"{settings.VITE_APP_DIR}/manifest.json", "r")
        manifest = json.load(fd)
    except:
        raise Exception(
            f"Vite manifest file not found or invalid. Maybe your {settings.VITE_APP_DIR}/manifest.json file is empty?"
        )

    if not settings.DEBUG:
        imports_files = "".join(
            [
                getScript(file['file']) for file in manifest.values()
            ]
        )

    else:
        imports_files = "".join(
            [
                getScript(file) for file in manifest.keys()
            ]
        )
        imports_files += f"""
                          <script type="module" src="http://localhost:5173/@vite/client"></script>
                          <script type="module" src="{static("js/vite-refresh.js")}"></script>
                      """

    return mark_safe(imports_files)
