# 📚 rdflib-serializer

**rdflib-serializer** is a simple command-line tool to parse and serialize RDF data using [rdflib](https://github.com/RDFLib/rdflib).
It supports reading from files or stdin, flexible input and output formats, and shell tab completion for an improved CLI experience.

Especially useful to prune unused prefixes from turtle files:

```shell-session
$ echo "@prefix foo: <urn:uri:foo/> .
@prefix bar: <urn:uri:bar/> .
foo:a a foo:A .
" | rdflib-serializer -
@prefix foo: <urn:uri:foo/> .

foo:a a foo:A .
```

---

## 🚀 Features

- Read RDF data from file or stdin (`-`)
- Support multiple RDF formats: `turtle`, `xml`, `json-ld`, `n3`, `nquads`, etc.
- Convert between different RDF formats
- Output serialized RDF content to stdout
- Tab-completion for commands and format options (using `argcomplete`)

---

## 📦 Installation

You have two easy options:

### 1. Install in a virtual environment (with [uv](https://github.com/astral-sh/uv))

```bash
# Create and activate a virtual environment
uv venv
source .venv/bin/activate

# Install rdflib-serializer locally
uv pip install -e .
```

✅ Now the `rdflib-serializer` command is available inside your virtual environment.

---

### 2. Install globally with pipx

```bash
# Make sure pipx is installed
pip install --user pipx
pipx ensurepath

# Install rdflib-serializer globally
pipx install .
```

✅ Now the `rdflib-serializer` command is available everywhere in your system.

---

## ⚡️ Enabling Shell Completion

To activate tab-completion (especially for `--source-format` and `--target-format`), run:

### Bash:

```bash
register-python-argcomplete rdflib-serializer >> ~/.bashrc
source ~/.bashrc
```

### Zsh:

```bash
register-python-argcomplete rdflib-serializer >> ~/.zshrc
source ~/.zshrc
```

After setup, you can tab-complete options like:

```bash
rdflib-serializer --source-format <TAB>
rdflib-serializer --target-format <TAB>
```

You will see available formats like `turtle`, `xml`, `json-ld`, etc.

---

## 🛠 Usage

Parse and serialize a file:

```bash
rdflib-serializer myfile.ttl
```

Parse from stdin:

```bash
cat myfile.ttl | rdflib-serializer -
```

Convert a file from Turtle to JSON-LD:

```bash
rdflib-serializer myfile.ttl -s turtle -t json-ld
```

Convert RDF/XML to Turtle:

```bash
rdflib-serializer myfile.rdf -s xml -t turtle
```

List available input formats manually:

```bash
rdflib-serializer --help
```

---

## ✨ Supported Formats

- `turtle`
- `xml`
- `n3`
- `nt`
- `trig`
- `nquads`
- `json-ld`
- `rdfa`

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.
