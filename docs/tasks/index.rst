Tasks
=====

add_user
--------
Completely initializes a new user.  It takes two optional parameters:

``user_to_add``
    The name of the user to add.  If not provided, ``add_user`` assumes you're
    adding a new user of the same name as the current user.

``path_to_key``
    The path to the SSH public key for the user that is being added.  If not
    provided, ``add_user`` assumes it is ``~/.ssh/id_rsa.pub``.

remove_user
-----------
Removes a user using ``userdel`` and optionally removing their home directory.
It takes two optional parameters:

``user_to_remove``
    The name of the user to remove.  If not provided, ``remove_user`` assumes
    you're removing the remote user of the same name as the current local user.

``remove_files``
    A boolean that defaults to ``False``.  If ``True``, ``remove_user`` also
    removes the home directory for the user after calling ``userdel``.

Warning
^^^^^^^
Be very careful with this task.  Calling it with ``remove_files=True`` calls
``rm -rf`` on the user's home directory.  If you don't know what that means, you
should **not** be using this task. [#]_

Plumbing Tasks
--------------
These are tasks that are here to support the main tasks.  They're exposed in
case you want to use them to build larger pieces tasks, such as the main tasks
above.

add_ssh_key_for
^^^^^^^^^^^^^^^

add_sudoer_user
^^^^^^^^^^^^^^^

reown_home_as
^^^^^^^^^^^^^

useradd
^^^^^^^

.. rubric:: Footnotes

.. [#] It's worth noting, if you *really* don't know or understand what ``rm
         -rf`` does, you probably should not be using any of these tasks.
