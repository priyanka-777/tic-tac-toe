
#!/bin/bash
mv 'game.py' 'board'

sudo chmod +x 'board'
sudo cp 'board' '/usr/bin/'
alias 'board'='python3 board'


cd ..
sudo rm -r Tic_tac_toe


