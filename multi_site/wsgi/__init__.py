"""Dynamic WSGI application loader for Django.

Thanks to this clever hack you can import anything from `wsgi` module.
For instance, if you import `wsgi.site_x`:

    >>> import wsgi.site_x

it dynamically creates a wsgi app
config which depends on `settings.site_x`:

    >>> import os
    >>> from django.core.wsgi import get_wsgi_application
    >>> os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "multi_site.settings.site_x")
    >>> application = get_wsgi_application()


More info:
https://www.usenix.org/system/files/login/articles/09beazley_061-068_online.pdf
"""

import imp
import sys
import textwrap


class Loader(object):
    """Dynamically generated wsgi.py files."""

    def load_module(self, fullname, path=None):
        """Generate a submodule based on the path being imported."""
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        code = textwrap.dedent("""\
        import os
        from django.core.wsgi import get_wsgi_application
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multi_site.settings.{0}")
        application = get_wsgi_application()
        """).format(fullname.split('.')[-1])
        exec(code, mod.__dict__)
        return mod


class Finder(object):
    """Inject `Loader` instance if trying to import a submodule of the current
    module.
    """

    def find_module(self, fullname, path=None):
        if fullname.startswith(__name__):
            return Loader()
        else:
            return None


sys.meta_path.append(Finder())
