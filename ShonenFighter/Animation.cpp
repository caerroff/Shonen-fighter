#include "Animation.hpp"

Animation::Animation(sf::Texture* texture, sf::Vector2u imageCount, float switchTime) {
    this->imageCount = imageCount; 
    this->switchTime = switchTime;
    this->indicePlayer = 0; 
    totalTime = 0; 
    currentImage.x = 0; 

    uvRect.width = texture->getSize().x / float(imageCount.x); 
    uvRect.height = texture->getSize().y / float(imageCount.y);
    
    /*spritesItachi[0] = 7;
    spritesItachi[1] = 6;
    spritesItachi[2] = 1;
    spritesItachi[3] = 1;
    spritesItachi[4] = 1;*/
    
    this->sprites[0] = 0; 

}

void Animation::setNbSprites(int indice)
{
    this->nbSprites[indice] = this->getSprites(indice);
}

int Animation::getSprites(int row) {
    return this->sprites[row];
}

void Animation::Update(int row, float deltaTime, bool faceRight) {
    currentImage.y = row; 
    totalTime += deltaTime; 

    if(totalTime >= switchTime) {
        totalTime -= switchTime; 
        currentImage.x++; 

        if(currentImage.x >= this->nbSprites[row]) {
            currentImage.x = 0; 
        }
    }

    uvRect.top = currentImage.y * uvRect.height;  

    if(faceRight){
        uvRect.left = currentImage.x * uvRect.width; 
        uvRect.width = abs(uvRect.width);
    }
    else {
        uvRect.left = (currentImage.x + 1) * abs(uvRect.width); 
        uvRect.width = -abs(uvRect.width); 
    }
}

void Animation::setCharacter(Characters charac) {
    this->character = charac;
}
