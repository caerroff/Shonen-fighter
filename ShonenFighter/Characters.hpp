#ifndef Characters_hpp
#define Characters_hpp

class Characters {
    
private:
    int tabSprites[100];
    int lengthTab = 100;
    int idCharacter;
    
public:
    Characters();
    void setTabSprites(int tabSprites[]);
    int getIdCharacter();
    void setIdCharacter(int id); 
    
};

#endif /* Characters_hpp */

