#include "Perso.hpp"
#include <iostream>

Perso::Perso(std::string path, std::string name, bool orientation) {
    this->path = path; 
    this->name = name; 
    this->orientation = orientation; 

    sf::Texture *texture =(sf::Texture*) calloc(10, sizeof(sf::Texture)); 
    texture->loadFromFile(path); 
    //this->sprites.tableau[0] = texture; 
    this->currentSprite = texture; 
}

sf::Texture *Perso::getTexture() {
    return this->currentSprite; 
}