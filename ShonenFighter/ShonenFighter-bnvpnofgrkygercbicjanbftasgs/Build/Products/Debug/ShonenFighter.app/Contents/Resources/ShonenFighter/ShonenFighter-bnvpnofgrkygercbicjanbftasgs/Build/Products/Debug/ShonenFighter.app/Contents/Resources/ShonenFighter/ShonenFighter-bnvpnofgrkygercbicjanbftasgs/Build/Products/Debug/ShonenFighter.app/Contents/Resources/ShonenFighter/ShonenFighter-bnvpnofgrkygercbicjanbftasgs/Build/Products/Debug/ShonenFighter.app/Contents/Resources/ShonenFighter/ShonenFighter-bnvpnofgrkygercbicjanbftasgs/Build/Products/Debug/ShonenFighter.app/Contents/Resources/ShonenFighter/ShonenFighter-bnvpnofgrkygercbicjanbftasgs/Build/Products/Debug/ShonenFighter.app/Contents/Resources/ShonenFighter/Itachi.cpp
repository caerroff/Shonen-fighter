#include "Itachi.hpp"
#include <iostream>

Itachi::Itachi() {
    this->setIdCharacter(1);
    
    int spritesItachi[100];
    
    spritesItachi[0] = 7; //Idle
    spritesItachi[1] = 6; //Run
    spritesItachi[2] = 1; //Jumping
    spritesItachi[3] = 1; //Falling
    spritesItachi[4] = 1; //Blocking
    spritesItachi[5] = 1; //Molding
    spritesItachi[6] = 2; //Kunai Throwing
    spritesItachi[7] = 3; //Damaged (taking damages)
    spritesItachi[8] = 4; //Combo 1
    spritesItachi[9] = 5; //Combo 2
    
    this->setTabSprites(spritesItachi);
    
    //this->checkTab();
}

/*
 setCharactersSprites : Give the tabSprites of Itachi to his mother (Characters), to charge it if the player
                            wants to play Itachi
 */
void Itachi::setCharactersSprites(int tabSprites []) {
    for(int i = 0; i < getLengthTab(); i++) {
        tabSprites[i] = this->getValueTabSprite(i); 
    }
}
