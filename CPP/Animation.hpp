#ifndef ANIMATION_H
#define ANIMATION_H
#include <SFML\Graphics.hpp>

class Animation {

    private: 
        sf::Vector2u imageCount; 
        sf::Vector2u currentImage; 

        float totalTime; 
        float switchTime; 

        int nbSprites[100]; 
        int numAnime; 

    public: 
        Animation(sf::Texture* texture, sf::Vector2u imageCount, float switchTime); 
        sf::IntRect uvRect; 
        void Update(int row, float deltaTime, bool faceRight); 
        void setNbSprites(int num, int indice);   
        int getNumAnime() {return this->numAnime ; }
}; 

#endif