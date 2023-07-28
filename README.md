# raspberry_projects
basic raspberry control

Install wiringPi

    gpio -v

    gpio readall

    sudo apt-get update

    sudo apt-get upgrade

    on rpi3:
    sudo apt-get install wiringpi

    on rpi4:
    sudo apt install -y make
    sudo apt install build-essential
    git clone https://github.com/WiringPi/WiringPi.git
    sudo ./build

    cd /<path>/wiringPi
    ./build

    (GPIO numbering: https://www.aranacorp.com/en/program-your-raspberry-pi-with-c/)

    find pinout with this command:
    gpio -v
    gpio readall

    g++ test.cc -o test -lwiringPi



    