#!/bin/bash

function setup_fun {
    cd "./Pyramid_Server"
    export VENV=~/env
    echo "[+] Creation of the virtual environment.." && python3 -m venv $VENV
    echo "[+] Installation of the project.. " && $VENV/bin/pip install -e . > /dev/null
    echo "[+] Traceback mode ? [y] or [n]"
    read choix
    if [ "$choix" = "y" ]; then
        $VENV/bin/pserve development.ini --reload | echo "[+] Done ! Project available here: http://127.0.0.1:6543"
    elif [ "$choix" = "n" ]; then
        echo "[+] Done ! Project available here: http://127.0.0.1:6543"
        $VENV/bin/pserve development.ini > /dev/null 2>&1
    else
        echo "[+] Invalid !"
    fi
}

setup_fun
