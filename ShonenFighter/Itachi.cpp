#include "Itachi.hpp"

Itachi::Itachi() {
    this->setIdCharacter(1);
    
    int spritesItachi[100];
    
    spritesItachi[0] = 7;
    spritesItachi[1] = 6;
    spritesItachi[2] = 1;
    spritesItachi[3] = 1;
    spritesItachi[4] = 1;
    
    this->setTabSprites(spritesItachi); 
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

