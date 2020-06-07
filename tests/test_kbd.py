import markdown
from kbdextension import KbdExtension

BRACKETS_TEXT = "I am a [[brackets]] example."
BRACES_TEXT = "I am a {{braces}} example."
PARENS_TEXT = "I am a ((parens)) example."


def get_html(text, **kwargs):
    return markdown.markdown(text, extensions=[KbdExtension(**kwargs)],)


def test_brackets_enabled():
    """ Confirm that the brackets syntax is enabled by default. """
    assert get_html(BRACKETS_TEXT) == "<p>I am a <kbd>brackets</kbd> example.</p>"


def test_brackets_disabled():
    """ Confirm that the brackets syntax is disabled on demand. """
    assert (
        get_html(BRACKETS_TEXT, enable_brackets=False)
        == "<p>I am a [[brackets]] example.</p>"
    )


def test_brackets_css():
    """ Confirm that custom css is applied to brackets syntax. """
    assert (
        get_html(BRACKETS_TEXT, brackets_css="custom-css")
        == '<p>I am a <kbd class="custom-css">brackets</kbd> example.</p>'
    )


def test_braces_disabled():
    """ Confirm that the braces syntax is disabled by default. """
    assert get_html(BRACES_TEXT) == "<p>I am a {{braces}} example.</p>"


def test_braces_enabled():
    """ Confirm that the braces syntax is enabled on demand. """
    assert (
        get_html(BRACES_TEXT, enable_braces=True)
        == "<p>I am a <kbd>braces</kbd> example.</p>"
    )


def test_braces_css():
    """ Confirm that custom css is applied to brackets syntax. """
    assert (
        get_html(BRACES_TEXT, enable_braces=True, braces_css="custom-css")
        == '<p>I am a <kbd class="custom-css">braces</kbd> example.</p>'
    )


def test_parens_disabled():
    """ Confirm that the parens syntax is disabled by default. """
    assert get_html(PARENS_TEXT) == "<p>I am a ((parens)) example.</p>"


def test_parens_enabled():
    """ Confirm that the parens syntax is enabled on demand. """
    assert (
        get_html(PARENS_TEXT, enable_parens=True)
        == "<p>I am a <kbd>parens</kbd> example.</p>"
    )


def test_parens_css():
    """ Confirm that custom css is applied to parens syntax. """
    assert (
        get_html(PARENS_TEXT, enable_parens=True, parens_css="custom-css")
        == '<p>I am a <kbd class="custom-css">parens</kbd> example.</p>'
    )
