#include <SFML/Graphics.hpp>
#include "Player.hpp"
#include "Characters.hpp"
#include "math.h"
#include <iostream>

bool isCombo1 = true;
int cptCombo = 0;

Ath playerAth(-450);
Ath player2Ath(150);

Player::Player(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed, float jumpHeight, float posX) :
    animation(texture, imageCount, switchTime)
{
    this->speed = speed;
    this->jumpHeight = jumpHeight;
    row = 0; 
    faceRight = true;

    body.setSize(sf::Vector2f(100.0f, 151.0f));
    body.setOrigin(body.getSize() / 2.0f); 
    body.setPosition(posX, 206.0f); 
    body.setTexture(texture);
}


/*
 resetMoveKey : Once an animation is completed, the animation of a current animation will be reset
                It allows to begin each animation from 0 and not with the current moment of the last one
 */
void Player::resetMoveKey() {
    for(int i = 0; i < nbMoveKey; i++) {
        moveKey[i] = false; 
    }
}

int Player::printPosition() {
    int valueX = body.getPosition().x;
    //std::cout << valueX << std::endl;
}

/*
 isOnScreen : checks if the player is on the screen or not
    This function allows to see the player everytime on the screen, when he tries to go off, he will go back / get blocked in the corder of the window
 */
bool Player::isOnScreen() {
    bool onScreen = true;
    
    if(body.getPosition().x < -465) {
        body.setPosition(-464, body.getPosition().y);
        onScreen = false;
    }
    
    if(body.getPosition().x > 465) {
        body.setPosition(464, body.getPosition().y);
        onScreen = false;
    }
    
    return onScreen;
}

/*
 update : update the movements of the character
 */
void Player::Update(float deltaTime) {
    
    velocity.x = 0.0f; 
    
    isOnScreen();
    
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Q))  { // Left / Right Movement = moveKey[1]
        velocity.x -= speed;   
        moveKey[1] = true;
    }

    if(sf::Keyboard::isKeyPressed(sf::Keyboard::D)) { // Left / Right Movement = moveKey[1]
        velocity.x += speed; 
        moveKey[1] = true;
    }

    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Z) && canJump) { // Jump = moveKey[2]
        moveKey[2] = true;
        canJump = false;
        velocity.y = -sqrtf(2.0f * 981.0f * jumpHeight); 
        isJump = true; 
    }
        
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::S)) { // Block = moveKey[4]
        moveKey[4] = true;
    }

    velocity.y += 981.0f * deltaTime; 
    isJump = false;
    
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::W)) { // Molding = moveKey[5]
        moveKey[5] = true;
    }
    
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::C)) { // Molding = moveKey[5]
        if(cptCombo%2 == 0) {
            isCombo1 = true;
            cptCombo = 0; 
        } else {
            isCombo1 = false;
        }
        cptCombo++;
        moveKey[8] = true;
    }
    
    if(moveKey[2]) {
        //Need to be fixed (no animation for now)
        row = 2;
        animation.setNbSprites(row);
    }
    
    if(velocity.x == 0.0f) {
            if(moveKey[4]) {
                row = 4;
                animation.setNbSprites(row);
            }
            else if(moveKey[5]) {
                row = 5;
                animation.setNbSprites(row);
            }
            else if(moveKey[8]) {
                if(isCombo1) {
                    row = 8;
                } else {
                    row = 9;
                }
                //row = 8;
                animation.setNbSprites(row);
            }
            else {
                row = 0;
                animation.setNbSprites(row);
            }
        }
        else {
            
            row = 1;
            animation.setNbSprites(row);

            if(velocity.x > 0.0f) {
                faceRight = true;
            } else {
                faceRight = false;
            }
        } 

    resetMoveKey(); 

    animation.Update(row, deltaTime, faceRight); 
    body.setTextureRect(animation.uvRect); 
    body.move(velocity * deltaTime); 
}

/*
 OnCollision : Detect the collision (hitbox) with other objects of the scene, and block the player if he reachs
                one of them
 */
void Player::OnCollision(sf::Vector2f direction) {

    if(direction.x < 0.0f) {
        velocity.x = 0.0f; //Collision on the left
    }
    else if (direction.x > 0.0f) {
        velocity.x = 0.0f; // Collion on the right 
    }
    if(direction.y < 0.0f) {
        //Collision on the buttom
        velocity.y = 0.0f; 
        canJump = true; 
    }
    else if(direction.y > 0.0f) {
        velocity.y = 0.0f; 
    }
}

/*
 draw : draw the character on the scene
 */
void Player::Draw(sf::RenderWindow& window) {
    window.draw(body);
    playerAth.Draw(window);
    //player2Ath.Draw(window);
}

/*
 setIdPlayer : set the id of the player : each player has is own id
 */
void Player::setIdPlayer(int idPlayer) {
    this->idPlayer = idPlayer; 
}

