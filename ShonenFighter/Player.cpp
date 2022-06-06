#include <SFML/Graphics.hpp>
#include "Player.hpp"
#include "Characters.hpp"
#include "math.h"
#include <iostream>

Player::Player(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed, float jumpHeight) :
    animation(texture, imageCount, switchTime)
{
    this->speed = speed;
    this->jumpHeight = jumpHeight;
    row = 0; 
    faceRight = true; 

    body.setSize(sf::Vector2f(100.0f, 151.0f));
    body.setOrigin(body.getSize() / 2.0f); 
    body.setPosition(206.0f, 206.0f); 
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

/*
 update : update the movements of the character
 */
void Player::Update(float deltaTime) {

    velocity.x = 0.0f; 

    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Q)) { // Left / Right Movement = moveKey[1] 
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
    
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::S)) { // Block = moveKey[2] 
        moveKey[4] = true; 
    }

    velocity.y += 981.0f * deltaTime; 
    isJump = false;
    
    if(moveKey[2]) {
        //Marche pas ! A fixer ! 
        row = 2;
        animation.setNbSprites(row);
    }
    
    if(velocity.x == 0.0f) {
            if(moveKey[4]) {
                row = 4;
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
}

/*
 setIdPlayer : set the id of the player : each player has is own id
 */
void Player::setIdPlayer(int idPlayer) {
    this->idPlayer = idPlayer; 
}

