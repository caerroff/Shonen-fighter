#ifndef PERSO_H
#define PERSO_H
#include <SFML\Graphics.hpp>
#include <iostream>

struct Sprite {
    int elements = 10; 
    bool tableau[];
};

class Perso {

    private: 
        std::string path; 
        std::string name; 
        bool orientation; //True if facingRight, False if facingLeft
        sf::Texture *currentSprite;
        Sprite sprites; 

    public: 
        Perso(std::string path, std::string name, bool orientation); //True (facingRight) by default 
        sf::Texture *getTexture(); 
}; 

#endif