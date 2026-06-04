# Zen CLI

**Zen** is a minimalist, opinionated project management tool designed for the terminal. It’s built for developers who believe that project orchestration shouldn't get in the way of the code.

---

## The Philosophy
Zen isn't trying to be a full-blown IDE or a complex project management suite. It exists because managing boilerplate project structures, Git syncs, and workspace switching often breaks the "flow" of development. Zen keeps your workspace organized, automated, and right where it belongs—in your terminal.

## Why Zen?
Zen isn't another CLI tool that adds complexity to your workflow. It reduces the cognitive load of managing multiple projects, keeping your environment consistent whether you're working on a Django backend or a simple Python script.

## Key Features
* **Rapid Boilerplate:** Standardized project creation across different stacks (Django, Python, Frontend, etc.).
* **Smart Sync:** Keep your local development environments synchronized across multiple machines without the bloat of heavy cloud tools.
* **Minimalist UI:** Built with `Rich`, Zen provides a clean, distraction-free visual experience.
* **Performance First:** Built using Python 3.12, designed for sub-second responses.
* **Human-Centric Stats:** Tracks your coding sessions with a focus on deep work, not just metrics.

## Technical Stack
* **Core:** Python 3.12.3
* **Environment:** Linux (Debian-based recommended)
* **Dependencies:**
    * `Rich`: Terminal formatting and UI elements.
    * `Questionary`: Interactive, intuitive CLI prompts.
    * `Pyfiglet`: Terminal typography.

## Quick Start
*Prerequisites: Ensure you have Python 3.12+ installed.*

```bash
# Clone the repository
git clone https://github.com/ibrahim-sisar/zen.git

# Install dependencies
pip install -r requirements.txt

# Run Zen
python3 zen.py
```
## Contributing
Zen is a tool born from personal necessity, but it is built to grow. If you find yourself constantly battling the same workspace setup issues, your input is more than welcome.

**How to contribute:**
  - Report Issues: Found a bug? Open an issue.
  - Feature Requests: Have a "Zen-like" way to improve workflow? Let’s discuss it.
  - Pull Requests: Check the Todo list in the header. Keep it clean, keep it minimalist.
Please ensure your code follows the established style and includes tests if you're introducing new logic.

Built by Ibrahim Said Abu Al-Roos
License: MIT
