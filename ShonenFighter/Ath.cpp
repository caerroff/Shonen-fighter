#include "Ath.hpp"

#include "iostream"
#include <SFML/Graphics.hpp>

Ath::Ath(int positionX) {
    this->posX = positionX;
    this->posY = -425;
    
    sf::Vector2f hpPosition(posX, posY);
    sf::Vector2f manaPosition(posX, posY + 50);
    
    sf::Color green(46, 239, 31);
    sf::Color blue(29, 228, 231);
    
    hp.setPosition(hpPosition);
    mana.setPosition(manaPosition);
    hp.setSize(sf::Vector2f(lengthHp, 30));
    mana.setSize(sf::Vector2f(300, 30));
    hp.setFillColor(green);
    mana.setFillColor(blue); 
}

void Ath::reduceHp() {
    this->lengthHp -= 30;
}

void Ath::setPosX(int positionX) {
    this->posX = positionX;
    hp.setPosition(posX, posY);
    mana.setPosition(posX, posY + 50);
}

/*
 draw : draw the ath on the scene
 */
void Ath::Draw(sf::RenderWindow& window) {
    window.draw(hp);
    window.draw(mana); 
}
