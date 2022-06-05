#ifndef PLAYER_H
#define PLAYER_H

#include <SFML/Graphics.hpp>
#include "Animation.hpp"
#include "Collider.hpp"
#include "Characters.hpp"

class Player {
    private:
        sf::RectangleShape body; 
        Animation animation; 
        unsigned int row; 
        float speed; 
        bool faceRight;
        
        sf::Vector2f velocity; 
        bool canJump; 
        bool isJump; 
        float jumpHeight;

        bool moveKey[100]; 
        int nbMoveKey = 5; //Default 5 : Idle, Moving (Left / Right), Jumping, Falling, Block: Add +1 when new movement (spell, throw, other actions..)
    
        int idPlayer;
        
    public: 
        Player(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed, float jumpHeight); 
        void Update(float deltaTime);
        void Draw(sf::RenderWindow& window);  
        void OnCollision(sf::Vector2f direction); 

        void resetMoveKey(); 

        sf::Vector2f GetPosition() { return body.getPosition(); }
        Collider GetCollider() { return Collider(body); }
    
        void setIdPlayer(int idPlayer);
};

#endif
