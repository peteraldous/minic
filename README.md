% Mini-C lexer and parser

# Introduction

This code implements a simple lexer and parser for Mini-C, a small C-like language. It generates an AST as specified in `minic_ast.py`.

# Requirements

This parser uses sly. `pip` is the easiest way to install it.

# Lexical specification

The following token types are supported:

- Keywords (if, else, while, int, float, char, string, return),
- Identifiers (begins with an alphabetic or underscore character and then has zero or more alphanumeric or underscore characters),
- Int literals (one or more digits),
- Float literals (optional digits, a period, and then at least one digit),
- Char literals (enclosed in `''`; allowable escape sequences are `\` followed by `\`, `n`, `r`, `t`, or `'`),
- String literals (enclosed in `""`; allowable escape sequences are `\` followed by `\`, `n`, `r`, `t`, or `"`),
- Arithmetic operators (`+`, `-`, `*`, `/`, `=`, `==`, `<`, `>`, `<=`, and `>=`),
- Punctuation (`;`, `,`, `(`, `)`, `[`, `]`, `{`, and `}`),

# Grammar

A Mini-C program is a sequence of function definitions. Names must be unique and one must be named `main`.

The following grammar is presented in a modified BNF, where * and + are interpreted as in regular expressions.

```
Program := Func*

Func := Type Id ( ParameterList ) { Statement+ }

Type := 'int' | 'float' | 'char' | 'string'

ParameterList := λ | Id | ParameterList , Id

Statement :=
    Expr ; |
    if ( Expr ) Statement |
    if ( Expr ) Statement else Statement |
    while ( Expr ) Statement |
    return; |
    return Expr; |
    { Statement* }

Expr :=
    <intlit> |
    <floatlit> |
    <charlit> |
    <stringlit> |
    Expr <binop> Expr |
    ( Expr ) |
    Id ( ExprList ) |
    [ ExprList ] |
    Expr [ Expr ]

ExprList := λ | Expr | Arglist , Expr
```

# Semantics

There are no booleans in Mini-C. Numeric values are false if zero and true otherwise.

There is a built-in `print` function, which any code can call. It should simply print the value to STDOUT.

There are no declarations in Mini-C. Assignment creates a variable if there is none.

# Errata

At present, all operators print as `+`. This will be remedied soon.
