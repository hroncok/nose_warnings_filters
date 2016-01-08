
Allow to inject warning filters during nosetest.


Put the the same arguments as `warnings.filterwarnings` in `nose.cfg` separated by pipes `|`.
Whitespace are stripped.

for example:
```
[nosetests]
warningfilters=default         |.*            |DeprecationWarning |notebook.*
               ignore          |.*metadata.*  |DeprecationWarning |notebook.*
               once            |.*schema.*    |UserWarning        |nbfor.*
               error           |.*warn.*      |DeprecationWarning |notebook.services.contents.manager*
```

run the tests with `nosetests -c nose.cfg`
