# Clean Code Guidelines

### Names
-	Choose descriptive/unambiguous names
-	No noise words like “product_info”, just use “product”
-	Use pronounceable names (“strptime” should be “parse_datetime_from_string”)
-	Magic numbers should be named constants.
-	No prefixes or type information. (so no df_customers)
-	Length of variable name is proportional to the scope they are used in.
-	For Classes and Functions it’s the opposite (larger scope means smaller names).

### Readability
-	Introduce explanatory variables (only purpose is to explain)
-	Replace conditions (in if- or loop-statements) by functions.
-	No repetition or duplication of code.
-   Use type annotations (enforce them with mypy).

### Functions
-	Small. How small? 
     - Do one thing.
     - All statements are of the same level of abstraction. One level lower than the function itself.
     - Keep extracting methods until the only thing left to extract is the function itself.
-	It will automatically turn out to roughly 7 lines max.
-	Prefer fewer arguments. Use classes, or data structures to reduce the number of arguments.
-	Have no side effects. (Like saving files?)
-	When calling functions, write all arguments explicitly.

### Comments
-	Express yourself in code first.
-	Only if the code can’t describe its purpose, use comments to clarify the intent of the code.
-	Don’t be redundant or add obvious noise.
-	Don’t comment out code, we have git for this.
-	Docstrings and arguments description, only if necessary. 

### Style Guide
-	Follow standard conventions (like pep8, …)
-	Enforce it with tooling (like flake8, …)

### Imports
-	All imports at the top.
-	No relative imports.
-	Order them alphabetically and first in modules, sub-imports, project imports.
-	Use isort to enforce this.

### Tests
-	One assert per test.
-	Fast.
-	Independent.
-	Repeatable.
