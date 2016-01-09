
Allow to inject warning filters during `nosetest`.


Put the same arguments as `warnings.filterwarnings` in `setup.cfg` at the root of your project.
Separated each argument by pipes `|`, one filter per line.
Whitespace are stripped.

for example:
```
[nosetests]
warningfilters=default         |.*            |DeprecationWarning |notebook.*
               ignore          |.*metadata.*  |DeprecationWarning |notebook.*
               once            |.*schema.*    |UserWarning        |nbfor.*
               error           |.*warn.*      |DeprecationWarning |notebook.services.contents.manager*
```

If you prefer another name for the configuration file, you can tell nose to load
the configuration using the `-c` flag: run the tests with `nosetests -c nose.cfg`.
