from inplaceeditform.fields import BaseAdaptorField


class MyAdaptor(BaseAdaptorField):
    @property
    def name(self):
        return 'myadaptor'