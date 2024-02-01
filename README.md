# Julia-Python interop

This is a minimal example repo that can be used as the basis for a software project that has a Julia backend for performance and a Python frontend for some reason.

Based on [PythonCall/juliacall](https://github.com/JuliaPy/PythonCall.jl).

The things you want Python for probably exist also in Julia, but if you want a specific surface layer using good python packages like `fastapi`, then the option for using a Python frontend exists.

### Julia dependencies
Standard `Project.toml` and `Manifest.toml` setup using the pkg functionality in the Julia REPL. Read more [here](https://pkgdocs.julialang.org/v1/getting-started/).

### Python dependencies
A non-version controlled `requirements.txt`.

## Running things
`make run`

## Making changes