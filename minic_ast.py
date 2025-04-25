from abc import ABC
from dataclasses import dataclass
from enum import auto, Enum
from typing import Optional, Tuple


INDENT = "    "


class Node(ABC):
    pass


class Expr(ABC):
    pass


@dataclass
class IntLit(Expr):
    value: int

    def __str__(self):
        return str(self.value)


@dataclass
class FloatLit(Expr):
    value: float

    def __str__(self):
        return str(self.value)


@dataclass
class CharLit(Expr):
    value: str

    def __str__(self):
        return self.value


@dataclass
class StringLit(Expr):
    value: int

    def __str__(self):
        return self.value


@dataclass
class Id(Expr):
    value: str

    def __str__(self):
        return self.value


class Op(Enum):
    PLUS = auto
    MINUS = auto
    TIMES = auto
    DIVIDE = auto
    ASSIGN = auto
    EQ = auto
    NEQ = auto
    LT = auto
    GT = auto
    LEQ = auto
    GEQ = auto

    def __str__(self):
        match self:
            case Op.PLUS:
                return "+"
            case Op.MINUS:
                return "-"
            case Op.TIMES:
                return "*"
            case Op.DIVIDE:
                return "/"
            case Op.ASSIGN:
                return "="
            case Op.EQ:
                return "=="
            case Op.NEQ:
                return "!="
            case Op.LT:
                return "<"
            case Op.GT:
                return ">"
            case Op.LEQ:
                return "<="
            case Op.GEQ:
                return ">="
            case _:
                return "???"


@dataclass
class Binop(Expr):
    lhs: Expr
    op: Op
    rhs: Expr

    def __str__(self):
        return f"({self.lhs} {self.op} {self.rhs})"


@dataclass
class FuncCall(Expr):
    func: Id
    args: list[Expr]

    def __str__(self):
        return f"{self.func}({', '.join(map(str, self.args))})"


@dataclass
class Array(Expr):
    values: list[Expr]

    def __str__(self):
        return f"[{', '.join(map(str, self.values))}]"


@dataclass
class Index(Expr):
    array: Expr
    index: Expr

    def __str__(self):
        return f"{self.array}[{self.index}]"


class Statement(Node):
    pass


@dataclass
class Block(Statement):
    body: list[Statement]

    def __str__(self):
        return body_str(self)


@dataclass
class ExprStmt(Statement):
    expr: Expr

    def __str__(self):
        return f"{self.expr};"


def body_str(s: Statement):
    def indent_body(s: Statement):
        return INDENT + ("\n" + INDENT).join(str(s).splitlines())

    match s:
        case Block([]):
            return " {}"
        case Block(stmts):
            stmt_str = "\n    ".join(map(indent_body, stmts))
            return f" {{\n    {stmt_str}\n{INDENT}}}"
        case _:
            return " \n" + INDENT + indent_body(s) + "\n" + INDENT


@dataclass
class If(Statement):
    cond: Expr
    body: Statement
    else_body: Optional[Statement] = None

    def __str__(self):
        if self.else_body:
            else_str = f" else{body_str(self.else_body)}"
        else:
            else_str = ""
        return f"if ({self.cond}){body_str(self.body)}{else_str}"


@dataclass
class While(Statement):
    cond: Expr
    body: Statement

    def __str__(self):
        return f"while ({self.cond}){body_str(self.body)}"


@dataclass
class Return(Statement):
    value: Optional[Expr] = None

    def __str__(self):
        if self.value:
            return f"return {self.value};"
        return "return;"


class Type(Node):
    pass


class Int(Type):
    def __str__(self):
        return "int"


class Float(Type):
    def __str__(self):
        return "float"


class Char(Type):
    def __str__(self):
        return "char"


class String(Type):
    def __str__(self):
        return "string"


@dataclass
class Func(Expr):
    return_type: Type
    name: Id
    args: list[Tuple[Type, Id]]
    body: list[Statement]

    def __str__(self):
        if self.body:
            body_str = f"{{\n    {'\n    '.join(map(str, self.body))}\n}}"
        else:
            body_str = "{}"
        return f"{self.return_type} {self.name}({', '.join(map(str, self.args))}) {body_str}"
