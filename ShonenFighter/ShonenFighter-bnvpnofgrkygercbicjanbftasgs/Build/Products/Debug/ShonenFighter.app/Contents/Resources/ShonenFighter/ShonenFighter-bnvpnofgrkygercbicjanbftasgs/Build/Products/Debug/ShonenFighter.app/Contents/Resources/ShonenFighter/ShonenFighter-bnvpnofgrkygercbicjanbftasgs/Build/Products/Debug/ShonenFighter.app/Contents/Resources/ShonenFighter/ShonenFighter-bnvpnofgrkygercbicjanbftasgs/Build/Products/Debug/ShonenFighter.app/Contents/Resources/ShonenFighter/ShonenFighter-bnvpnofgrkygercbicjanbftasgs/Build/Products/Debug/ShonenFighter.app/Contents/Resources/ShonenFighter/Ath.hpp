#ifndef Ath_hpp
#define Ath_hpp

#include <SFML/Graphics.hpp>
#include "Player.hpp"

class Ath {
private:
    sf::RectangleShape hp;
    sf::RectangleShape mana;
    
    int lengthHp = 300; 
    
    int posX;
    
    int posY; 
    
public:
    Ath(int posX);

    void reduceHp(); 
    
    void Draw(sf::RenderWindow& window);
    void setPosX(int positionX); 
};

#include <stdio.h>

#endif /* Ath_hpp */
