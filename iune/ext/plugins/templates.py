from itertools import groupby
from operator import attrgetter

from hyde.plugin import Plugin
from hyde.ext.templates.jinja import HydeLoader

from jinja2 import contextfunction
from jinja2.loaders import FileSystemLoader
from yammy.translator import yammy_to_html_string


class YammyHydeLoader(HydeLoader):
    def get_html_source(self, get_source, environment, template):
        contents, filename, uptodate = get_source(environment, template)
        if filename.endswith(('.ymy', '.yammy')):
            contents = yammy_to_html_string(contents, keep_line_numbers=False)
        return contents, filename, uptodate

    def get_source(self, environment, template):
        source = super(YammyHydeLoader, self).get_source
        return self.get_html_source(source, environment, template)


class YammyPlugin(Plugin):
    def template_loaded(self, template):
        loader = template.env.loader
        template.env.loader = YammyHydeLoader(
                loader.searchpath,
                loader.site,
                loader.preprocessor,
                )
        super(YammyPlugin, self).template_loaded(template)

    def begin_text_resource(self, resource, text):
        if resource.meta.get('parse', None) == 'yammy':
            return yammy_to_html_string(text, keep_line_numbers=False)
        return text


@contextfunction
def translated(context, resources):
    current_lang = context['resource'].meta.get('language', None)
    for uuid, resources in groupby(resources, attrgetter('meta.uuid')):
        resources = list(resources)
        current = ( r for r in resources if r.meta.language == current_lang )
        current = next(current, None)
        resource = resources[0] if current is None else current
        yield resource


class TranslatedResourcePlugin(Plugin):
    def begin_site(self):
        self.template.env.globals['translated'] = translated
