# raspberry_projects
basic raspberry control

Install wiringPi
    gpio -v
    gpio readall
    sudo apt-get update
    sudo apt-get upgrade
    git clone git://git.drogon.net/wiringPi

    cd /<path>/wiringPi
    ./build

    (GPIO numbering: https://www.aranacorp.com/en/program-your-raspberry-pi-with-c/)

    find pinout with this command:
    gpio readall

    gcc test.cc -o test -lwiringPi