#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>
#include "Player.hpp"
#include "Platform.hpp"
#include "Perso.hpp"
#include "Characters.hpp"
#include "Itachi.hpp"
#include "Ath.hpp"

static const float VIEW_HEIGHT = 1000.0f;

void ResizeView(const sf::RenderWindow& window, sf::View& view) {
    float aspectRatio = float(window.getSize().x) / float(window.getSize().y);
    view.setSize(VIEW_HEIGHT * aspectRatio, VIEW_HEIGHT); 
}

int main()
{
    sf::RenderWindow window(sf::VideoMode(2560, 1600), "Shonen Fighter - CPP", sf::Style::Close);
    sf::View view(sf::Vector2f(0.0f, 0.0f), sf::Vector2f(VIEW_HEIGHT, VIEW_HEIGHT));
    sf::Texture playerTexture; 
    playerTexture.loadFromFile("Sprites/Sprites_Itachi.png");
    playerTexture.loadFromFile("/Users/mohamed/Documents/GitHub/Shonen-fighter/ShonenFighter/Sprites/Sprites_Itachi.png");
    
    Player player(&playerTexture, sf::Vector2u(12, 30), 0.15f, 500.0f, 400.0f, -300.0f);
    Player player2(&playerTexture, sf::Vector2u(12, 30), 0.15f, 500.0f, 400.0f, 200.0f);

    //player selected = Itachi : (Add menu)
    Itachi itachi;
    player.animation.setCharacter(itachi);
    player2.animation.setCharacter(itachi);
    player2.setIdPlayer(2); 
    
    std::vector<Platform> platforms;

    sf::Texture grass;
    //grass.loadFromFile("Sprites/grass_cuted.jpg");
    grass.loadFromFile("Sprites/grass_cuted.jpg");
    grass.loadFromFile("/Users/mohamed/Documents/GitHub/Shonen-fighter/ShonenFighter/Sprites/grass_cuted.jpg");

    platforms.push_back(Platform(&grass, sf::Vector2f(400.0f, 150.0f), sf::Vector2f(500.0f, 150.0f))); 
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
    player2.Update(deltaTime);
        
    player.printPosition(); 

    sf::Vector2f direction; 

    for(Platform& platform : platforms) 
        if(platform.GetCollider().CheckCollision(player.GetCollider(), direction, 1.0f)) 
            player.OnCollision(direction);
        
    for(Platform& platform : platforms)
        if(platform.GetCollider().CheckCollision(player2.GetCollider(), direction, 1.0f))
            player2.OnCollision(direction);
        
    //view.setCenter(player.GetPosition());
        
    window.clear(sf::Color(150, 150, 150)); 
    window.setView(view); 
    player.Draw(window);
    player2.Draw(window);
    for(Platform& platform : platforms)
        platform.Draw(window); 

    window.display(); 
    } 

    return 0; 
}
