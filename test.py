import markdown
from kbdextension import KbdExtension

kbd_keyboard = markdown.markdown(
    "Press the [[Enter]] key!",
    extensions=[KbdExtension(brackets_css="custom-brackets-kbd")],
)
kbd_button = markdown.markdown(
    "Click the {{Search}} button!",
    extensions=[KbdExtension(enable_braces=True, braces_css="custom-braces-kbd")],
)
kbd_menu = markdown.markdown(
    "Click the ((File)) menu!",
    extensions=[KbdExtension(enable_parens=True, parens_css="custom-parens-kbd")],
)

print(kbd_keyboard)
print(kbd_button)
print(kbd_menu)
