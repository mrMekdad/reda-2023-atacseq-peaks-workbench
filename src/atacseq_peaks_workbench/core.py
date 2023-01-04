"""Core workflow for ATACseq Peaks Workbench by Red@."""

PROJECT_NAME = "ATACseq Peaks Workbench"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
