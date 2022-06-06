#include "Animation.hpp"

Animation::Animation(sf::Texture* texture, sf::Vector2u imageCount, float switchTime) {
    this->imageCount = imageCount; 
    this->switchTime = switchTime;
    this->indicePlayer = 0; 
    totalTime = 0; 
    currentImage.x = 0; 

    uvRect.width = texture->getSize().x / float(imageCount.x); 
    uvRect.height = texture->getSize().y / float(imageCount.y);
    
    for(int i = 0; i < this->character.getLengthTab(); i++) {
        this->sprites[i] = this->character.getValueTabSprite(i);
    }
}

/*
 setNbSprites : set the number of animation for a movement, based on the indice on his tab
 */
void Animation::setNbSprites(int indice)
{
    this->nbSprites[indice] = this->getSprites(indice);
}

/*
 getSprites : return the number of animations based on the row in the tab
                If row = 0, it matches with "Idle", so it'll return the number of sprites used for the idle
 */
int Animation::getSprites(int row) {
    return this->sprites[row];
}

/*
 Update : Update the position of the player, once an animation is completed, it'will load another one (asked for)
            or repeat this one
 */
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

/*
 setCharacter : set the character of the player : Each player will choose a character, and setting it allows to
                import his datas, like the number of animation or the id of the character
 */
void Animation::setCharacter(Characters charac) {
    this->character = charac;
}
