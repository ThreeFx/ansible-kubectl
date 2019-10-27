kubectl
=========

Ansible role to install kubectl and setup zsh integration

Requirements
------------

None.

Role Variables
--------------

| Variable Name | Default Value | Description |
--------------- |---------------|--------------
`kubectl_user` | `"{{ ansible_user_id }}"` | Use for which to install kubectl

Dependencies
------------

None.

## Optional

Works well with my [unbound](https://github.com/ThreeFx/unbound) role.

Example Playbook
----------------

See `molecule/default/playbook.yml`.

License
-------

BSD

Author Information
------------------

Find me on [GitHub](https://github.com/ThreeFx).


Dependencies
------------

* [ansible-zsh](https://github.com/ThreeFx/ansible-zsh)

Example Playbook
----------------

See `molecule/default/playbook.yml`.

License
-------

BSD

Author Information
------------------

Find me on [GitHub](https://github.com/ThreeFx).
