# Julia-Python interop

This is a minimal example repo that can be used as the basis for a software project that has a Julia backend for performance and a Python frontend for some reason. Maybe you want cool Python packages like `fastapi`. Development of both happens in this monorepo.

Based on [PythonCall/juliacall](https://github.com/JuliaPy/PythonCall.jl).

### Running things
`make run` runs a Python script `demo_script.py` that passes a path to a JSON file to a python API function, which then calls a Julia function using that path. A computed float value is returned.

### Julia dependencies
Standard `Project.toml` and `Manifest.toml` setup using the pkg functionality in the Julia REPL. Read more [here](https://pkgdocs.julialang.org/v1/getting-started/).

### Python dependencies
A non-version controlled `requirements.txt`.

## Making changes to Julia code and seeing them in Python