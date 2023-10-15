```
sudo apt install gnome-terminal
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
sudo apt update
sudo apt-get install ca-certificates curl gnupg
sudo apt autoremove
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo   "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world
sudo service docker start
sudo docker run hello-world
sudo docker run -it ubuntu bash
sudo docker pull ultralytics/yolov5
sudo docker images
sudo docker run -it ultralytics/yolov5
```
### File copy
```
From DockerContainer To LocalMachine

$docker cp containerId:/sourceFilePath/someFile.txt C:/localMachineDestinationFolder
#
From LocalMachine To DockerContainer

$docker cp C:/localMachineSourceFolder/someFile.txt containerId:/containerDestinationFile
```
