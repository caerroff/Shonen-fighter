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

