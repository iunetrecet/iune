import os
from hyde.ext.plugins.css import SassyCSSPlugin


class SASSPlugin(SassyCSSPlugin):
    def _should_parse_resource(self, resource):
        """
        Check user defined
        """
        return resource.source_file.kind == 'sass' and \
               getattr(resource, 'meta', {}).get('parse', True)

    def text_resource_complete(self, resource, text):
        """
        Run sassycss compiler on text.
        """
        if not self._should_parse_resource(resource):
            return

        includes = [resource.node.path] + self.includes
        includes = [path.rstrip(os.sep) + os.sep for path in includes]
        options = self.options
        if not 'load_paths' in options:
            options['load_paths'] = []
        options['load_paths'].extend(includes)
        scss = self.scss.Scss(scss_opts=options, scss_vars=self.vars )
        return scss.compile(text, is_sass=True)
