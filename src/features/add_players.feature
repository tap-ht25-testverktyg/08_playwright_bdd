Feature: Lägga till spelare

  Scenario: Lägga till två spelare
    Given att vi är på sidan
    When användaren klickar på "Lägg till spelare"
    And användaren skriver "David"
    And användaren klickar på "Lägg till spelare"
    Then spelaren "David" visas i listan över spelare
    When användaren skriver "Anna"
    And användaren klickar på "Lägg till spelare"
    Then spelaren "Anna" visas i listan över spelare
