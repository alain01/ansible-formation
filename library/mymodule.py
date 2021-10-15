#!/usr/bin/python3

# Copyright: (c) 2021, Pierre  <psable@dawan.fr>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import *

# Utilisation des parametres et ajout de contition pour warning ou fail
def presentation(module):
    name = module.params['name']
    if name != "Pierre":
        #module.warn("WARNING : vous n'êtes pas Pierre")
        module.fail_json("FAILED: vous n'êtes pas Pierre ")
    type = module.params['type']
    return {"MYMODULE" : "Mon nom est : {} et mon type est : {}".format(name, type)}

def main():

    # Declaration des parametre du module
    parametres = {
      "name": {"required": True, "type": "str"},
      "type": {
          "default": "plouf",
          "choice": ['plouf', "plaf"],
          "type": 'str'
      }
    }

    # Interpretation des parametres
    module = AnsibleModule(argument_spec=parametres)
    module.exit_json(changed=False, meta=presentation(module))

if __name__ == '__main__':
    main()