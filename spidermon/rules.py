from .context import create_context_dict


class Rule(object):
    """
    Base class for rules
    """
    __rule_type__ = 'rule'

    def __str__(self):
        return self.__class__.__name__

    @property
    def type(self):
        return self.__rule_type__

    @property
    def name(self):
        return self.type

    def run_check(self, stats):
        context_params = create_context_dict(stats)
        return bool(self.check(**context_params))

    def check(self, stats):
        raise NotImplementedError


class CallableRule(Rule):
    """
    Callable rule. must be initialiazed with a callable that will be used for checking
    """
    __rule_type__ = 'callable'

    def __init__(self, call):
        self.call = call

    @property
    def name(self):
        return self.call.func_name

    def check(self, **context_params):
        return self.call(**context_params)