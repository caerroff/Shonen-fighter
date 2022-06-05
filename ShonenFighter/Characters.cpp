#include <stdio.h>
#include "Characters.hpp"

Characters::Characters() {
    
}

void Characters::setTabSprites(int *tabSprites) {
    for(int i = 0; i < lengthTab; i++) {
        this->tabSprites[i] = tabSprites[i];
    }
}

void Characters::setIdCharacter(int id) {
    this->idCharacter = id; 
}
