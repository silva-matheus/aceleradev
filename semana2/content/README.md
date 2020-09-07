# Artigos
## Minimally Sufficient Pandas

*What is minimally sufficient Pandas*

* It is a small subset of the library that is sufficient to accomplish nearly everything that it has to offer.
    * Your code will be simple, explicit, straightforward, and boring
    * You will choose one obvious way to accomplish a task
    * You will use this obvious way every single time
    * You won’t have to retain as many commands in working memory
    * Your code will be easier to understand by others and by you
* It allows you to focus on doing data analysis and not the syntax

*Standardizing commom tasks*

Standardize your code to follow just one pattern, principally if you are working with other people.

*No Tricks*
Avoid to use tricks for doing any task. Prefer do that on right way, even if it's more verbose.

## Why and How to use Pandas with Large Data

Use Pandas or Numpy directly is a matter of choice, both have their pros and cons, but most importantly is how we use it.

* Aways you have a large dataset, read it with chuncks and then concat these chuncks to form your work dataset;
* Filter the unimportant features;
* Change dtypes(e.g change a float64 for a float32) for save memory;
    * PS: Analyse your problem first to now for sure that you can do that!
