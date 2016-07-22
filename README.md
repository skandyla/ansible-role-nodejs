Ansible Role: Nodejs
=========

Install NodeJS with latest npm for RedHat and Debian systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

```
# Set the version of Node.js to install ("0.12", "4.x", "5.x", "6.x").
nodejs_version: "4.x"
nodejs_npm_global_packages: 
  - name: npm
```

Dependencies
------------

None.

Example Playbook
----------------

```
    - hosts: servers
      vars_files:
        - vars/main.yml
      roles:
         - { role: skandyla.nodejs }
```


License
-------

BSD

Author Information
------------------

Sergey Kandyla
