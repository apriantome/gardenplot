# === Stage 55: Add a setting to disable colorized output ===
# Project: GardenPlot
USE_COLOR = not os.environ.get("NO_COLOR", "").strip()

if not USE_COLOR:
    _ORIGINAL = sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdout = sys.__stdout__

    def colorize(text, style=""):
        return text

    def style(text, style_=""):
        return text

    def green(text):
        return text

    def red(text):
        return text

    def yellow(text):
        return text

    def blue(text):
        return text

    def cyan(text):
        return text

    def bold(text):
        return text

    def dim(text):
        return text

    def reset(text):
        return text
