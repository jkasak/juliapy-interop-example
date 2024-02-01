from pathlib import Path
from juliacall import Main as jl

# References from the root of the repository
repo_root_path = Path(__file__).parent.parent
julia_module_path = str(repo_root_path / "julia_src" / "MyJuliaModule.jl")

jl.Pkg.activate(str(repo_root_path), io=jl.devnull)
jl.seval(f'include("{julia_module_path}")')

# Functions in MyJuliaModule are now in this namespace
julia_module = jl.MyJuliaModule

