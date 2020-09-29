from _dependencies.attributes import _Attributes
from _dependencies.spec import _make_dependency_spec


def _deep_replace_dependency(injector, current_attr, replace):

    spec = _make_dependency_spec(current_attr, replace.dependency)
    marker, attribute, args = spec
    attribute = _Attributes(attribute, replace.attrs)
    spec = (marker, attribute, args)

    for base in injector.__mro__:
        if base.__dependencies__.has(current_attr):
            base.__dependencies__.set(current_attr, spec)
        else:
            break
