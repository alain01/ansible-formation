class VagrantPlugins::ProviderVirtualBox::Action::Network

    def dhcp_server_matches_config?(dhcp_server, config)
  
      true
    end
  end
  
  Vagrant.configure("2") do |config|
    [
      ["master.formation.lan", "1024", 'ubuntu/focal64' ],
      ["srv01.formation.lan", "1024",  
    ].each do |vmname,mem,os|
      config.vm.define "#{vmname}" do |machine|
  
        machine.vm.provider "virtualbox" do |v|
          v.memory = "#{mem}"
          v.cpus = 1
          v.name = "#{vmname}"
        end
  
        machine.vm.box = "#{os}"
        machine.vm.hostname = "#{vmname}"
        config.vm.synced_folder "./", "/vagrant", id: "vagrant-root",
          owner: "vagrant",
          group: "vagrant",
          mount_options: ["dmode=775,fmode=664"]
        machine.vm.network "private_network", type: "dhcp"
        config.vm.provision "shell", inline: <<-SHELL
         echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIxOTxLaFREMdw7MJwpaTkkM9xXYkQmLhPyDTh0kmIDU vagrant@key" >> /home/vagrant/.ssh/authorized_keys
        SHELL
      end
    end
  end
  