import ast


def parse(func_def: ast.FunctionDef, func_expr: ast.Expr) -> None:
    assert isinstance(func_expr.value, ast.Call), "ast.Call Node"

    ##### 在这里实现你的逻辑