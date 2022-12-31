import argparse
import ast
import os.path
from pathlib import Path

import astpretty
import funcparser

parser = argparse.ArgumentParser(prog="parser", description="A trivial function parser")
parser.add_argument("file")

if __name__ == "__main__":
    args = parser.parse_args()
    parsed_file = args.file
    is_file = os.path.isfile(parsed_file)
    assert is_file, "the file is really a file"
    is_python_file = Path(parsed_file).suffix == ".py"
    assert is_python_file, "the file is really a Python file"

    with open(parsed_file, "r") as f:
        abstract_syntax_tree: ast.Module = ast.parse(f.read())
        assert len(abstract_syntax_tree.body) == 2, "Two AST nodes"
        func_def = abstract_syntax_tree.body[0]
        assert isinstance(func_def, ast.FunctionDef), "ast.FunctionDef Node"
        astpretty.pprint(func_def)
        func_call = abstract_syntax_tree.body[1]
        assert isinstance(func_call, ast.Expr), "ast.Expr Node"
        astpretty.pprint(func_call)

        funcparser.parse(func_def, func_call)
