#ifndef PLAYER_H
#define PLAYER_H

#include <SFML/Graphics.hpp>
#include "Animation.hpp"
#include "Collider.hpp"
#include "Characters.hpp"
#include "Ath.hpp"

class Player {
    private:
        sf::RectangleShape body; 
         
        unsigned int row; 
        float speed; 
        bool faceRight;
        
        sf::Vector2f velocity; 
        bool canJump; 
        bool isJump; 
        float jumpHeight;

        bool moveKey[100]; 
        int nbMoveKey = 20; //Default 5 : Idle, Moving (Left / Right), Jumping, Falling, Block: Add +1 when new movement (spell, throw, other actions..)
    
        int idPlayer = 1;
        int hp = 100;
        int mana = 0;     
        
    public:
    Animation animation;
        Player(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed, float jumpHeight, float posX); 
        void Update(float deltaTime);
        void Draw(sf::RenderWindow& window);  
        void OnCollision(sf::Vector2f direction); 
        bool isOnScreen();  
        void resetMoveKey(); 

        int printPosition(); 
    
        sf::Vector2f GetPosition() { return body.getPosition(); }
        Collider GetCollider() { return Collider(body); }
    
        void setIdPlayer(int idPlayer);
};

#endif
