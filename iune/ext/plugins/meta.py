from operator import attrgetter
from itertools import groupby

from hyde.ext.plugins.meta import Group, GrouperPlugin
from hyde.site import Resource
from hyde.util import pairwalk


class LanguageGrouperPlugin(GrouperPlugin):
    def begin_site(self):
        """
        Initialize plugin. Add the specified groups to the
        site context variable.
        """
        config = self.site.config
        if not hasattr(config, 'grouper'):
            return
        if not hasattr(self.site, 'grouper'):
            self.site.grouper = {}

        for name, grouping in self.site.config.grouper.__dict__.items():
            grouping.name = name
            prev_att = 'prev_in_%s' % name
            next_att = 'next_in_%s' % name
            setattr(Resource, prev_att, None)
            setattr(Resource, next_att, None)
            self.site.grouper[name] = Group(grouping)
            walker = Group.walk_resources(
                            self.site.content, self.site.grouper[name])

            for language, walker in groupby(walker, attrgetter('meta.language')):
                for prev, next in pairwalk(walker):
                    setattr(next, prev_att, prev)
                    setattr(prev, next_att, next)
