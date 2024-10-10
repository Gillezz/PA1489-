# Uppgifter

## Front - End

**Index.html**
Två olika "sidor" en som är "beställningssidan" och "order sidan"
beställningssidan => där man kan "beställa" vilken hamburgare man vill ha
order sidan => Visar vilka ordrar som har skapats

**KRAV**
Det ska gå att ta bort och lägga till olika ingredienser

**Databas**
**FRÅGA** Är det ett krav att hamburgarna ska ligga på databasen? Eller går det att antingen bara hårdkåda in det i htmt eller skapa en Json fil.

**Hur jag tänker det ska vara** Orders sparas på databasen med följande keys
**EX:**

```
1 == True
0 == False
----------------------------------------------------------------
| Id | burgerName   | meat | lettuce | tomato | cheese | sauce |
----------------------------------------------------------------
|  1 | Cheeseburger |  1   |    1    |   0    |    1   |   1   |
|  2 | Veggie Burger|  0   |    1    |   1    |    1   |   0   |
|  3 | Bacon Burger |  1   |    0    |   0    |    1   |   1   |
----------------------------------------------------------------
```

Där man bara visar Burger name och alla ingredienser som har värdet 1/True

### TESTER

Tester jag tänker kommer att vara nödväniga

Vi vill testa response codes (200 - 299 (GRÖNT)) Det vill säga att det vi gjorde blev godkänt eller ej för att se hur dessa scenarier utspelar sig
Databas connection
POST method
GET method

### Verktygslåda

1. Git
2. Github
3. Visual Studio Code
4. Podman

#### "Språk"

1. Python
2. HTML
3. CSS

#### Server

1. MYSQL
