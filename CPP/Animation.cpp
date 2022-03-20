#include "Animation.hpp"

Animation::Animation(sf::Texture* texture, sf::Vector2u imageCount, float switchTime) {
    this->imageCount = imageCount; 
    this->switchTime = switchTime; 
    totalTime = 0; 
    currentImage.x = 0; 

    uvRect.width = texture->getSize().x / float(imageCount.x); 
    uvRect.height = texture->getSize().y / float(imageCount.y); 
}

void Animation::setNbSprites(int num, int indice) {
    this->nbSprites[indice] = num; 
    this->numAnime = num; 
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