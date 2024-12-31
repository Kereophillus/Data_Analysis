class Display:
    """Utility to display HTML representation of multiple objects in Jupyter notebooks."""

    TEMPLATE = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>
    {1}
    </div>
    """

    @staticmethod
    def display(*args):
        """
        Display multiple objects in Jupyter notebooks.

        Args:
            *args: Variable length argument list of tuples (label, object).
                   Example: ("Label", object)
        """
        from IPython.core.display import display, HTML

        html_parts = []
        for label, obj in args:
            if hasattr(obj, '_repr_html_'):
                html_parts.append(Display.TEMPLATE.format(label, obj._repr_html_()))                
            else:
                html_parts.append(Display.TEMPLATE.format(label, repr(obj)))
                
        display(HTML("\n".join(html_parts)))
