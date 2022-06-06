#include <stdio.h>
#include "Characters.hpp"

Characters::Characters() {
    
}

/*
 setTabSprites : set the tab from a specific character (like Itachi, child class) to this tab (Characters)
                    This function allows to transfer the tab (datas of sprites), from children to mothers' class
 */
void Characters::setTabSprites(int *tabSprites) {
    for(int i = 0; i < lengthTab; i++) {
        this->tabSprites[i] = tabSprites[i];
    }
}

/*
 setIdCharacter : set the id of the character
 */
void Characters::setIdCharacter(int id) {
    this->idCharacter = id; 
}
