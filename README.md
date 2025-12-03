# True-Info — simple tool to obtain reliable information

[![Bandit](https://github.com/LuisGomes18/True-Info/actions/workflows/bandit.yml/badge.svg)](https://github.com/LuisGomes18/True-Info/actions/workflows/bandit.yml)

[![CodeQL](https://github.com/LuisGomes18/True-Info/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/LuisGomes18/True-Info/actions/workflows/github-code-scanning/codeql)

This project helps you search for information on a topic while automatically avoiding websites you consider unreliable (e.g., misinformation sites, denialist channels, or sources you prefer to block).

The focus here is practicality: non-technical users can operate the program through a menu, without touching any code.

## Getting started (quick)

* Open a terminal in the project folder.
* Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

* Install dependencies:

```bash
pip install -r requirements.txt
```

* Run the program:

```bash
python app.py
```

## Using the menu (step-by-step)

When the app starts, you’ll see a menu with simple options:

* `1 - Run search`: searches a topic and returns filtered results.
* `2 - Add domain to blacklist`: adds a website to the blocked list.
* `3 - Remove domain from blacklist`: removes a website from the blocked list.
* `4 - Activate blacklist list`: enables one of the pre-made lists (e.g., Brazil, Portugal).
* `5 - Deactivate blacklist list`: temporarily disables an active list.
* `0 - Exit`: closes the program.

The menu guides your input — just type the option number and follow the on-screen instructions.

## Where the lists are stored

* The site lists are located in the `data/` folder (`.txt` files, one domain per line).
* It is recommended to use the menu to update the lists so changes are saved automatically.

## Quick recommendations

* Always document why a site was blocked (e.g., reference link). Use Git history to record important changes.
* When in doubt, ask someone experienced in information verification to review the exclusions.

## Technical info and improvements

If you’re a developer or want to see technical suggestions (such as adding tests, formatting code, or turning the project into a package), check `todo.md` — it contains the recommended improvements.

## Help

If you need help, tell me what you tried and describe the issue — I can guide you step by step.

---

## Simplified README version for non-technical users.

## Technical section (quick)

For those who prefer straightforward technical instructions, here’s a short and simple summary.

* Requirements: `Python 3.8+` and `pip`.
* Open a terminal in the project folder.
* (Recommended) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

* Install dependencies:

```bash
pip install -r requirements.txt
```

* Run the program:

```bash
python app.py
```

## Quick tips for editing lists

* **Edit via menu:** run the program and use options 2–5 to add/remove/enable/disable lists without touching files.
* **Edit manually:** open the files in `data/` and add/remove domains (one per line). Commit the changes if you want to keep track of them.

## Ethics and responsibility

Filtering tools do not replace human verification. Use ethical, verifiable criteria when building exclusion lists. Avoid unjustified censorship; prefer public, replicable, and evidence-based criteria.

## Contributions

PRs are welcome. For policy changes related to filtering, describe criteria and evidence. For new features, include tests when possible.
