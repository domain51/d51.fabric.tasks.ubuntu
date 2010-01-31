d51.fabric.tasks.ubuntu
=======================
Fabric tasks for handling basic management tasks on Ubuntu


Requirements
------------
This has been built to be used with the 1.0a version of the [Fabric fork][]
maintained by [Travis Swicegood][].  It might be usable with other versions of
Fabric, but your mileage may vary.


Usage
-----
You can import the individual tasks into your current fabfile:

    from d51.fabric.tasks.ubuntu import *

Or, you can import the module and execute the tasks that way:

    from d51.fabric.tasks import ubuntu


Tasks
-----
* add\_user
* remove\_user


[Fabric fork]: http://github.com/tswicegood/fabric
[Travis Swicegood]: http://www.travisswicegood/
