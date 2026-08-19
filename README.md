# MySQL Learning Notebook

Personal study notes and runnable examples created while preparing for MySQL. The repository is centered on an interactive Jupyter notebook and includes a small Python/MySQL connector example, a regex reference, and supporting diagrams.

(YESSS This is AI, Don't judge me guys)

The repository takes you through some advanced concepts too, which is more than enough to get a FAANG job but pls practise else no interview passing.

## Contents

- [Learning path](#learning-path)
- [Repository index](#repository-index)
- [Getting started](#getting-started)
- [Database prerequisites](#database-prerequisites)
- [Security note](#security-note)
- [Illustrations](#illustrations)

## Learning path

1.  Start with [MySQL 101](sql_learning.ipynb), including connecting to a server, inspecting databases and tables, and switching databases.
2.  Review MySQL statement categories, especially DDL, and work through the notebook's SQL syntax and examples.
3.  Use the notebook's query examples to practice filtering, aggregation, joins, date and string operations, NULL handling, conditional expressions, and set operations.
4.  Continue with subqueries, including scalar, row, table, correlated, and non-correlated forms.
5.  Study transactions and database administration topics such as savepoints, rollback, users, `GRANT`, and `REVOKE`.
6.  Finish with advanced topics such as window functions and partitioning, including the practical limits of partition indexes.
7.  Use the [regex cheat sheet](regex.html) when working with pattern matching and regular expressions.

## Repository index

| Path                                     | Purpose                                                                                                                                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [sql_learning.ipynb](sql_learning.ipynb) | Main MySQL tutorial and practice notebook. It contains SQL examples, explanatory notes, query output, subquery guidance, transaction exercises, permissions, window functions, and partitioning notes. |
| [mysql_python.py](mysql_python.py)       | Minimal `mysql.connector` example that connects to a local MySQL server, queries `UBER.Accounts`, prints rows, and closes the connection.                                                              |
| [regex.html](regex.html)                 | Browser-friendly regex cheat sheet covering anchors, wildcards, quantifiers, character classes, grouping, alternation, digit/word/whitespace classes, and boundaries.                                  |
| [pyproject.toml](pyproject.toml)         | Python project metadata and dependencies for Jupyter, `ipython-sql`, MySQL Connector/Python, and table output.                                                                                         |
| [uv.lock](uv.lock)                       | Locked Python dependency versions generated for the project environment.                                                                                                                               |
| [.python-version](.python-version)       | Selects Python 3.13 for the project.                                                                                                                                                                   |
| [Illustrations](Illustrations/)          | Diagrams and screenshots supporting permissions, transactions, window functions, partitioning concepts, and SQL set relationships.                                                                     |

## Getting started

The project targets Python 3.13 and uses a local MySQL server.

1.  Install Python 3.13 and MySQL Server. Make sure the MySQL service is running.
2.  Create or activate the project environment. With `uv`:

    ```powershell
    uv sync
    uv run jupyter notebook
    ```

    Alternatively, install the dependencies from [pyproject.toml](pyproject.toml) into another Python 3.13 environment.

3.  Open [sql_learning.ipynb](sql_learning.ipynb) in Jupyter or VS Code.
4.  In the first connection cell, replace the connection URL with the credentials and database used by your local server.
5.  Run the notebook cells from top to bottom. Several cells expect sample databases such as `sakila`, `world`, or a locally created `UBER` database.

To run the Python example directly:

```powershell
uv run python mysql_python.py
```

## Database prerequisites

The examples were written against MySQL and use the `mysql+mysqlconnector` SQLAlchemy URL through `ipython-sql`. The notebook's recorded outputs reference databases including:

- `sakila` for relational query practice
- `world` for sample geography data
- `UBER` and `system_demo` for locally created exercises

Sample databases and local tables are not included in this repository. Queries that depend on them will need equivalent schemas and data before they can be rerun successfully. Notebook outputs are retained as study notes, so the displayed results may differ from a fresh local run.

## Security note

The notebook and [mysql_python.py](mysql_python.py) contain example local credentials (`root`/`root`) and a local connection target. Do not use these values outside a disposable development database. Before sharing or deploying the code, replace them with environment variables or another secret-management approach, and use a least-privileged MySQL account.

## Illustrations

The `Illustrations/` directory contains the visual references used alongside the notes:

- [sql_venn_diagram.png](Illustrations/sql_venn_diagram.png): SQL set relationships
- [window_functions.png](Illustrations/window_functions.png): window-function reference
- [savepoint.png](Illustrations/savepoint.png) and [Rollback.png](Illustrations/Rollback.png): transaction control
- [user_create.png](Illustrations/user_create.png), [grant_access.png](Illustrations/grant_access.png), [revoke_access.png](Illustrations/revoke_access.png), and [revoke_implemented.png](Illustrations/revoke_implemented.png): user and privilege management
- [Command_line_execution.png](Illustrations/Command_line_execution.png): command-line execution reference
