import pkg_resources
pkg_resources.declare_namespace(__name__)

FABRIC_TASK_MODULE = True

from fabric.api import put, sudo
import os
import sys

def add_user(user_to_add=None, path_to_key=None):
    """Completely initial a new user"""
    if not user_to_add:
        user_to_add = os.environ['USER']
    if not path_to_key:
        path_to_key = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa.pub')

    if not os.path.exists(path_to_key):
        print "ERROR!  Unable to find your key at: %s" % path_to_key
        sys.exit(1)

    replacements = {
        'user': user_to_add,
    }
    useradd(user_to_add)
    add_ssh_key_for(user_to_add, path_to_key)
    reown_home_as(user_to_add)
    add_sudoer_user(user_to_add)

def useradd(user_to_add):
    """Call useradd on the remove system"""
    replacements = {
        'user': user_to_add,
    }
    sudo("""/usr/sbin/useradd \
            --home-dir /home/%(user)s \
            --create-home \
            --user-group \
            --shell /bin/bash \
            --password "SrmZ9buSJKlxk" \
            %(user)s""" % replacements)

def add_ssh_key_for(user, path_to_key):
    """Add the SSH public key for a provided user"""
    replacements = {
        'user': user,
    }
    sudo("mkdir /home/%(user)s/.ssh" % replacements)
    put(path_to_key, "~/%(user)s.pub" % replacements)
    sudo("cat ~/%(user)s.pub | sudo tee /home/%(user)s/.ssh/authorized_keys2" % replacements)
    sudo("ssh-keygen -f /home/%(user)s/.ssh/id_rsa -P ''" % replacements)
    sudo("chmod 0700 /home/%(user)s/.ssh" % replacements)
    sudo("chmod 0600 /home/%(user)s/.ssh/id_rsa" % replacements)
    sudo("chmod 0600 /home/%(user)s/.ssh/authorized_keys2" % replacements)
    sudo("chmod 0644 /home/%(user)s/.ssh/id_rsa.pub" % replacements)

def reown_home_as(user):
    """Set a directory as owned by a provided user"""
    sudo("chown -R %(user)s.%(user)s /home/%(user)s" % {'user': user})

def add_sudoer_user(user):
    """Make sure the user is part of the admin group"""
    sudo("usermod --append --groups admin %(user)s" % {'user': user})

def remove_user(user_to_remove=None, remove_files=False):
    """Remove the user, optionally removing all files"""
    if not user_to_remove:
        user_to_remove = os.environ['USER']
    sudo("/usr/sbin/userdel %s" % user_to_remove)
    if remove_files:
        sudo("rm -rf /home/%s" % user_to_remove)

