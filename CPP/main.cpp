#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>
#include "Player.hpp"
#include "Platform.hpp"
#include "Perso.hpp"

static const float VIEW_HEIGHT = 1200.0f; 

void ResizeView(const sf::RenderWindow& window, sf::View& view) {
    float aspectRatio = float(window.getSize().x) / float(window.getSize().y);
    view.setSize(VIEW_HEIGHT * aspectRatio, VIEW_HEIGHT); 
}

int main()
{
    sf::RenderWindow window(sf::VideoMode(1280, 720), "Shonen Fighter - CPP", sf::Style::Close | sf::Style::Resize);
    sf::View view(sf::Vector2f(0.0f, 0.0f), sf::Vector2f(VIEW_HEIGHT, VIEW_HEIGHT)); 
    sf::Texture playerTexture; 
    playerTexture.loadFromFile("Sprites/Sprites.png"); 
    //playerTexture.loadFromFile("../Naruto/Stand/Sprite1.png"); 

    //Perso perso("Naruto", "Naruto", true); 

    //Player player(perso.getTexture(), sf::Vector2u(16, 14), 0.5f, 500.0f, 400.0f);
    Player player(&playerTexture, sf::Vector2u(12, 30), 0.15f, 500.0f, 400.0f); //16, 14

    std::vector<Platform> platforms;

    sf::Texture grass;
    grass.loadFromFile("Sprites/grass_cuted.jpg"); 

    platforms.push_back(Platform(&grass, sf::Vector2f(400.0f, 150.0f), sf::Vector2f(500.0f, 150.0f))); 
    //platforms.push_back(Platform(&playerTexture, sf::Vector2f(400.0f, 200.0f), sf::Vector2f(500.0f, 0.0f))); 
    platforms.push_back(Platform(&grass, sf::Vector2f(2000.0f, 200.0f), sf::Vector2f(000.0f, 500.0f))); 

    float deltaTime = 0.0f; 
    sf::Clock clock; 

    while(window.isOpen()) 
    {
        deltaTime = clock.restart().asSeconds();

        sf::Event evnt; 
        while(window.pollEvent(evnt)) 
        {
            switch(evnt.type)
            {
                case sf::Event::Closed:
                    window.close(); 
                    break; 
                case sf::Event::Resized:
                    ResizeView(window, view); 
                    break;
            }
        }

    player.Update(deltaTime); 

    sf::Vector2f direction; 

    for(Platform& platform : platforms) 
        if(platform.GetCollider().CheckCollision(player.GetCollider(), direction, 1.0f)) 
            player.OnCollision(direction); 
        
    view.setCenter(player.GetPosition());

    window.clear(sf::Color(150, 150, 150)); 
    window.setView(view); 
    player.Draw(window); 
    for(Platform& platform : platforms)
        platform.Draw(window); 

    window.display(); 
    } 

    return 0; 
}