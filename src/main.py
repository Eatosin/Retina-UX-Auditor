from fasthtml.common import fast_app, Titled, Div, P

app, rt = fast_app()


@rt("/")
def get():
    return Titled("Retina", Div(P("System Online")))
