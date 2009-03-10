from django.utils.translation import ugettext_lazy as _

class FormOptions():
    """
    FormOptions class gives Form extra properties 
    so we can build a generic form template and
    relieve the need to re-create a form, even more
    lazier then newforms.
    """
    (id, method, title, action, enctype, accept,
    accept_charset, cssclass, has_reset,
    include_help_text, submit_label, reset_label) = (None, None, None, 
    None, None, None, None, None, None, None, None, None)

    def __init__(self, id=None, method='POST', title=None, action='#', enctype=None, accept=None,
                 accept_charset=None, cssclass='form_wrapper', has_reset=False,
                 include_help_text=False, submit_label=_('Guardar'), reset_label=_('Cancelar')):

        if not action:
            raise ValueError('Action is not defined.')

        (self.id, self.method, self.title, self.action, self.enctype,
         self.accept, self.accept_charset, self.cssclass,
         self.has_reset, self.submit_label, self.reset_label,
         self.include_help_text) = (id, method, title, action, enctype,
         accept, accept_charset, cssclass,
         has_reset, submit_label, reset_label,
         include_help_text)
