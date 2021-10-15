#!/usr/bin/python3

# Copyright: (c) 2021, Pierre  <psable@dawan.fr>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import *

def main():

    module = AnsibleModule(argument_spec={})
    response = {"result" : "hello world"}
    module.exit_json(changed=False, meta=response)

if __name__ == '__main__':
    main()