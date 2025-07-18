# CSVConceptMapEditor

A simple Tkinter-based desktop application for editing CSV files and visualizing them as concept maps. This tool allows you to open, edit, and save CSV files in a text editor interface, then generate concept map visualizations in PNG, SVG, or PDF formats using the [ConceptMap](csv_concept_map.py) class.

Propositions are used extensively in my book "Generative Analysis". This simple editor was created to help my readers visualize propositions as Concept Maps. Propositions are perfect inputs to Generative AI for the generation of code any many other artefacts.

Propositions are defined as:

`concept1 linking words concept2`

They are stored comma delimited in CSV files as follows:

`concept1, linking words, concept2`

Here is an example proposition CSV file for a Concept Map about Mind Mapping (`mind_mapping.csv`), which is another one of our favorite techniques:

```Mind Map, comprising, central idea
Mind Map, hierarchic, structure
structure, comprising, branches
branches, comprising, pictures
branches, comprising, text
branches, representing, ideas
ideas, associated via, branches
central idea, associated via, branches
information, using, Mind Map
Mind Mapping, captures, information
Mind Mapping, communicates, information
Mind Mapping, recovers, information
Mind Mapping, generates, information
Mind Mapping, integrates, information
Mind Mapping, invented by, Tony Busan 1970s
Mind Mapping, principle, picture speaks 1000 words
Mind Mapping, uses, colors
Mind Mapping, uses, one word per branch
Mind Mapping, uses, imagination
Mind Mapping, stimulates, imagination
Mind Mapping, associates, ideas
Mind Mapping, associates, concepts
Mind Mapping, similar to,brain
brain, associates, concepts
brain, associates, ideas
Mind Mapping, similar to, Concept Mapping
Concept Mapping, invented by, Prof. Joseph D. Novak 1970s
```

---

## Features

- **Open and edit CSV files** in a plain text editor with syntax-friendly font.
- **Cut, copy, and paste** support via context menu and keyboard shortcuts.
- **Save** your changes directly back to CSV.
- **Generate concept map visualizations** from your CSV:
  - Export as PNG, SVG, or PDF with one click.
- **Simple, intuitive interface** built with Tkinter.

---

## Getting Started

### Prerequisites

- Python 3.7 or newer
- The `csv_concept_map.py` module (must be present in the same directory)
- Additional dependencies for concept map rendering (as required by `ConceptMap`, e.g., `graphviz`)

### Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/CSVConceptMapEditor.git
   cd CSVConceptMapEditor
   ```

2. **Install dependencies:**

   - Install Python requirements (if any, as specified by `csv_concept_map.py`).
   - For concept map rendering, you may need [Graphviz](https://graphviz.gitlab.io/download/) installed on your system.

3. **Run the application:**

   ```bash
   python csv_concept_map_editor.py
   ```

---

## Usage

1. **Open a CSV file**  
   Click "Open CSV" and select your CSV file. The contents will appear in the editor.

2. **Edit the CSV**  
   Make changes directly in the text area. Use right-click or `Ctrl+X/C/V` for cut/copy/paste.

3. **Save your changes**  
   Click "Save CSV" to write your edits back to disk.

4. **Generate Concept Map**  
   Click one of the "Concept map" buttons (PNG, SVG, PDF) to render a concept map from your CSV file. The visual will be saved in the same directory as your CSV.

---

## Keyboard Shortcuts

- `Ctrl+X` — Cut
- `Ctrl+C` — Copy
- `Ctrl+V` — Paste

---

## File Structure

```
.
├── csv_concept_map_editor.py   # Main application (this file)
├── csv_concept_map.py          # ConceptMap class for visualization (required)
└── README.md                   # Project documentation
```

---

## Example

  
*Edit your CSV and generate a concept map with a single click!*

---

## License

This project is open source. See [LICENSE](LICENSE) for details.

---

## Acknowledgments

- Built with [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- Concept map rendering powered by [Graphviz](https://graphviz.gitlab.io/) (via `ConceptMap`).
- Some code was generated by Perplexity.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## Contact

For questions or suggestions, please open an issue on GitHub.

Sources
[1] README.md - rochacbruno/python-project-template - GitHub https://github.com/rochacbruno/python-project-template/blob/main/README.md
[2] An awesome README template to jumpstart your projects! - GitHub https://github.com/othneildrew/Best-README-Template
[3] Creating Great README Files for Your Python Projects - Real Python https://realpython.com/readme-python-project/
[4] README.md - azavea/python-project-template - GitHub https://github.com/azavea/python-project-template/blob/master/README.md
[5] How to Write a README for Your Beginner Python Project - YouTube https://www.youtube.com/watch?v=12trn2NKw5I
[6] Make a README https://www.makeareadme.com
[7] python-package-template/README.md at main - GitHub https://github.com/allenai/python-package-template/blob/main/README.md
[8] Project-README-template.md - GitHub https://github.com/sfbrigade/data-science-wg/blob/master/dswg_project_resources/Project-README-template.md
